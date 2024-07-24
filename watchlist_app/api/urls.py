from django.urls import path
from . import views
urlpatterns = [
    path('serieslist/',views.SeriesList.as_view()),
    path('get_series_detail/<int:id>/',views.GetSeriesDetail.as_view()),
]
