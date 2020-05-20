from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Video, Playlist
from django.utils import timezone
from pytube import YouTube
from pytube import Playlist
# Create your views here.
def index(request):
    if request.method=='POST':
        link = request.POST['link']
        yt=YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
        
        context = {"url": 'link'}

    else:
        context = {}
    return render(request, 'pirate/inputForm.html', context)
