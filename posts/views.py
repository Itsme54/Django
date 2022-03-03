from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import Post, Comment
from posts.form import CommentForm, CreatepostForm


def createpost_view(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            posts = Post.objects.filter(user=request.user)
            context = {"posts": posts}
            title = request.POST['title']
            blog_content = request.POST['blog_content']

            # url = request.POST['imgURL']
            post = Post(title=request.POST['title'], blog_content=request.POST['blog_content'], user=request.user.id)
            post.save()
            messages.success(request, 'Post created successfully')
            return render(request, 'home/index.html', context)
        else:
            return render(request, 'posts/post.html')
    else:
        return render(request, 'home/login.html')


def post_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "posts/post_index.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data["name"],
                comment_body=form.cleaned_data["form_body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "posts/post_detail.html", context)
