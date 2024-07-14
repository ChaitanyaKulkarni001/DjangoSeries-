from django.urls import path
from . import views
urlpatterns = [
    path('serieslist',views.series_list),
    path('get_series_detail/<int:id>/',views.get_series_detail),
]
