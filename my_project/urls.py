from django.http import HttpResponse
from django.urls import path
from django.contrib import admin

def hardcoded_test(request):
    return HttpResponse("HARDCODED TEST WORKS", content_type="text/plain")
from my_app.views import test_view

urlpatterns = [
    path('hardcoded-test/', hardcoded_test),
    path('admin/', admin.site.urls),
    path('api/books/', test_view),  # Your original view

]