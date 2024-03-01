import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

logger = logging.getLogger(__name__)

class RegistrationView(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Account has been successfully created', status=201)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during registration', status=500)

class ActivationView(APIView):

    @swagger_auto_schema(request_body=ActivationSerializer)
    def post(self, request):
        try:
            serializer = ActivationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.activate()
            return Response('User has been activated', status=200)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during activation', status=500)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('You have successfully logged out')
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during logout', status=500)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def post(self, request):
        try:
            serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.set_new_password()
            return Response('Password has been changed', status=200)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during password change', status=500)

class ForgotPasswordView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def post(self, request):
        try:
            serializer = ForgotPasswordSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.send_verification_email()
            return Response('Password recovery code has been sent to your email', status=200)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during password recovery', status=500)

class ForgotPasswordCompleteView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordCompleteSerializer)
    def post(self, request):
        try:
            serializer = ForgotPasswordCompleteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.set_new_password()
            return Response('Password has been changed', status=200)
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            return Response('An error occurred during password change', status=500)
