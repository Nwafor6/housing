from django.contrib import admin
from .models import House,HouseImages

# Register your models here.

admin.site.register(HouseImages)
class AdminHouse(admin.ModelAdmin):
    list_display=["agent","available","lodge_id","price",
    "subsequent_price","balcony","kitchen","waldrop","tiled","posted_on"
    ]
admin.site.register(House,AdminHouse)


