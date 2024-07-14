from .serializers import SeriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from watchlist_app.models import Series


@api_view(['GET', 'POST', 'PUT'])
def series_list(request):
    if request.method == 'GET':    
        series_list = Series.objects.all()
        serializer = SeriesSerializer(series_list,many=True )
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT','DELETE'])
def get_series_detail(request,id):
    if request.method == 'GET':
        series_list = Series.objects.get(id=id)
        serializer = SeriesSerializer(series_list)
        return Response(serializer.data)

    if request.method == 'PUT':
        series = Series.objects.get(id= id)
        serializer = SeriesSerializer(series ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE' :
        series = Series.objects.get(id=id)
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)