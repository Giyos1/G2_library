from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include,re_path

from config import settings


def index(request):
    return HttpResponse(f"Hello, Django!")


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('books/', include('books.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('tran/', include('transactions.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
