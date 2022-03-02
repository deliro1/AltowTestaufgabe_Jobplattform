from rest_framework.response import Response
from rest_framework import viewsets
from jobs.models import Company
from .serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

