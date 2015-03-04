from django.shortcuts import render, get_object_or_404
from blogapp.models import Post
from blogapp.models import Comment

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_id):
    posts = get_object_or_404(Post, pk=blog_id)
    comment = Comment.objects.filter(post_id = blog_id)
    return render(request, 'blogapp/detail.html', {'post': posts, 'comment': comment})
