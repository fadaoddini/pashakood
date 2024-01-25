from django.views import View
from django.shortcuts import render


class MainIndex(View):
    template_name = 'web/index/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()

        if request.user.is_anonymous:
            context['user'] = "hello dear ...!"

        else:
            context['user'] = "hello !"

        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


