from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Hotel_Booking)
admin.site.site_header='Travel'
admin.site.index_title='Travel Site Administration'
