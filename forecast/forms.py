from django import forms
from django.forms.fields import ChoiceField


class ForecastForm(forms.Form):
    SCENARIONAME = (
        ('EC-P25', 'EC-P25'),
        ('EC-P50', 'EC-P50'),
        ('EC-P75', 'EC-P75')
    )
    AREAID = (
        (1, 'AreaID 1'),
        (2, 'AreaID 2'),
        (3, 'AreaID 3'),
        (4, 'AreaID 4')
    )

    forecastedate = forms.CharField(label='Date ForecastDate YYYY/M/D')
    scenarioname = forms.ChoiceField(
        choices=SCENARIONAME, label='ScenarioName')
    area_id = forms.ChoiceField(choices=AREAID, label='AreaID')
