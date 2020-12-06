from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request,'courses/index.html')

def entrepreneurship(request):
    return render(request,'courses/entrepreneurship.html')

def finance(request):
    return render(request,'courses/finance.html')

def cryptocurrency(request):
    return render(request,'courses/cryptocurrency.html')
