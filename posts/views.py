from django.shortcuts import render
from posts.models import Post, Comment
from posts.form import CommentForm


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
