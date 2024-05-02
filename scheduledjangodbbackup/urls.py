from django.contrib import admin
from django.urls import path
from blog.scheduler import scheduler

urlpatterns = [
    path('admin/', admin.site.urls),
]

scheduler.start()
