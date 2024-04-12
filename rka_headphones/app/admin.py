from django.contrib import admin
from .models import Headphone, Cable, Eartip, HeadphoneCombination

admin.site.register(Headphone)
admin.site.register(Cable)
admin.site.register(Eartip)
admin.site.register(HeadphoneCombination)
