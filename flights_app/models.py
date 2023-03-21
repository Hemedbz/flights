from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *


class Airport(models.Model):
    class Meta:
        db_table = 'airports'

    airport_code = models.CharField(max_length=5, unique=True)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    timezone = models.SmallIntegerField(validators=[MinValueValidator(-24), MaxValueValidator(24)])
            # examples: +3, -12. UTC will be 0

class Flight(models.Model):
    class Meta:
        db_table = 'flights'

    flight_number = models.PositiveIntegerField()
    origin_airport = models.ForeignKey(Airport, related_name='origin_code', db_column='origin', on_delete=models.RESTRICT)
    destination_airport = models.ForeignKey(Airport, related_name='destination_code', db_column='destination', on_delete=models.RESTRICT)
    date_time_departure = models.DateTimeField()
    date_time_arrival = models.DateTimeField()
    total_seats = models.PositiveSmallIntegerField()
    seats_left = models.PositiveSmallIntegerField()
            # Django documentation says 0 is acceptable, \
            # if this returns error will need to switch to small integer
    is_cancelled = models.BooleanField(default=False)
    price = models.PositiveSmallIntegerField()
        # future: move price to ticket
        # for now, one price is assumed for all seats


class Order(models.Model):
    class Meta:
        db_table = "orders"

    outbound_flight = models.ForeignKey(Flight, on_delete=models.RESTRICT)
    # future:
    # inbound_flight = models.ForeignKey('flight', on_delete=models.RESTRICT)
    # for now each order will be one way
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    number_of_tickets = models.SmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(12)))
    order_date = models.DateField(auto_now_add=True)
    total_price = models.IntegerField()

# future:
# class Passenger(models.Model):
#     class Meta:
#         db_table = "passengers"
#
#     full_name =
#     sex =
#     passport_num =
#     passport_expiration =
#
# class Tickets(models.Model):
#     class Meta:
#         db_table = "tickets"
#
#     ticket_num =
#     order_id =
#     passenger_id =
#     row =
#     seat =
#     meal =
#     price =