from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state + ", " + str(self.country)


class District(models.Model):
    district = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.district + ", " + str(self.state)


class City(models.Model):
    city = models.CharField(max_length=30, verbose_name='City/Town')
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city + ", " + str(self.district)


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    pincode = models.IntegerField(verbose_name='Pin Code')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.city) + " - " + str(self.pincode)