from django.urls import path

from . import views

urlpatterns = [
    path('work_dates', views.WorkDatesJSONView.as_view(), name='work_dates_for_month_json'),
    path('time_cells', views.WorkTimeCellsJSONView.as_view(), name='working_time_cells')
]