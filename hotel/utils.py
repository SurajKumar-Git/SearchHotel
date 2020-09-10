from math import acos, sin, cos
from django.db.models import F, Func
from django.db.models.functions import ACos, Sin, Cos, Radians
from django.db.models import F, Value as V


def distance_expression(user_latitude, user_longitude):

    # Radius of Earth
    R = float(6371)

    dist_formula = ACos(
                (Sin(Radians('latitude')) * Sin(Radians(user_latitude))) + 
                (Cos(Radians('latitude')) * Cos(Radians(user_latitude)) * Cos(Radians(F('longitude') - user_longitude)))
                ) * R

    return dist_formula
