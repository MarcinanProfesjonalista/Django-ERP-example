from django.contrib import admin

# Register your models here.
from produkcja.models import Product, Machine, Sensor, Location_sensor_in_machine,  Order, number_of_elements_from_the_order, the_number_of_elements_from_the_order_to_pass_through_the_machine
from produkcja.models import sensor_log

admin.site.register(Product)
admin.site.register(Machine)
admin.site.register(Sensor)
admin.site.register(Location_sensor_in_machine)
admin.site.register(sensor_log)
admin.site.register(Order)
admin.site.register(number_of_elements_from_the_order)
admin.site.register(the_number_of_elements_from_the_order_to_pass_through_the_machine)