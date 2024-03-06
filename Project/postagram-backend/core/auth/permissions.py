from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is anonymous
        if request.user.is_anonymous:
            # If the request method is safe (GET, HEAD, OPTIONS), allow access
            return request.method in SAFE_METHODS
        # For non-anonymous users, only allow access if they are authenticated
        return bool(request.user and request.user.is_authenticated)

        if view.basename in ["post-comment"]:
            if request.method in ['DELETE']:
                return bool(request.user.is_superuser or request.user in [obj.author, obj.post.author])
            return bool(request.user and request.user.is_authenticated)

    def has_permission(self, request, view):
        if view.basename in ["post", "post-comment"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool(request.user and request.user.is_authenticated)
        # For other views, deny permission
        return False

