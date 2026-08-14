from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, Lesson, Enrollment, Question, Choice, Submission


class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_details_bootstrap.html'


def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        user = request.user
        if user.is_authenticated:
            enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)
            return redirect('onlinecourse:course_details', pk=course.id)
    return redirect('onlinecourse:index')


# <HINT> Create a submit view to create an exam submission record for a course enrollment
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get(user=user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    choices = extract_answers(request)
    submission.choices.set(choices)
    submission_id = submission.id
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course_id, submission_id)))


# <HINT> A helper method to collect the selected choices from the exam form from the request object
def extract_answers(request):
    submitted_answers = []
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers


# <HINT> Create an exam result view to check if learner passed exam and show their question results and result for each question
def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(id=submission_id)
    choices = submission.choices.all()
    selected_ids = [choice.id for choice in choices]
    
    total_score = 0
    total_possible = 0
    questions = course.question_set.all()
    question_results = []
    
    for question in questions:
        total_possible += question.grade
        is_correct = question.is_get_score(selected_ids)
        if is_correct:
            total_score += question.grade
        question_results.append({'question': question, 'is_correct': is_correct})
        
    percentage = (total_score / total_possible * 100) if total_possible > 0 else 0
    passed = percentage >= 80

    context['course'] = course
    context['submission'] = submission
    context['selected_ids'] = selected_ids
    context['grade'] = total_score
    context['total_possible'] = total_possible
    context['percentage'] = percentage
    context['passed'] = passed
    context['question_results'] = question_results
    context['choices'] = choices

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)


def registration_request(request):
    return redirect('onlinecourse:index')


def login_request(request):
    return redirect('onlinecourse:index')


def logout_request(request):
    logout(request)
    return redirect('onlinecourse:index')
