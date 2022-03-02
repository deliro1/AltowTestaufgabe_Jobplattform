from jobs.api.viewsets import CompanyViewSet, JobPostingViewSet, ApplicantViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('jobposting', JobPostingViewSet)
router.register('applicant', ApplicantViewSet)
