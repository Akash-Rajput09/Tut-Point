from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_chapters = models.PositiveIntegerField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    enrollment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"id = {self.id} name = {self.name}" 
    
    
class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    chapter_number = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')

    class Meta:
        unique_together = ('course', 'chapter_number')
        ordering = ['chapter_number']

    def __str__(self):
        return f"Chapter {self.chapter_number}: {self.title}"
    
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return f"Video {self.title} for Chapter {self.chapter.chapter_number}"