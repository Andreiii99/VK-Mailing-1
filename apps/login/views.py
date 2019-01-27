from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .functions import login


class LogUserInView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        response = HttpResponseRedirect(self.get_success_url())

        if user:
            response = login(response, user)
        return response
