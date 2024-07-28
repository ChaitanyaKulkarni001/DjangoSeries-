# from django.urls import path
# from . import views
# urlpatterns = [
#     path('watchlist/',views.WatchListAll.as_view()),
#     path('watchlist/<int:id>/',views.getDetail.as_view(),name = 'get_movie_detail'),
#     path('stream/',views.watchStreamplatform.as_view()),
#     path('stream/<int:id>/',views.GetStream.as_view(),name='get_stream_detail'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('watchlist/', views.WatchListAll.as_view()),
    path('get_detail/<int:id>/', views.getDetail.as_view(), name='get_movie_detail'),
    path('stream/', views.watchStreamPlatform.as_view()),
    path('get_stream/<int:id>/', views.GetStream.as_view(), name='get_stream_detail'),
]
