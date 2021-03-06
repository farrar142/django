from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from pybo.models import Question


def main_index(request):
    return render(request, 'index.html')


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # page
    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여줌
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # id값으로 필터해서 보여줌
    context = {'question': question}

    return render(request, 'pybo/question_detail.html', context)
