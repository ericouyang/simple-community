from django.template import RequestContext
from django.shortcuts import render_to_response


def permission_denied(request):
    return render_to_response(
        'errors/permission_denied',
        context_instance=RequestContext(request)
    )
