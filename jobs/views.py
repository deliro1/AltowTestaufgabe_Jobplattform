from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'jobs/company_confirm_delete.html'
    success_url = '/'


class JobpostingListView(ListView):
    model = JobPosting
    template_name = 'jobs/jobposting_list.html'
    context_object_name = 'jobpostings'


class JobpostingDetailView(DetailView):
    model = JobPosting


class JobpostingCreateView(CreateView):
    model = JobPosting
    fields = ['title', 'description', 'company']


class JobpostingDeleteView(DeleteView):
    model = JobPosting
    template_name = 'jobs/jobposting_confirm_delete.html'
    success_url = '/'


class ApplicantListView(ListView):
    model = Applicant
    template_name = 'jobs/applicant_list.html'
    context_object_name = 'applicants'


class ApplicantDetailView(DetailView):
    model = Applicant


class ApplicantCreateView(CreateView):
    model = Applicant
    fields = ['name', 'email', 'jobPosting']


class ApplicantDeleteView(DeleteView):
    model = Applicant
    success_url = '/'
