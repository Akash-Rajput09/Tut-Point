from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('preview/<int:id>/', views.preview, name='preview'),
    path('create/', views.create, name='create'),
    path('addchapter/<int:course_id>/', views.addchapter, name='addchapter'),
    path('cdcreate/<int:course_id>/', views.coursedetailscreator, name='cdcreate'),
    path('delete_chapter/<int:chapter_id>/', views.delete_chapter, name='deletechapter'),
    path('edit_chapter/<int:chapter_id>/', views.editchapter, name='editchapter'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('enrolledin/',views.enrolledcourses, name='enrolledin'),
]
