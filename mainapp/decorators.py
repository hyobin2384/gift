from django.http import HttpResponseForbidden

from mainapp.models import Main


def main_ownership_required(func):
    def decorated(request, *args, **kwargs):
        main = Main.objects.get(pk=kwargs['pk'])
        if not main.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
