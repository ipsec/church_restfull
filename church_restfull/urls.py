from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet
from courses.views import StudentClassViewSet, CourseViewSet, StudentViewSet, TeacherViewSet
from news.views import NewsViewSet

router = routers.DefaultRouter()
# Core APP
router.register(r'users', UserViewSet)

# News APP
router.register(r'news', NewsViewSet)

# Courses APP
router.register(r'course', CourseViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)
router.register(r'student_class', StudentClassViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('users/', UserList.as_view()),
    # path('users/<pk>/', UserDetails.as_view()),
    # path('groups/', GroupList.as_view()),
]
