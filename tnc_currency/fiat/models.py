from django.db import models


class Fiat(models.Model):
    from_currency = models.CharField(max_length=255)
    to_currency = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        """returns string representation of the user"""
        return self.from_currency + ' to ' + self.to_currency
