from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.course),
    path('courses/<int:pk>', views.course_detail)
]
