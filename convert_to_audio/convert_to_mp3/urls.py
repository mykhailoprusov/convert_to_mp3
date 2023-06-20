from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page,name="home-page"),
    path('download_mp3/<int:audio_id>/',views.download_mp3, name='download-mp3')

]
