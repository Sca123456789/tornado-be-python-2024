from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
# from core.post.viewsets import PostViewSet
from rest_framework_nested import routers
from core.post.viewsets import PostViewSet

# User Routes
router = routers.SimpleRouter()
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"user", UserViewSet, basename="user")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"post", PostViewSet, basename="post")
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')

urlpatterns = [
    *router.urls,
]
