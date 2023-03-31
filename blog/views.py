from django.shortcuts import render,HttpResponse

from blog.models import BlogPost

# Create your views here.

def index(request):
    blogcard= BlogPost.objects.all();
    bl= {"blogCard":blogcard}
    return render(request, "blog/index.html",bl)

def blogpost(request,blogid):
   postCard= BlogPost.objects.filter(post_id=blogid)[0]
   bl= {"postCard":postCard}
   return render(request, "blog/blogpost.html",bl)