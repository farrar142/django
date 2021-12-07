from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/',views.test,name='test'),
    path('<int:question_id>/',views.detail,name='detail')
]