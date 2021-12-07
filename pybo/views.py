from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def main_index(request):
    return render(request, 'index.html')
def test(request):
    return HttpResponse("test")
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)#id값으로 필터해서 보여줌
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)