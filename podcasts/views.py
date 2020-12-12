from django.shortcuts import render

# Create your views here.
def index(request):
    context={'page_id': 'podcast_main'}
    return render(request,'podcast/index.html',context)
