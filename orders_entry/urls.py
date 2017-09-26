from django.conf.urls import url, include

from . import views

app_name = 'orders_entry'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^nueva-orden/$', views.new_order, name='new_order'),
    url(r'^pdf/$', GeneratePDF.as_view(), name='pdf'),
]
