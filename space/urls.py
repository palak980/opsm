from django.urls import path, include
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI
from space import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name="register"),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('/api/password_reset/confirm/',include('django_rest_passwordreset.urls', namespace='password_confirm')),
    path('get/', views.snippet_list, name='get'),
    path('PutDeletePatch/<int:pk>', views.snippet_detail, name='PutDeletePatch'),
]
