
from blog.models import Post
from django.shortcuts import render, get_object_or_404
#import datetime
from django.utils.timezone import now

# Create your views here.




def index(request):
    post_list = Post.objects.all().filter(status=True).exclude(pub_date__gte=now()).order_by('-created')[:15]
    context = {'post_list': post_list}
    return render(request, 'blog/index_post.djhtml', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail_post.djhtml', {'post': post})
    
