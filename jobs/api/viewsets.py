from rest_framework import viewsets, mixins
from jobs.models import Company, JobPosting, Applicant
from .serializer import CompanySerializer, JobPostingSerializer, ApplicantSerializer


# class CompanyViewSet(viewsets.ModelViewSet):
#    queryset = Company.objects.all()
#    serializer_class = CompanySerializer


class CompanyViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobPostingViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer


class ApplicantViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer



