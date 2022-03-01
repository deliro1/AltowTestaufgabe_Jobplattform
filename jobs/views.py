from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Company, Applicant, JobPosting


class CompanyListView(ListView):
    model = Company
    template_name = 'jobs/home.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name']


class JobpostingListView(ListView):
    model = JobPosting
    template_name = 'jobs/jobposting_list.html'
    context_object_name = 'jobpostings'


class JobpostingDetailView(DetailView):
    model = JobPosting


class JobpostingCreateView(CreateView):
    model = JobPosting
    fields = ['title', 'description', 'company']


class ApplicantListView(ListView):
    model = Applicant
    template_name = 'jobs/applicant_list.html'
    context_object_name = 'applicants'


class ApplicantDetailView(DetailView):
    model = Applicant


class ApplicantCreateView(CreateView):
    model = Applicant
    fields = ['name', 'email', 'jobPosting']

