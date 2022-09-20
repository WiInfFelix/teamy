from django.urls import path

from .views import OrganisationList, OrganisationDetail

urlpatterns = [
    path("", OrganisationList.as_view(), name="org-list"),
    path("<int:pk>", OrganisationDetail.as_view(), name="org-detail")
]
