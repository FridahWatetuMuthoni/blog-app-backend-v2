from rest_framework.permissions import BasePermission, SAFE_METHODS

class PostUserWritePermission(BasePermission):
    message = 'Editing and Writting posts is restricted to the author only '
    
    def has_object_permission(self, request, view, obj):
        #check if the http method is in the safe_methods
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user