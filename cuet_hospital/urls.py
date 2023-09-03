from django.contrib import admin
from django.urls import path, include
from common.views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('doctor/', include('patients.urls')),
]

# accounts/login
# accounts/register
