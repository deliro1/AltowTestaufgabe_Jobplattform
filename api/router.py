from .viewsets import CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
