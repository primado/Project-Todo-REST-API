from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):    
        if obj.user == request.user:
            return True
        return False
    

class IsOwnerCanEdit(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH'] and obj.user == request.user:
            return True
        return False


        
