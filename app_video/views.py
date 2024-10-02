from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
# Messages
from django.contrib import messages
#form
from app_video.forms import VideoForm
from django.contrib.auth import logout
from app_video.models import Video
# Create your views here.

def homepage(request):
  video=Video.objects.all()
    
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

@login_required
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
            return HttpResponseRedirect(reverse('user_handle:homepage'))
        else:
            messages.error(request, "There was an error adding the video. Please try again.")
    
    return render(request, 'app_video/add_video.html', context={'form': form})
        
        
        
        
  
    
  
