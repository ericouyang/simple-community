from django.conf import settings


def google_analytics(request):
    """
    Inject Google Analytics ID into template context

    Based on http://www.nomadblue.com/blog/django/google-analytics-tracking-code-into-django-project/
    """
    ga_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', False)
    if not settings.DEBUG and ga_id:
        return {
            'GOOGLE_ANALYTICS_ID': ga_id,
        }
    return {}
