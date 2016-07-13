from django.shortcuts import render
from blog.models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',{'post_list':posts})

def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/post_detail.html',{'post':post})

