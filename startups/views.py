from django.shortcuts import render
from startups.models import Startup
# Create your views here.
def index(request):
    startups = Startup.objects.all()

    context = {'startups' : startups, 'body_id' : 'startups', 'section_id': 'startups_header'}

    return render(request,'startups/index.html', context)
