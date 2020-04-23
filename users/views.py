from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, PostForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def new_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})
