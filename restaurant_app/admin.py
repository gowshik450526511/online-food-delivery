from django.contrib import admin
from restaurant_app.models import UserProfileInfo,User
from restaurant_app.models import south_breakfast
from restaurant_app.models import north_breakfast
from restaurant_app.models import north_lunch
from restaurant_app.models import south_lunch
from restaurant_app.models import south_dinner
from restaurant_app.models import north_dinner
from restaurant_app.models import orders

# Register your models here.
admin.site.register(south_breakfast)
admin.site.register(south_lunch)
admin.site.register(south_dinner)
admin.site.register(north_breakfast)
admin.site.register(north_lunch)
admin.site.register(north_dinner)
admin.site.register(UserProfileInfo)
admin.site.register(orders)
