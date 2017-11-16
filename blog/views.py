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

def add_post(request):
    
    if request.method == "POST":
        # Get the details from the request
        form = BlogPostForm(request.POST, request.FILES)
        # Handle saving to DB
        if form.is_valid():
            form.save()
            return redirect(post_list)
    else:
        # GET Request so just give a blank form
        form = BlogPostForm()
    return render(request, "blogpostform.html", { 'form': form })

def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(post_list)
    else:
        form = BlogPostForm(instance=item)
        
    return render(request, "blogpostform.html", { 'form': form })  
    
def viewpost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render (request, "viewpost.html", {'post': post })

