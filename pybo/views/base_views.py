from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from ..models import Question

def index(request) :
    #입력 파라미터
    page = request.GET.get('page','1') # 페이지
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')

    #정렬
    if so == 'recommend' :
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular' :
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else :
        question_list = Question.objects.order_by('-create_date')

    if kw :
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  #제목검색
            Q(content__icontains=kw) |  #내용검색
            Q(author__username__icontains=kw) |  #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  #답변 글쓴이 검색
        ).distinct()

    #페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}
    #render 함수 - 조회된 질문목록 데이터를 지정된 파일에 적용하여 HTML로 변환해 주는 함수
    #question_list.html - 템플릿 (장고에서 사용하는 태그들을 사용가능한 HTML 파일
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
