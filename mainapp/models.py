from django.db import models
from accounts.models import CustomUser as User
from  accounts import utils

# Create your models here.
Amenities=[("Yes","Yes"),("No","No")]
Types=[("Self-Contain","Self-Contain"),("Flat","Flat"),("Boys-Quater","Boys-Quater"),]

class House(models.Model):
    agent=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lodge_id=models.CharField(max_length=50, null=True, blank=True)
    location=models.CharField(max_length=200)
    cover_img=models.ImageField(blank=True, null=True, upload_to="lodge_cover_img")
    price=models.PositiveIntegerField()
    type=models.CharField(max_length=30, choices=Types,blank=True, null=True)
    subsequent_price=models.PositiveIntegerField()
    description=models.TextField()
    balcony=models.CharField(max_length=30, choices=Amenities)
    kitchen=models.CharField(max_length=30, choices=Amenities)
    waldrop=models.CharField(max_length=30, choices=Amenities)
    tiled=models.CharField(max_length=30, choices=Amenities)
    contact=models.CharField(max_length=30)
    distance_to_school=models.CharField(max_length=50)
    available=models.CharField(max_length=30, choices=Amenities)
    posted_on=models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.lodge_id

    def save(self, *args, **kwargs):
        # Check for a slug        
        if not self.lodge_id:
            # Create default slug
            self.lodge_id = self.gen_random_slug()
        # Finally save.
        super().save(*args, **kwargs)


class HouseImages(models.Model):
    house=models.ForeignKey(House, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="house_images")

    def __str__(self):
        return f"{self.house} images"
    

