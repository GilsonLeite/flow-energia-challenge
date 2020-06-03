from django import forms


class ForecastForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ForecastForm, self).__init__(*args, **kwargs)
        self.fields['forecastedate'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YYYY/M/D'})
        self.fields['area_id'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['scenarioname'].widget.attrs.update(
            {'class': 'form-control'})

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

    forecastedate = forms.CharField(label='Forecast Date')
    scenarioname = forms.ChoiceField(
        choices=SCENARIONAME, label='Scenario Name')
    area_id = forms.ChoiceField(choices=AREAID, label='AreaID')
