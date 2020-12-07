from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request) :
    # 조회 결과를 작성일시 역순으로 정렬
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    #render 함수 - 조회된 질문목록 데이터를 지정된 파일에 적용하여 HTML로 변환해 주는 함수
    #question_list.html - 템플릿 (장고에서 사용하는 태그들을 사용가능한 HTML 파일
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
