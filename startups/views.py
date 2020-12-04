from django.shortcuts import render
from startups.models import Startup
# Create your views here.
def indexView(request):
    startups = Startup.objects.all()
    args = {'startups' : startups}
    return render(request,'startups/index.html', args)
