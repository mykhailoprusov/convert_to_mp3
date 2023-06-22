# convert_to_mp3
Django website that allows converting video into audio files

### Project Description:
This is a django application where users can conveniently upload their MP4 files and effortlessly download the corresponding audio versions. Moviepy
library is used for converting purposes and PostgreSQL database for video and audio data storage.

### Code Organization:
Django project. Main app - config, convert_to_mp3 app - covers everything related to the project, media app contains video and audio files

### Installation and Setup:
You need to have a a config_data.json file in the root
directory that has such data:
```json
{
    "default": {
        "ENGINE": "",
        "NAME": "",
        "HOST": "",
        "PORT": ,
        "USER": "",
        "PASSWORD": ""
    },

    "SECRET_KEY" :
    

}
Make sure to replace the empty values (`""`, ` `) with the actual values for your configuration.
```n

##### Library requirements:
asgiref==3.7.2
backports.zoneinfo==0.2.1
beautifulsoup4==4.12.2
certifi==2023.5.7
charset-normalizer==3.1.0
colorama==0.4.6
crispy-bootstrap4==2022.1
decorator==4.4.2
Django==4.2.2
django-bootstrap4==23.1
django-crispy-forms==2.0
idna==3.4
imageio==2.31.1
imageio-ffmpeg==0.4.8
moviepy==1.0.3
numpy==1.24.3
Pillow==9.5.0
proglog==0.1.10
psycopg2==2.9.6
requests==2.31.0
soupsieve==2.4.1
sqlparse==0.4.4
tqdm==4.65.0
typing_extensions==4.6.3
tzdata==2023.3
urllib3==2.0.3
