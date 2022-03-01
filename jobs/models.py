from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobposting-detail', kwargs={'pk': self.pk})


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    jobPosting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('appliant-detail', kwargs={'pk': self.pk})

