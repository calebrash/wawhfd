from django.conf.urls import url
from django.contrib import admin

from wawhfd.views import (
    IndexView,
    DatesListView,
    DatesEditView,
    DatesDeleteView,
    RecipesListView,
    RecipesAddView,
    RecipesEditView,
    RecipesDeleteView,
)


urlpatterns = [
    url(r'^$', IndexView.as_view()),

# blah/00-00-0000/lsadfljk/
    url(r'^api/dates/$', DatesListView.as_view()),
    url(r'^api/dates/(?P<date_str>[\d]{4}-[\d]{2}-[\d]{2})/edit/$', DatesEditView.as_view()),
    url(r'^api/dates/(?P<date_str>[\d]{4}-[\d]{2}-[\d]{2})/delete/$', DatesDeleteView.as_view()),

    url(r'^api/recipes/$', RecipesListView.as_view()),
    url(r'^api/recipes/add/$', RecipesAddView.as_view()),
    url(r'^api/recipes/(?P<recipe_id>[\d]+)/edit/$', RecipesEditView.as_view()),
    url(r'^api/recipes/(?P<recipe_id>[\d]+)/delete/$', RecipesDeleteView.as_view()),

    url(r'^admin/', admin.site.urls),
]
