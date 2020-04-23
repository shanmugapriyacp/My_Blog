from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    post_id = forms.IntegerField(widget=forms.HiddenInput)
    parent_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(label='', widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['user_id', 'post_id', 'parent_id', 'content']