# from django.shortcuts import render,HttpResponse
# from .models import Series
# from django.http import JsonResponse
# # Create your views here.

# def series_list(request):
#     series_list = Series.objects.all()
#     print(series_list)
#     data = {
#         'series_list':list(series_list.values()),
        
#     }
#     # return  HttpResponse (f'series_list: {series_list[0].description}')
#     return JsonResponse(data)

# def get_series_detail(request,id):
#     series = Series.objects.get(id=id)
#     print(series)
#     data = {
#         'name' : series.name,
#         'description' : series.description,
#         'active' : series.activate
#     }
#     return JsonResponse(data)