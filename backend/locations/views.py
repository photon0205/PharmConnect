from rest_framework import generics, permissions
from .models import UserLocation
from .serializers import UserLocationSerializer

class UserLocationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserLocation.objects.filter(user=self.request.user)

    serializer_class = UserLocationSerializer

class UserLocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer