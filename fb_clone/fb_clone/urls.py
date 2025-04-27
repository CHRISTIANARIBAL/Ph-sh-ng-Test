from django.contrib import admin
from django.urls import path
from accounts.views import login_view, spin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),

    path('', spin_view, name='spin'),
]
