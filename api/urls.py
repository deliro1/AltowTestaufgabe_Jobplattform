from django.urls import path, include
from . import views
from .router import router


urlpatterns = [
    path('', views.getData),
    path('new/', views.addCompany),
    path('api/', include(router.urls))
]