from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.rest import viewsets as booksviewsets

route = routers.DefaultRouter()
route.register(r'', booksviewsets.BooksViewSet, basename='Books')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls))
]
