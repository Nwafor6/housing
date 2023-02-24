from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from.models import House,HouseImages
from .serialzers import HouseSerializer, House_ImageSerializer,ContactTeamSerializer
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives

# Create your views here.


class HouseListView(generics.ListAPIView):
    queryset=House.objects.all()
    serializer_class=HouseSerializer


    def get(self, request, *args, **kwargs):
        houses=House.objects.all()
        houses_serializer=self.serializer_class(houses, many=True)
        return Response({"houses":houses_serializer.data})

class HouseDetailView(generics.RetrieveAPIView):
    queryset=House.objects.all()
    serializer_class=HouseSerializer


    def get(self, request, *args, **kwargs):
        house=House.objects.get(pk=self.kwargs["pk"])
        house_images=house.houseimages_set.all()
        image_serializer=House_ImageSerializer(house_images,many=True)
        house_serializer=self.serializer_class(house, many=False)
        return Response({"house":house_serializer.data, "images":image_serializer.data})

class ContactTeamView(generics.CreateAPIView):
	serializer_class=ContactTeamSerializer

	def post(self, request, *args, **kwargs):
		serializer= self.serializer_class(data=request.data)
		if serializer.is_valid():
			name=serializer.data["name"]
			email=serializer.data["email"]
			subject=serializer.data["subject"]
			message=serializer.data["message"]
			msg= EmailMultiAlternatives(subject, message,'info@scholarsjoint.com.ng',[email])
			msg.send()
			return Response({"success":"Message sent !!"})
		return Response({"error":"Error ! Make sure your email is valid."},status=status.HTTP_400_BAD_REQUEST)