# # Custom permission

from rest_framework import permissions 

class isAdminorReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission =  bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_permission

class ReviewUserorReadoOnly(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check permissions for read-only request
        else:
            return obj.user_name == request.user
    