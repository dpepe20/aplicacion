from postapp import views
from django.conf.urls import url

from django.urls import path, include
from postapp.views import PostListAPIView,AddPost,ShowPost,GeneroAllAPIView,CategoryIdAPIView
#,GeneroIdAPIView

urlpatterns = [
	path('list/', views.PostListAPIView.as_view(), name='restpost-list'),
    path('add/',views.AddPost.as_view(),name= 'restpost-add'),
    path('<id>/',views.ShowPost.as_view(), name = 'restpost-show'),

    path('genero/list/',views.GeneroAllAPIView.as_view(), name='restpost-list-genero'),

    
    path('genero/list/<id>', views.CategoryIdAPIView.as_view(), name='restpost-genero-id'),



    #path('gener/<id>', views.GeneroIdAPIView.as_view(), name='restpost-genero-id'),
    
]