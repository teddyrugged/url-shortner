from . import views
from django.urls import path


urlpatterns = [
    path('firstpage/', views.new_page)
]
