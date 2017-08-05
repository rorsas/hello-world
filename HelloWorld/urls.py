from django.conf.urls import url
 
from . import view,testdb,search,search2
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^base$', view.base),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search), 
    url(r'^search-post$', search2.search_post),
]

