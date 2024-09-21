from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = request.user.userprofile  # Attach the logged-in user's profile
            post.save()
            form.save_m2m()  # Save many-to-many fields (like tags if applicable)
            return redirect('community:home')  # Redirect to the post list after successful creation
    else:
        form = PostForm()

    context = {
        'form': form
    }
    
    return render(request, 'community/create_post.html', context)


@login_required
def home(request):
   user_profile = request.user.userprofile
   posts = Post.objects.all().order_by('-created_at')
   context ={
       'user_profile':user_profile,
       'posts':posts
   }
   return render(request, 'community/home.html', context)


