from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import BlogPostForm, BlogCommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify



# Create your views here.
#def get_index(request):
    #return render(request, "index.html")

def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
                
        return render(request, "blogposts.html", {'posts': posts})
    
def viewpost(request, slug):
    this_post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=this_post)
    form = BlogCommentForm()
    this_post.views += 1
    this_post.save()
    return render (request, "viewpost.html", {'post': this_post, 'comments': comments, 'form': form })

def whatever(request):
    return render (request, "404.html")

@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method == "POST":
        # Get the details from the request
        form = BlogPostForm(request.POST, request.FILES)
        # Handle saving to DB
        if form.is_valid():
            post= form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(post_list)
    else:
        # GET Request so just give a blank form
        form = BlogPostForm()
    return render(request, "blogpostform.html", { 'form': form })

def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(post_list)
    else:
        form = BlogPostForm(instance=post)
        
    return render(request, "blogpostedit.html", { 'form': form, 'post': post })  


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(post_list)
    
def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    form = BlogCommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        
        comment.author = request.user
        comment.created_date = timezone.now()
        comment.post = post
        
        comment.save()
        return redirect('viewpost', post_slug)



