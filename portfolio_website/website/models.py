import datetime

from django.db import models

from portfolio_website.settings import TIME_ZONE

STATUS_ORDER_CHOICES = (
    ('waiting', 'Waiting'),
    ('canceled', 'Canceled'),
    ('confirmed', 'Confirmed'),
    ('finished', 'Finished'),)


class Order(models.Model):
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=13)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=300, null=True, blank=True)
    time_cell = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default='waiting', max_length=10, choices=STATUS_ORDER_CHOICES)
    # canceled = models.BooleanField(default=False)
    # confirmed = models.BooleanField(default=False)
    # finished = models.BooleanField(default=False)
    paid_up = models.IntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def _get_status_str(self) -> str:
        if self.status == 'canceled':
            return "Canceled"
        elif self.status == 'confirmed':
            return "Confirmed"
        elif self.status == 'finished':
            return "Payment" if self.paid_up <= 0 else "Finished"
        else:
            return "Waiting"

    def __str__(self):
        return f'{self._get_status_str().upper()} | ' \
               f'{self.name.__str__()} ' \
               f'{self.telephone.__str__()} ' \
               f'{"There is no reserve" if self.time_cell is None else self.get_time_in_time_zone(self.time_cell).strftime("Reserved: %d.%m.%Y %H:%M")} ' \
               f'{self.get_time_in_time_zone(self.date).strftime("Created: %d.%m.%Y %H:%M")} '


    def get_time_in_time_zone(self, date: datetime) -> datetime:
        return date


class Gallery_image(models.Model):
    image = models.ImageField(upload_to='static/media/gallery')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.image.__str__()


class Offer(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return " ".join([self.name.__str__(), self.price.__str__(), '$'])


class Certificate_image(models.Model):
    image = models.ImageField(upload_to='static/media/certificate_gallery')

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return self.image.__str__()