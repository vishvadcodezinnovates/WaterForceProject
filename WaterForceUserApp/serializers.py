from rest_framework import serializers
from WaterForceUserApp.models import *


class ClientSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSlider
        fields = "__all__"