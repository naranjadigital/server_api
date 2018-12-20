from rest_framework import serializers

from motel.models import *


class MotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motel
        fields = ('__all__')


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ('__all__')