from django.shortcuts import render

# Create your views here.
def index(request):
    context={'page_id':'team_main'}
    return render(request,'team/index.html',context)
