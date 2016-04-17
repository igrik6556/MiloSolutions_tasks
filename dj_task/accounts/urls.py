from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.list_all_user, name="main"),
    url(r'^view/(?P<user_id>\d+)/$', views.view_user, name="view_user"),
    url(r'^add/$', views.add_user, name="add_user"),
    url(r'^edit/(?P<user_id>\d+)/$', views.edit_user, name="edit_user"),
    url(r'^delete/(?P<user_id>\d+)/$', views.delete_user, name="delete_user"),
    url(r'^save_csv/$', views.csv_list, name="save_csv"),
]
