from django.shortcuts import render

# Create your views here.
def index(request):

    context = { 'page_id' : 'main' }

    return render(request, 'core/index.html', context=context)

def esummit(request):

    return render(request, 'core/esummit.html')