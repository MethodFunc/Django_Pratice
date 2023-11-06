from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter

# NameSpace 역활
app_name = 'instagram'

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    # path('archives/<int:year>', views.archives_years),
    # re_path(r'archives/(?P<year>\d{3,4})/', views.archives_years),
    path('archives/<year:year>/', views.archives_years),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('archive/', views.post_archive, name="post_archive"),
    path('archive/<year:year>', views.post_archive_year, name="post_archive_year"),
    # path('archive/<year:year>/<month:month>', views.post_archive_year, name="post_archive_year"),
    # path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_year, name="post_archive_year"),
]
