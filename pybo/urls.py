from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/',views.test,name='test'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('question/delete/<int:question_id>/',views.question_delete,name='question_delete'),
    path('question/create/',views.question_create,name='question_create'),
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    path('answer/delete/<int:answer_id>/',views.answer_delete,name='answer_delete'),
]