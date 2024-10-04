from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
# Messages
from django.contrib import messages
#form
from app_video.forms import VideoForm,CommentForm
from django.contrib.auth import logout
from app_video.models import Video,Comment
from django.db.models import Q
# Create your views here.

def homepage(request):
  video=Video.objects.all().order_by('?')
  return render(request,'app_video/video_list.html',context={'video':video})

def get_youtube_thumbnail(url):
    # Extract the video ID from the URL
    video_id = url.split('v=')[1]
    ampersand_position = video_id.find('&')
    if ampersand_position != -1:
        video_id = video_id[:ampersand_position]

    # Construct the thumbnail URL
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return thumbnail_url


def add_video(request):
    # Only allow superusers to access this view
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to do that.")
        logout(request)
        return redirect('user_handle:login_user')  # Assuming you have a 'login_user' URL pattern

    # Initialize the form
    form = VideoForm()

    if request.method == "POST":
        form = VideoForm(data=request.POST)
        if form.is_valid():
            # Save form without committing to get the instance
            video = form.save(commit=False)
            link = form.cleaned_data.get('link')
            thumbnail = get_youtube_thumbnail(link)
            video.thumbnail = thumbnail  # Assign thumbnail before saving the instance
            video.save()  # Now save the instance
            messages.success(request, "Video added to the database successfully!!")
            return HttpResponseRedirect(reverse('app_video:homepage'))
        else:
            messages.error(request, "There was an error adding the video. Please try again.")
    
    return render(request, 'app_video/add_video.html', context={'form': form})
        
        
def vid_search(request):
    query=request.GET.get('q')
    if query:
        video=Video.objects.filter(
            Q(title__icontains=query) |  # Case-insensitive search in title
            Q(category__icontains=query)  # Case-insensitive search in category
            )
        return render(request,'app_video/video_list.html',context={'video':video})
    
    else:
        messages.error(request,"Nothing Found!!")
        return HttpResponseRedirect(reverse('app_video:homepage'))


  
def vid_details(request, pk):
    # Fetch other videos, excluding the current one
    video = Video.objects.all().exclude(pk=pk).order_by('?')

    # Fetch the video being viewed
    vid_q = get_object_or_404(Video, pk=pk)

    # Fetch comments for the current video
    comments = Comment.objects.filter(commented_video=vid_q)

    # Initialize the comment form
    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(data=request.POST)  # Populate form with POST data
            if form.is_valid(): 
                comment = form.save(commit=False)
                comment.user = request.user  # Set the user
                comment.commented_video = vid_q  # Associate comment with the current video
                comment.save()

                messages.success(request, "Comment Added Successfully!!")

                # Redirect to the same page to prevent duplicate form submissions
                return redirect(reverse('app_video:vid_details', kwargs={'pk': pk}))
            else:
                messages.error(request, "Comment Not Added!!")
        else:
            messages.error(request, "Please Login First!!")
            return redirect(reverse('user_handle:login_user'))  # Redirect to login if not authenticated

    # Render the page with the video details and comment form
    return render(request, 'app_video/video_details.html', context={
        'video': video,
        'vid_q': vid_q,
        'comments': comments,
        'form': form,
    })
         

    
  
