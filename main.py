from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json_data: bytes) -> Car:
    stream = BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise Exception(f"Invalid data: {serializer.errors}")
