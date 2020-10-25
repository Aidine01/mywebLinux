from django.contrib import admin
from django.urls import path, include

from ecommerce.views import (home_page, about_page, contact_page, login_page, register_page, logout_page)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_page, name = 'about'),
    path('contact/', contact_page, name = 'contact'),
    path('', home_page, name = 'homepage'),
    path('login/', login_page, name = 'login'),
    path('register/', register_page, name = "register"),
    path('logout/', logout_page, name = 'logout'),
]