"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.urls import path, re_path, include
from arches_keep_app.views.keep import ChangesView, ConceptsExportView
from arches_keep_app.views.keep_export import process_resource

urlpatterns = [
    re_path(r"^resource/changes", ChangesView.as_view(), name="ChangesView"),
    re_path(r"^concept/export", ConceptsExportView.as_view(), name="ConceptsExportView"),    
    re_path(r"^keep/export/$", process_resource, name='process_resource'),
]

urlpatterns.append(path("", include("arches.urls")))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))