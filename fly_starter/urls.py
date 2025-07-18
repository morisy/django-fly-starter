# hello_django/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.http import JsonResponse



# ↓ New basic view returning "Hello, Fly!" ↓
def hello(request):
    return HttpResponse("Hello, Fly!")

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello, name="hello"),  # ← Added!
    path('health/', health_check),
]