from django.contrib import admin
from .models import Company, JobPosting, Applicant

admin.site.register({Company, JobPosting, Applicant})
