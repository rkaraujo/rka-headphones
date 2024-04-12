from rest_framework import generics
from .models import Headphone, Cable, Eartip, HeadphoneCombination
from .serializers import HeadphoneSerializer, CableSerializer, EartipSerializer, HeadphoneCombinationSerializer


class HeadphoneListView(generics.ListAPIView):
    queryset = Headphone.objects.all()
    serializer_class = HeadphoneSerializer


class CableListView(generics.ListAPIView):
    queryset = Cable.objects.all()
    serializer_class = CableSerializer


class EartipListView(generics.ListAPIView):
    queryset = Eartip.objects.all()
    serializer_class = EartipSerializer


class HeadphoneCombinationListView(generics.ListAPIView):
    queryset = HeadphoneCombination.objects.all()
    serializer_class = HeadphoneCombinationSerializer
