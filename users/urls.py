from django.urls import path
from users import views, api

app_name = 'users'

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("profile-page/", views.ProfileView.as_view(), name="profile-page"),
    path("register-page/", views.RegisterView.as_view(), name="register-page"),
    path("login-page/", views.LoginView.as_view(), name="login-page"),
    path("update-profile-page/", views.UpdateView.as_view(), name="update-profile-page"),
    path("logout/", views.LogoutView, name="logout"),

    path("register/", api.RegisterViewSet.as_view({
        'post': 'post',
    }), name='register'),

    path("login/", api.LoginViewSet.as_view({
        'post': 'post',
    }), name="login"),

    path("profile/<int:id>/", api.UserViewSet.as_view({
        'get':'get',
        'put': 'put',
    }), name="profile"),
]
