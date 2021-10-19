from django.conf.urls import url
from restaurant_app import views

#template tagging
app_name = "restaurant_app"

urlpatterns=[
    # url('formpage/',views.form_view,name='form_view'),
    url('home/',views.home,name='home'),
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
    url('south/',views.south_indian_food,name='south_indian_food'),
    url('south_indian_breakfast/',views.south_indian_breakfast,name='south_indian_breakfast'),
    url('south_indian_lunch/',views.south_indian_lunch,name='south_indian_lunch'),
    url('south_indian_dinner/',views.south_indian_dinner,name='south_indian_dinner'),
    url('north/',views.north_indian_food,name='north_indian_food'),
    url('north_indian_breakfast/',views.north_indian_breakfast,name='north_indian_breakfast'),
    url('north_indian_lunch/',views.north_indian_lunch,name='north_indian_lunch'),
    url('north_indian_dinner/',views.north_indian_dinner,name='north_indian_dinner'),
    url('ordered_item/',views.ordered_item,name='ordered_item'),
    url('Orders/',views.order,name='order'),
]
