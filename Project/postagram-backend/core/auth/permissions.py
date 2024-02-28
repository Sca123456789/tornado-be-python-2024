from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is anonymous
        if request.user.is_anonymous:
            # If the request method is safe (GET, HEAD, OPTIONS), allow access
            return request.method in SAFE_METHODS
        # For non-anonymous users, only allow access if they are authenticated
        return bool(request.user and request.user.is_authenticated)

    def has_permission(self, request, view):
        # Check if the view basename is 'post'
        if view.basename in ["post"]:
            # For 'post' views, handle permissions differently
            if request.user.is_anonymous:
                # If the request user is anonymous and the method is safe, allow access
                return request.method in SAFE_METHODS
            # For non-anonymous users, only allow access if they are authenticated
            return bool(request.user and request.user.is_authenticated)
        return False
