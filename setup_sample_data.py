import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineQuizPlatform.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Course, Lesson, Question, Choice, Enrollment, Instructor, Learner

# Create superuser admin
if not User.objects.filter(username='admin').exists():
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser admin created")
else:
    admin_user = User.objects.get(username='admin')

# Create instructor profile
instructor, _ = Instructor.objects.get_or_create(user=admin_user, full_time=True, total_learners=100)

# Create course
course, _ = Course.objects.get_or_create(
    name='Introduction to Python & Web Development',
    defaults={
        'description': 'Learn Python fundamentals, Django web framework, models, views, templates, and quiz platforms.',
        'pub_date': '2026-08-14'
    }
)
course.instructors.add(instructor)

# Create lessons
l1, _ = Lesson.objects.get_or_create(course=course, order=1, title='Introduction to Python', content='Python is an interpreted, high-level, general-purpose programming language.')
l2, _ = Lesson.objects.get_or_create(course=course, order=2, title='Django Models & Admin', content='Django models define the data structure and database tables for the application.')
l3, _ = Lesson.objects.get_or_create(course=course, order=3, title='Views, Templates, and Forms', content='Django views handle business logic and render response templates using Bootstrap.')

# Create questions and choices
q1, _ = Question.objects.get_or_create(
    course=course,
    question_text='Which of the following models are required for the assessment system?',
    grade=5
)
c1_1, _ = Choice.objects.get_or_create(question=q1, choice_text='Question Model', is_correct=True)
c1_2, _ = Choice.objects.get_or_create(question=q1, choice_text='Choice Model', is_correct=True)
c1_3, _ = Choice.objects.get_or_create(question=q1, choice_text='Submission Model', is_correct=True)
c1_4, _ = Choice.objects.get_or_create(question=q1, choice_text='Random Dummy Model', is_correct=False)

q2, _ = Question.objects.get_or_create(
    course=course,
    question_text='Which inline classes are implemented in admin.py to edit choices and questions?',
    grade=5
)
c2_1, _ = Choice.objects.get_or_create(question=q2, choice_text='ChoiceInline', is_correct=True)
c2_2, _ = Choice.objects.get_or_create(question=q2, choice_text='QuestionInline', is_correct=True)
c2_3, _ = Choice.objects.get_or_create(question=q2, choice_text='UnknownInline', is_correct=False)

# Enroll admin user
enrollment, _ = Enrollment.objects.get_or_create(user=admin_user, course=course)

print("Sample data populated successfully.")
