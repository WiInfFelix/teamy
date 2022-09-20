from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Organisation
from .serializers import OrganisationSerializer


# Create your views here.
class OrganisationList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


class OrganisationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
