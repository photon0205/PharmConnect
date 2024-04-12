from accounts.permissions import IsCEO
from accounts.serializers import UserLoginSerializer, UserSerializer
from companies.models import Company, Store
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Worker
from .serializers import WorkerSerializer


class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                }
            }

            if user.role == "CEO":
                company = Company.objects.filter(ceo=user).first()
                if company:
                    response_data["company"] = {
                        "id": company.id,
                        "name": company.name,
                    }

            elif user.role == "STORE_MANAGER":
                store = Store.objects.filter(manager=user).first()
                if store:
                    response_data["company"] = {
                        "id": store.company.id,
                        "name": store.company.name,
                    }
                    response_data["store"] = {
                        "id": store.id,
                        "name": store.name,
                    }

            return Response(response_data)
        else:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

class UserLogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response(
                {"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"success": "Successfully logged out"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST
            )


class WorkerListCreateAPIView(APIView):
    permission_classes = [IsCEO]

    def get(self, request):
        ceo_company = Company.objects.filter(ceo=request.user).first()
        if ceo_company:
            stores = ceo_company.stores.all()
            workers = Worker.objects.filter(store__in=stores)
            serializer = WorkerSerializer(workers, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "CEO's company not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerDetailAPIView(APIView):
    permission_classes = [IsCEO]

    def get(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    def delete(self, request, pk):
        worker = self.get_object(pk)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
