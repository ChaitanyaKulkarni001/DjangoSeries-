
# from serializers import Serializers
from rest_framework import serializers
from watchlist_app.models import Series













# Basics
'''
class SeriesSerializer(serializers.ModelSerializer):
    # Cutsom Fields
    len_names = serializers.SerializerMethodField()
    
    def get_len_names(self,object):
        length = len(object.name)
        return length
    def validate_name(self, name):
        if len(name) < 2:
            raise serializers.ValidationError("Name should be at least 2 characters long")
        return name
#     #  Object level validation 
    class Meta:
        model = Series
        fields = "__all__"
        
        # fields = ('id','name','description','activate')
        # exclude= ['activate']
        
'''














#---------------------------------------------------------------->

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name should be at least 2 characters long")
    
# class SeriesSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     #  Validator 
#     name  = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     activate = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Series.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Series` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.activate = validated_data.get('activate', instance.activate)
#         instance.save()
#         return instance
    
#     # Filed level validation 
    
#     # def validate_name(self, name):
#     #     if len(name) < 2:
#     #         raise serializers.ValidationError("Name should be at least 2 characters long")
#     #     return name
#     #  Object level validation 
#     # def validate(self,data):
#     #     if data['name'] == data['description']:
#     #         raise serializers.ValidationError("Name and description cannot be the same")
#     #     return data
