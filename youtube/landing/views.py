# from django.views.generic import TemplateView
from .forms import NoPageSendingForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


# class LandingView(TemplateView):
#     template_name = "landing.html"
#
#     def get_context_data(self, **kwargs):
#         response = super().get_context_data(**kwargs)
#         response['name'] = 'Chandr'
#         response['current_day'] = '03.03.2017'
#         return response


class NoPageCreateView(SuccessMessageMixin, CreateView):
    form_class = NoPageSendingForm
    success_url = '/'
    template_name = 'landing.html'
    context_object_name = 'form'
    success_message = ''

    def from_valid(self, form):
        response = super().form_valid(form)
        View = form.save()
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        form = request.POST
        print(form)
        return response

    def get_success_message(self, cleaned_data):
        return 'Спасибо {} Вы успешно подписались'.format(dict(cleaned_data)['name'])
