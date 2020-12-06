from django.shortcuts import render
from blogs.models import BlogPosts

# Create your views here.
def index(request):

    blogs = BlogPosts.objects.all()
    context = { 'blogs' : blogs, 'page_id' : 'blog' }

    return render(request, 'blogs/index.html', context=context)