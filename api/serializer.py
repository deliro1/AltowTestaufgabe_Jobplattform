from rest_framework import serializers
from jobs.models import Company, JobPosting, Applicant


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobPostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
