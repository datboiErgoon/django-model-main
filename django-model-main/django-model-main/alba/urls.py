from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('', views.index, name='index'),
path('albums/', views.AlbumListView.as_view(), name='albums'),
path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
path('albums/zanr/<str:album_zanr>/', views.AlbumListView.as_view(), name='album-zanr'),
]