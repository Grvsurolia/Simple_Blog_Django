
from django.urls import path
from .views import MyObtainTokenPairView, RegisterView, UserViewSet, GetAllBlog, CreateBlog, UpdateDeleteBlog
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('v1/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/register/', RegisterView.as_view(), name='auth_register'),
    path('v1/get-profile/', UserViewSet.as_view(), name='getprofile'),
    path('get-blog/', GetAllBlog.as_view(), name='get-blog'),
    path('create-blog/', CreateBlog.as_view(), name='create-blog'),
    path('get-blog-by-id/<int:pk>/', UpdateDeleteBlog.as_view(), name='get-blog-by-id'),
    path('update-blog-by-id/<int:pk>/', UpdateDeleteBlog.as_view(), name='update-blog-by-id'),
    path('delete-blog-by-id/<int:pk>/', UpdateDeleteBlog.as_view(), name='delete-blog-by-id'),
]