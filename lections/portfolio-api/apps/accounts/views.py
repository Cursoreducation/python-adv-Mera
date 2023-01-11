from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsOwnerOrReadOnly
from .serializers import RegisterSerializer


User = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ...


class UpdateProfileAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )
    serializer_class = ...


class DeleteProfileAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


register = RegisterAPIView.as_view()
change_password = ChangePasswordAPIView.as_view()
update_profile = UpdateProfileAPIView.as_view()
delete_profile = DeleteProfileAPIView.as_view()
logout = LogoutAPIView.as_view()
