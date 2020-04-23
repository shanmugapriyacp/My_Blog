from django.shortcuts import render
from users.models import Post
from comments.forms import CommentForm


def home(request):
    posts = Post.objects.order_by('-date_published')
    return render(request, 'home_page.html', {'posts': posts, 'comment_form':CommentForm()})
