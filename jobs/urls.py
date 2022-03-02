from django.urls import path
from .views import (CompanyListView, CompanyDetailView, CompanyCreateView, CompanyDeleteView,
                    JobpostingCreateView, JobpostingListView, JobpostingDetailView, JobpostingDeleteView,
                    ApplicantListView, ApplicantDetailView, ApplicantCreateView, ApplicantDeleteView
                    )


urlpatterns = [
    path('', CompanyListView.as_view(), name='jobs-home'),

    path('company/', CompanyListView.as_view(), name='jobs-home'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/new/', CompanyCreateView.as_view(), name='company-create'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),

    path('jobposting/', JobpostingListView.as_view(), name='jobposting-list'),
    path('jobposting/<int:pk>/', JobpostingDetailView.as_view(), name='jobposting-detail'),
    path('jobposting/new/', JobpostingCreateView.as_view(), name='jobposting-create'),
    path('jobposting/<int:pk>/delete/', JobpostingDeleteView.as_view(), name='jobposting-delete'),

    path('applicant/', ApplicantListView.as_view(), name='applicant-list'),
    path('applicant/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    path('applicant/new/', ApplicantCreateView.as_view(), name='applicant-create'),
    path('applicant/<int:pk>/delete/', ApplicantDeleteView.as_view(), name='applicant-delete'),

]
