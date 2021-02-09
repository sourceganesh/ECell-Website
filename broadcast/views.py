from django.shortcuts import render
from broadcast.models import Broadcast
# Create your views here.
def index(request):

    all_broadcast = Broadcast.objects.all()
    context={'page_id': 'blog', 'all_broadcasts' : all_broadcast }
    
    return render(request,'broadcast/index.html',context)
