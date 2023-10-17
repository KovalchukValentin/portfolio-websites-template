import datetime

from django.db import models


class Day_of_week(models.Model):
    monday = models.BooleanField(default=True, verbose_name='Monday')
    tuesday = models.BooleanField(default=True, verbose_name='Tuesday')
    wednesday = models.BooleanField(default=False, verbose_name='Wednesday')
    thursday = models.BooleanField(default=True, verbose_name='Thursday')
    friday = models.BooleanField(default=True, verbose_name="Friday")
    saturday = models.BooleanField(default=False, verbose_name='Saturday')
    sunday = models.BooleanField(default=False, verbose_name='Sunday')

    class Meta:
        verbose_name = 'Work days'
        verbose_name_plural = 'Work days'

    def __str__(self):
        return f'{"Mo | " if self.monday else ""}' \
               f'{"Tu | " if self.tuesday else ""}' \
               f'{"We | " if self.wednesday else ""}'\
               f'{"Th | " if self.thursday else ""}'\
               f'{"Fr | " if self.friday else ""}'\
               f'{"Sa | " if self.saturday else ""}'\
               f'{"Su | " if self.sunday else ""}' \
               f' Work days'


class Time_cell(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = 'cell'
        verbose_name_plural = 'Work cells'

    def __str__(self):
        return f'{(self.time).strftime("%H:%M")}'



# Create your models here.
