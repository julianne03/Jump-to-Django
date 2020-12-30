from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

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

def answer_create(request, question_id) :
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST" :
        form = AnswerForm(request.POST)
        if form.is_valid() :
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else :
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request) :
    """
    pybo 질문등록
    """
    if request.method == 'POST' :
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)
