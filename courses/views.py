from django.shortcuts import render

# Create your views here.
def index(request):

    context = { 'page_id' : 'courses_main' }

    return render(request,'courses/index.html', context=context)

def entrepreneurship(request):

    context = { 'page_id' : 'course_1_main' }
    
    return render(request,'courses/entrepreneurship.html', context=context)

def finance(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/finance.html', context=context)

def cryptocurrency(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/cryptocurrency.html', context=context)
