from django.contrib import admin
from django.urls import path
from accounts.views import login_view, signup_view, spin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('', spin_view, name='spin'),
]
