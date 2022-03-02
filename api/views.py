from rest_framework.response import Response
from rest_framework.decorators import api_view
from jobs.models import Company
from .serializer import CompanySerializer


@api_view(['GET'])
def getData(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)