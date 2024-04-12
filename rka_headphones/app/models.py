from django.db import models


class Headphone(models.Model):
    TYPE_CHOICES = [
        ("IEM", "IEM"),
        ("OVER_EAR", "Over ear"),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    buy_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cable(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Eartip(models.Model):
    SIZE_CHOICES = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.size}"


class HeadphoneCombination(models.Model):
    headphone = models.ForeignKey(Headphone, on_delete=models.CASCADE)
    cable = models.ForeignKey(Cable, on_delete=models.CASCADE)
    eartip = models.ForeignKey(Eartip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.headphone.name} / {self.cable.name} / {self.eartip.name} {self.eartip.size}"
