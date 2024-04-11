from rest_framework import generics, permissions
from .models import Company, Store
from .serializers import CompanySerializer, StoreSerializer, StoreManagerSerializer
from accounts.models import User

class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class StoreListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreManagerListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return Store.objects.get(id=store_id).manager.all()

    serializer_class = StoreManagerSerializer

class StoreManagerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = User.objects.filter(role='STORE_MANAGER')
    serializer_class = StoreManagerSerializer