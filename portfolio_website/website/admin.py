from django.contrib import admin
from .models import Offer, Order, Gallery_image, Certificate_image

# Register your models here.

admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(Gallery_image)
admin.site.register(Certificate_image)
