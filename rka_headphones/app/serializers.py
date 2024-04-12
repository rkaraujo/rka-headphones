from rest_framework import serializers
from .models import Headphone, Cable, Eartip, HeadphoneCombination


class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphone
        fields = '__all__'


class CableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cable
        fields = '__all__'


class EartipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eartip
        fields = '__all__'


class HeadphoneCombinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadphoneCombination
        fields = '__all__'
