from django.urls import path, re_path, register_converter
from . import views

# NameSpace 역활
app_name = 'instagram'


class YearConvert:
    regex = r'\d{3,4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


register_converter(YearConvert, 'yyyy')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>', views.archives_years),
    # re_path(r'archives/(?P<year>\d{3,4})/', views.archives_years),
    path('archives/<yyyy:year>/', views.archives_years),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail)
]
