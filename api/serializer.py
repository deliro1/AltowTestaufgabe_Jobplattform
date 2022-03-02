from rest_framework import serializers
from jobs.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        #fields = '__all__'
        fields = ['name']
