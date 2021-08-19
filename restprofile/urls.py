
from django.conf.urls import url

from django.urls import path, include

from restprofile import views
from restprofile.views import *



urlpatterns = [
	path('list/',views.ListAuthor.as_view(), name='list'),
	path('delete/<int:id>/',views.DeletePost.as_view(), name = 'delete'),
	path('edit/<int:id>/', views.PostUpdateAPIView.as_view(), name='edit'),
]