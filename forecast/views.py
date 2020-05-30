from django.views.generic import TemplateView


class ForecastDetailView(TemplateView):
    template_name = 'forecast/analysis_result.html'

    def get_context_data(self, **kwargs):
        return {'name': 'reinout'}
