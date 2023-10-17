import calendar
import datetime

from django.http import JsonResponse
from django.views import View

from .models import Time_cell

from .services import get_working_dates_list_in_format, get_working_time_cells_list_in_format

from website.models import *


class WorkDatesJSONView(View):
    def get(self, request):
        return JsonResponse({"work_dates": get_working_dates_list_in_format("%d.%m")}, safe=False)


class WorkTimeCellsJSONView(View):
    def get(self, request):
        if request.method == 'GET':
            return JsonResponse({"work_time_cells": get_working_time_cells_list_in_format(date=request.GET.get('date_str'), _format="%H:%M")})
        return JsonResponse({'success:': False})