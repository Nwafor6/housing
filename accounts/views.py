from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer,LoginSerializer
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser as User





class SignUp(generics.CreateAPIView):
	serializer_class=UserSerializer

class Login(generics.CreateAPIView):

	serializer_class=LoginSerializer

	def post(self, request, *args, **kwargs):
		email=request.POST['email']
		password=request.POST['password']

		try:
			print("hello")
			User.objects.get(email=email, is_staff=True)
		except:
			return Response("Error!! No such email or not a staff email")

		user=authenticate(request,email=email, password=password)
		if user is not None:
			login(request,user)
			return Response("Login Successful !!")
		return Response({"detail": "No such email or not a staff email"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout_view(request):
	logout(request)
	return Response("Logout Successful !!")