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

def productManagement(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/productManagement.html', context=context)

def entrepreneurship2(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/entrepreneurship2.html', context=context)

def marketing(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/marketing.html', context=context)

def economics(request):

    context = { 'page_id' : 'course_1_main' }

    return render(request,'courses/economics.html', context=context)