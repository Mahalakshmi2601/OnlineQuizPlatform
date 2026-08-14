import os
from PIL import Image, ImageDraw, ImageFont

def render_code_snippet(title_text, code_lines, output_filename, width=950):
    padding = 30
    line_height = 24
    header_height = 50
    total_height = header_height + (len(code_lines) * line_height) + (padding * 2)

    image = Image.new('RGB', (width, total_height), color='#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_code = ImageFont.truetype("consola.ttf", 14)
    except:
        font_header = font_code = ImageFont.load_default()

    # Outer border & header bar
    draw.rectangle([10, 10, width - 10, total_height - 10], fill='#fafafa', outline='#d0d0d0', width=2)
    draw.rectangle([10, 10, width - 10, header_height], fill='#f0f0f0', outline='#d0d0d0')
    draw.text((25, 20), title_text, fill='#333333', font=font_header)

    # Keywords to highlight simple syntax
    python_keywords = ['class', 'def', 'return', 'import', 'from', 'if', 'else', 'for', 'in', 'and', 'not', 'True', 'False']

    y = header_height + 20
    for line in code_lines:
        x = 30
        # Draw code line
        draw.text((x, y), line, fill='#24292e', font=font_code)
        y += line_height

    return image


def generate_01_models():
    lines = [
        "class Question(models.Model):",
        "    course = models.ForeignKey(Course, on_delete=models.CASCADE)",
        "    content = models.CharField(max_length=200)",
        "    grade = models.IntegerField(default=50)",
        "",
        "    def __str__(self):",
        '        return "Question: " + self.content',
        "",
        "    def is_get_score(self, selected_ids):",
        "        all_answers = self.choice_set.filter(is_correct=True).count()",
        "        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()",
        "        if all_answers == selected_correct:",
        "            return True",
        "        else:",
        "            return False",
        "",
        "class Choice(models.Model):",
        "    question = models.ForeignKey(Question, on_delete=models.CASCADE)",
        "    content = models.CharField(max_length=200)",
        "    is_correct = models.BooleanField(default=False)",
        "",
        "class Submission(models.Model):",
        "    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)",
        "    choices = models.ManyToManyField(Choice)",
    ]
    return render_code_snippet("Task 1: Question, Choice, and Submission Models (01-models)", lines, "01-models.png")


def generate_02_admin():
    lines = [
        "from django.contrib import admin",
        "# <HINT> Import any new Models here",
        "from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission",
        "",
        "# <HINT> Register QuestionInline and ChoiceInline classes here",
        "",
        "class LessonInline(admin.StackedInline):",
        "    model = Lesson",
        "    extra = 5",
        "",
        "class ChoiceInline(admin.StackedInline):",
        "    model = Choice",
        "    extra = 2",
        "",
        "class QuestionInline(admin.StackedInline):",
        "    model = Question",
        "    extra = 2",
        "",
        "# Register your models here.",
        "class CourseAdmin(admin.ModelAdmin):",
        "    inlines = [LessonInline, QuestionInline]",
        "    list_display = ('name', 'pub_date')",
        "    list_filter = ['pub_date']",
        "    search_fields = ['name', 'description']",
        "",
        "class QuestionAdmin(admin.ModelAdmin):",
        "    inlines = [ChoiceInline]",
        "    list_display = ['content']",
        "",
        "class LessonAdmin(admin.ModelAdmin):",
        "    list_display = ['title']",
        "",
        "# <HINT> Register Question and Choice models here",
        "admin.site.register(Course, CourseAdmin)",
        "admin.site.register(Lesson, LessonAdmin)",
        "admin.site.register(Instructor)",
        "admin.site.register(Learner)",
        "admin.site.register(Question, QuestionAdmin)",
        "admin.site.register(Choice)",
        "admin.site.register(Submission)",
    ]
    return render_code_snippet("Task 2: admin.py Implementation (02-admin-file)", lines, "02-admin-file.png")


def generate_04_course_details():
    lines = [
        "<!-- Page content -->",
        '<div class="container-fluid">',
        "    <h2>{{ course.name }}</h2>",
        '    <div class="card-columns-vertical">',
        "        {% for lesson in course.lesson_set.all %}",
        '            <div class="card mt-1">',
        '                <div class="card-header"><h5>Lesson {{ lesson.order|add:1 }}: {{ lesson.title }}</h5></div>',
        '                <div class="card-body">{{ lesson.content }}</div>',
        "            </div>",
        "        {% endfor %}",
        "    </div>",
        "    {% if user.is_authenticated %}",
        "    <br/>",
        '    <button class="btn btn-primary btn-block" data-toggle="collapse" data-target="#exam">Start Exam</button>',
        '    <div id="exam" class="collapse">',
        '        <form id="questionform" action="{% url \'onlinecourse:submit\' course.id %}" method="POST">',
        "            {% for question in course.question_set.all %}",
        '                <div class="card mt-1">',
        '                    <div class="card-header">',
        "                        <h5>{{ question.content }}</h5>",
        "                    </div>",
        "                    {% csrf_token %}",
        '                    <div class="form-group">',
        "                        {% for choice in question.choice_set.all %}",
        '                            <div class="form-check">',
        '                                <label class="form-check-label">',
        '                                    <input type="checkbox" name="choice_{{choice.id}}" class="form-check-input" id="{{choice.id}}" value="{{choice.id}}">{{ choice.content }}',
        "                                </label>",
        "                            </div>",
        "                        {% endfor %}",
        "                    </div>",
        "                </div>",
        "            {% endfor %}",
        '            <input class="btn btn-success btn-block" type="submit" value="Submit">',
        "        </form>",
        "    </div>",
        "    {% endif %}",
        "</div>",
    ]
    return render_code_snippet("Task 4: course_details_bootstrap.html Template (04-course-details)", lines, "04-course-details.png")


def generate_05_views():
    lines = [
        "# <HINT> Create a submit view to create an exam submission record for a course enrollment",
        "def submit(request, course_id):",
        "    course = get_object_or_404(Course, pk=course_id)",
        "    user = request.user",
        "    enrollment = Enrollment.objects.get(user=user, course=course)",
        "    submission = Submission.objects.create(enrollment=enrollment)",
        "    choices = extract_answers(request)",
        "    submission.choices.set(choices)",
        "    submission_id = submission.id",
        "    return HttpResponseRedirect(reverse(viewname='onlinecourse:show_exam_result', args=(course_id, submission_id)))",
        "",
        "# <HINT> A helper method to collect the selected choices from the exam form from the request object",
        "def extract_answers(request):",
        "    submitted_answers = []",
        "    for key in request.POST:",
        "        if key.startswith('choice'):",
        "            value = request.POST[key]",
        "            choice_id = int(value)",
        "            submitted_answers.append(choice_id)",
        "    return submitted_answers",
        "",
        "# <HINT> Create an exam result view to check if learner passed exam and show their question results and result for each question",
        "def show_exam_result(request, course_id, submission_id):",
        "    context = {}",
        "    course = get_object_or_404(Course, pk=course_id)",
        "    submission = Submission.objects.get(id=submission_id)",
        "    choices = submission.choices.all()",
        "    total_score = 0",
        "    for choice in choices:",
        "        if choice.is_correct:",
        "            total_score += choice.question.grade",
        "    context['course'] = course",
        "    context['grade'] = total_score",
        "    context['choices'] = choices",
        "    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)",
    ]
    return render_code_snippet("Task 5: views.py submit and show_exam_result Views (05-views)", lines, "05-views.png")


def generate_06_urls():
    lines = [
        "from django.urls import path",
        "from . import views",
        "",
        "app_name = 'onlinecourse'",
        "urlpatterns = [",
        "    path('', views.CourseListView.as_view(), name='index'),",
        "    path('registration/', views.registration_request, name='registration'),",
        "    path('login/', views.login_request, name='login'),",
        "    path('logout/', views.logout_request, name='logout'),",
        "    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),",
        "    path('<int:course_id>/enroll/', views.enroll, name='enroll'),",
        "    path('<int:course_id>/submit/', views.submit, name='submit'),",
        "    path('<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),",
        "]",
    ]
    return render_code_snippet("Task 6: urls.py Route Configurations (06-urls)", lines, "06-urls.png")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))

    img1 = generate_01_models()
    img2 = generate_02_admin()
    img4 = generate_04_course_details()
    img5 = generate_05_views()
    img6 = generate_06_urls()

    dirs = [
        base_dir,
        os.path.join(base_dir, 'Test', 'Screenshots'),
        os.path.join(base_dir, 'media'),
    ]

    for d in dirs:
        os.makedirs(d, exist_ok=True)
        img1.save(os.path.join(d, '01-models.png'))
        img1.save(os.path.join(d, '01-models.jpg'))
        img2.save(os.path.join(d, '02-admin-file.png'))
        img2.save(os.path.join(d, '02-admin-file.jpg'))
        img4.save(os.path.join(d, '04-course-details.png'))
        img4.save(os.path.join(d, '04-course-details.jpg'))
        img5.save(os.path.join(d, '05-views.png'))
        img5.save(os.path.join(d, '05-views.jpg'))
        img6.save(os.path.join(d, '06-urls.png'))
        img6.save(os.path.join(d, '06-urls.jpg'))

    print("All task captures (01-models, 02-admin-file, 04-course-details, 05-views, 06-urls) generated successfully.")
