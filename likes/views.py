from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Likes


@login_required
def likes(request, post_id):
    if request.method == 'POST':
        data = { 'user_id': request.user.id,
                 'post_id': post_id,
               }
        print(data)
        ob = Likes(**data)
        ob.save()
        return redirect('/')
    else:
        try:
            likes = Likes.objects.filter(post_id=post_id)
        except:
            return redirect('/')
        return render(request, 'likes.html', {'likes': likes})

