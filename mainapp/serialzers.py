from rest_framework import serializers 
from accounts.serializers import UserSerializer
from .models import House,HouseImages

class HouseSerializer(serializers.ModelSerializer):
    agent=UserSerializer(many=False)
    class Meta:
        model=House
        fields=["id","agent","location","type","contact","available","lodge_id","cover_img","price","description",
    "subsequent_price","balcony","kitchen","waldrop","tiled","posted_on"
    ]

class House_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=HouseImages
        fields=["house","image",]


class ContactTeamSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=100, required=True)
	email=serializers.EmailField(required=True)
	subject=serializers.CharField(max_length=100, required=True)
	message=serializers.CharField(max_length=500, required=True)