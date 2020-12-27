from django.shortcuts import render
from podcasts.models import Podcast

# Create your views here.
def index(request):

    all_podcasts = Podcast.objects.all()
    context={'page_id': 'podcast_main', 'all_podcasts' : all_podcasts }
    
    return render(request,'podcast/index.html',context)
