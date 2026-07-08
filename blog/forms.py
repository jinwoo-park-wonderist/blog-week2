from django import forms
from blog.models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content', 'post_tag']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_content']