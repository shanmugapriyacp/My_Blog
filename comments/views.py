from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from users.models import Post


@login_required
def comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment_form = CommentForm()
    post_comments = Comment.objects.filter(post_id=post_id, parent_id__isnull=True)

    if request.method == 'POST':
        data = { 'user_id': request.user.id,
                 'post_id': post_id,
                 'parent_id': request.POST.get('parent_id'),
                 'content': request.POST.get('content'),
               }
        c = Comment(**data)
        c.save()
    return render(request, 'comment.html', {'post': post, 'comment_form': comment_form, 'post_comments': post_comments})

