
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from my_app.views import test_view  # Replace `my_app` with your app name
def test_view(request):
    return HttpResponse("DIRECT TEST WORKS!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_view, name='test_view'),  # Must be here
]