from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Course,Chapter,Enrollment,Video
from django.contrib.auth.decorators import login_required


import random
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

def preview(request, id):
    course = get_object_or_404(Course, id=id)
    # doStuff()
    context = {
        'course': course,
        'chapters': course.chapters.all(),
        'count': course.chapters.count()
    }
    return render(request, 'courses/course_details.html', context)

@login_required
def content(request, course_id, chap_num):
    course = get_object_or_404(Course, id=course_id) 
    chapter = get_object_or_404(course.chapters.filter(chapter_number=chap_num))
    previous = chap_num - 1
    next = chap_num + 1
    videos = chapter.videos.all()
    context = {
        'course': course,
        'chapter': chapter,
        'chapters': course.chapters.all(),
        'chapters_total': course.chapters.count(),
        'previous': previous,
        'next': next,
        'current': chap_num,
        'videos': videos
        
    }
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return redirect('preview', id=course.id)
    return render(request, 'courses/course_content.html', context)


@login_required
def create(request):
    course = None
    if request.method == 'POST':
        name = request.POST.get('course_name')
        thumbnail = request.FILES.get('thumbnail')
        price = 0
        author = request.user
        course = Course.objects.create(
            name=name, 
            author=author, 
            thumbnail=thumbnail, 
            price=price, 
            number_of_chapters=0
        )
        
        return redirect('addchapter', course_id=course.id)
    
    return render(request, 'courses/create.html',{'course':course})

@login_required
def addchapter(request, course_id):
    course = Course.objects.get(id=course_id)
    if course.author != request.user:
        return redirect('teach')
    
    if request.method == 'POST':
        title = request.POST.get('chapter_title')
        content = request.POST.get('chapter_content')
        chapter_number = course.chapters.count() + 1

        chapter = Chapter.objects.create(
            title=title,
            content=content,
            chapter_number=chapter_number,
            course=course
        )
        video_files = request.FILES.getlist('video_file')
        video_descriptions = request.POST.get('video-desc')
        video_title = request.POST.get('video-title')
        for video_file in video_files:
                Video.objects.create(
                    title=video_title,
                    video_file=video_file,
                    description=video_descriptions,
                    chapter=chapter
                )
        course.number_of_chapters = course.chapters.count()
        course.save()
        return redirect('cdcreate', course_id=course_id)

    return render(request, 'courses/addchapter.html', {'course': course})

@login_required
def coursedetailscreator(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.author != request.user:
        return redirect('teach')
    return render(request, 'courses/coursedetailscreator.html', {'course': course})


@login_required
def delete_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    course_id = chapter.course.id
    chapter.delete()
    course = get_object_or_404(Course, id=course_id)
    if course.author != request.user:
        return redirect('teach')
    return redirect('cdcreate', course_id=course_id)
@login_required
def editchapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    course_id = chapter.course.id
    course = get_object_or_404(Course, id=course_id)
    if course.author != request.user:
        return redirect('teach')

    if request.method == 'POST':
        title = request.POST.get('chapter_title')
        content = request.POST.get('chapter_content')

        chapter.title = title
        chapter.content = content
        chapter.save()

        return redirect('cdcreate', course_id=chapter.course.id)

    return render(request, 'courses/editchapter.html', {'chapter': chapter})

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if Enrollment.objects.filter(user=request.user, course=course).exists():
        return redirect('content', course_id=course.id, chap_num=1)
    enroll,created = Enrollment.objects.get_or_create(user=request.user, course=course)
    print(f"Enrollment Created: {created}")
    if not created:
        return redirect('preview', course_id=course.id, chap_num=1)
    if created:
        course.enrollment_count += 1
        course.save()
        
    return redirect('content', course_id=course.id, chap_num=1)

@login_required
def enrolledcourses(request):
    user = request.user
    courses = Course.objects.filter(enrollment__user=user)
    return render(request, 'courses/enrolledcourses.html', {'courses':courses})

@login_required
def video(request, video_id):
    # Fetch the video by its ID
    video = get_object_or_404(Video, id=video_id)
    
    # Get the chapter associated with the video
    chapter = video.chapter
    course = chapter.course  # Get the course associated with the chapter
    
    # Get all videos in the same chapter
    videos_in_chapter = chapter.videos.all()
    
    # Get the list of next videos in the same course
    next_videos = Video.objects.filter(chapter__course=course).exclude(id=video.id).order_by('chapter__chapter_number')  # Exclude the current video
    
    return render(request, 'courses/videoplayer.html', {
        'video': video,
        'course': course,
        'next_videos': next_videos,
        'videos_in_chapter': videos_in_chapter  # Optional: if you want to show all videos in the chapter
    })
