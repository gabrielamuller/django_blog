from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import BlogPostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
#def get_index(request):
    #return render(request, "index.html")

def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
                
        return render(request, "blogposts.html", {'posts': posts})
    
def viewpost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render (request, "viewpost.html", {'post': post })

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
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(post_list)
    else:
        # GET Request so just give a blank form
        form = BlogPostForm()
    return render(request, "blogpostform.html", { 'form': form })

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(post_list)
    else:
        form = BlogPostForm(instance=post)
        
    return render(request, "blogpostedit.html", { 'form': form, 'post': post })  


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect(post_list)



