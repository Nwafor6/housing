from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from .managers import CustomUserManager
from django.conf import settings
from .import utils

class CustomUser(AbstractUser):
	username = None 
	email = models.EmailField(unique=True)
	slug=models.SlugField(unique=True, null=True, blank=True)
	profile_image=models.ImageField(blank=True, null=True, upload_to="profile_images")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	objects = CustomUserManager()
	class Meta:
		ordering = ["email"]
		verbose_name = "User"

	def __str__(self):
		return self.email 


	# Creating a default slug/username for users if blank.
	def gen_random_slug(self):
		random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id())
		while CustomUser.objects.filter(slug=random_slug).exists():
			random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id())
		return random_slug
        
	def save(self, *args, **kwargs):
        # Check for a slug        
		if not self.slug:
            # Create default slug
			self.slug = self.gen_random_slug()
        # Finally save.
		super().save(*args, **kwargs)


	def __str__(self):
		return self.email