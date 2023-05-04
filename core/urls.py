from captcha import fields
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.urls import include, path

from .schema import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),  # for browsable api
    path("", include("apps.urls")),  # entry point to other project app urls
    path("sentry-debug/", trigger_error),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.unregister(Group)
