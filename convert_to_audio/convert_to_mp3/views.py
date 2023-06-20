from django.shortcuts import render, redirect
from .forms import UploadVideoForm
from .models import Video
from django.contrib import messages
from moviepy.editor import VideoFileClip
from .models import Audio
from django.http import HttpResponse


def conversion(video_path, output_path,database_path):
    video = VideoFileClip(video_path)
    audio = video.audio

    audio.write_audiofile(output_path,codec='libmp3lame')

    audio_object = Audio(file=database_path)
    audio_object.save()

def start_page(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():


            file_obj = request.FILES['file']
            file_name = file_obj.name
            try:
                instance = Video(file=request.FILES["file"], name = file_name)
                instance.save()
                audio_filename = file_name.replace('.mp4','.mp3')
                conversion(f'media/convert_to_mp3/video/{file_name}',f'media/convert_to_mp3/audio/{audio_filename}',
                           f'convert_to_mp3/audio/{audio_filename}')

                messages.success(request, f"Your video was successfully converted to mp3! ")
                audio_id = Audio.objects.get(file=f'convert_to_mp3/audio/{audio_filename}')

            except Exception as e:
                messages.error(request, "An error occurred while saving the file.")
                return redirect('home-page')

            return render(request, 'convert_to_mp3/start_page.html', context={'form':form,'audio_id':audio_id.id})
        else:
            messages.error(request, 'Your form is invalid')
            form = UploadVideoForm()
            return render(request, 'convert_to_mp3/start_page.html', context={'form':form})
    else:
        form = UploadVideoForm()
        return render(request, 'convert_to_mp3/start_page.html', context={'form':form})


def download_mp3(request,audio_id):
    audio = Audio.objects.get(id=audio_id)
    file_path = audio.file.path

    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename="audio.mp3"'
        return response


