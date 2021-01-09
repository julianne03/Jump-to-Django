from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from ..models import Question

def index(request) :
    #입력 파라미터
    page = request.GET.get('page','1') # 페이지
    # 조회 결과를 작성일시 역순으로 정렬
    question_list = Question.objects.order_by('-create_date')
    #페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    #render 함수 - 조회된 질문목록 데이터를 지정된 파일에 적용하여 HTML로 변환해 주는 함수
    #question_list.html - 템플릿 (장고에서 사용하는 태그들을 사용가능한 HTML 파일
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
