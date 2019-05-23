from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin


class JFBaseView(LoginRequiredMixin, ContextMixin):
    app_title = "Julgamento de Fatos"

    def get_context_data(self, **kwargs):
        context = super(JFBaseView, self).get_context_data(**kwargs)
        context["app_title"] = self.app_title
        return context
