from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog import queries
from blog.forms import PostForm, CommentForm, TagForm
from blog.models import Tag


def post_list(request):
    posts = queries.get_post()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, pk):
    post = queries.get_post(pk)
    comments = queries.get_comments_by_post(pk)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.comment_author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'post.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'form.html', {'form': form})


def tag_list(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('tag_list')
    else:
        tag_form = TagForm()

    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags, 'tag_form': tag_form})


def posts_by_tag(request, tag_id):
    tag = queries.get_tag(tag_id)
    posts = queries.get_posts_by_tag(tag_id)
    return render(request, 'tag_posts.html', {'tag': tag, 'posts': posts})