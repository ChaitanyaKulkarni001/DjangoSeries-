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
    path('reviews/',views.Reviews.as_view()),
    path('watchlist/<int:pk>/', views.getDetail.as_view(), name='get_movie_detail'),
    # path('watchlist/<int:id>/', views.getDetail.as_view(), name='get_movie_detail'), for API View
    path('stream/', views.watchStreamPlatform.as_view()),
    path('stream/<int:id>/', views.GetStream.as_view(), name='get_stream_detail'),
    path('stream/<int:pk>/review/', views.ReviewList.as_view()),
    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view()),
    path('stream/review/<int:pk>/', views.ReviewDetail.as_view(),name='review_detail'),    
    # path('stream/8/reviews/', views.watchStreamPlatform.as_view()),
]
# '''
# # Genral
# path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
# path('reviews/', views.ReviewList.as_view()),
# '''
