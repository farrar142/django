from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def main_index(request):
    return render(request, 'index.html')
def test(request):
    return HttpResponse("test")
def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page','1') # page
    # 조회
    question_list = Question.objects.order_by('-create_date')

    #페이징 처리
    paginator = Paginator(question_list,10)#페이지당 10개씩 보여줌
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj}
    return render(request,'pybo/question_list.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)#id값으로 필터해서 보여줌
    context = {'question':question}

    return render(request,'pybo/question_detail.html',context)

def question_create(request):
    '''
    pybo 질문 등록
    '''
    if request.method =='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/question_form.html',context)

def question_delete(request,question_id):
    question = get_object_or_404(Question, pk=question_id)#id값으로 필터해서 보여줌
    #question.delete()#게시물 삭제 후
    question_list = Question.objects.order_by('-create_date')#다시 담아서
    context = {'question_list':question_list}#컨텍스트에 담음.

    return render(request, 'pybo/question_list.html', context)
#
def answer_create(request,question_id):
    '''
    pybo 답변 등록
    '''
    question = get_object_or_404(Question,pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail',question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question,'form': form}
    return render(request, 'pybo/question_detail.html', context)

def answer_delete(request,question_id):
    '''
    pybo 답변 삭제
    '''#
    question = get_object_or_404(Question,pk=question_id)
    for i in question.answer_set.all():
        if question==i.question:
            i.delete()
            break
    return redirect('pybo:detail', question_id=question_id)


def answer_revise(request,question_id):
    '''
    pybo 답변 삭제
    '''
    question = get_object_or_404(Question,pk=question_id)
    for i in question.answer_set.all():
        if question==i.question:
            i.delete()
            break
    return redirect('pybo:detail', question_id=question_id)