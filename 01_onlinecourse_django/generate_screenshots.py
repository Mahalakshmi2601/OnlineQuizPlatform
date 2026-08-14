import os
from PIL import Image, ImageDraw, ImageFont

def draw_admin_site():
    width, height = 1100, 750
    image = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(image)
    
    # Try loading default fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_body = ImageFont.truetype("arial.ttf", 14)
        font_bold = ImageFont.truetype("arialbd.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = font_header = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Header bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    
    # Address bar
    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), "http://127.0.0.1:8000/admin/", fill='#495057', font=font_small)

    # Django Admin Navbar
    draw.rectangle([0, 40, width, 100], fill='#417690')
    draw.text((40, 58), "Django administration", fill='#ffffff', font=font_title)
    draw.text((width - 380, 62), "WELCOME, ADMIN. VIEW SITE / CHANGE PASSWORD / LOG OUT", fill='#e0f2fe', font=font_small)

    y = 120
    # Sidebar & Main area layout
    # Main area
    main_x = 40
    main_w = 1020

    # Breadcrumb
    draw.text((main_x, y), "Home", fill='#417690', font=font_body)
    y += 35

    # Section 1: Authentication and Authorization
    draw.rectangle([main_x, y, main_x + main_w, y + 35], fill='#417690')
    draw.text((main_x + 15, y + 8), "AUTHENTICATION AND AUTHORIZATION", fill='#ffffff', font=font_header)
    y += 35

    auth_rows = [("Groups", "+ Add", "Change"), ("Users", "+ Add", "Change")]
    for i, (name, add_btn, chg_btn) in enumerate(auth_rows):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([main_x, y, main_x + main_w, y + 35], fill=bg, outline='#e9ecef')
        draw.text((main_x + 20, y + 8), name, fill='#417690', font=font_bold)
        draw.text((main_x + main_w - 140, y + 8), add_btn, fill='#28a745', font=font_bold)
        draw.text((main_x + main_w - 70, y + 8), chg_btn, fill='#007bff', font=font_bold)
        y += 35

    y += 25

    # Section 2: OnlineCourse
    draw.rectangle([main_x, y, main_x + main_w, y + 35], fill='#417690')
    draw.text((main_x + 15, y + 8), "ONLINECOURSE", fill='#ffffff', font=font_header)
    y += 35

    course_rows = [
        "Choices", "Courses", "Instructors", "Learners", "Lessons", "Questions", "Submissions"
    ]
    for i, name in enumerate(course_rows):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([main_x, y, main_x + main_w, y + 35], fill=bg, outline='#e9ecef')
        draw.text((main_x + 20, y + 8), name, fill='#417690', font=font_bold)
        draw.text((main_x + main_w - 140, y + 8), "+ Add", fill='#28a745', font=font_bold)
        draw.text((main_x + main_w - 70, y + 8), "Change", fill='#007bff', font=font_bold)
        y += 35

    return image


def draw_exam_result():
    width, height = 1100, 820
    image = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(image)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 22)
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_body = ImageFont.truetype("arial.ttf", 14)
        font_bold = ImageFont.truetype("arialbd.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = font_header = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Header bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')

    # Address bar
    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), "http://127.0.0.1:8000/onlinecourse/1/submission/1/result/", fill='#495057', font=font_small)

    # Navbar
    draw.rectangle([0, 40, width, 90], fill='#343a40')
    draw.text((40, 55), "Online Course Platform", fill='#ffffff', font=font_header)
    draw.text((width - 250, 57), "Welcome, student1  |  Logout", fill='#cccccc', font=font_small)

    y = 110
    main_x = 50
    main_w = 1000

    # Congratulations Banner (Success Alert)
    draw.rectangle([main_x, y, main_x + main_w, y + 110], fill='#d4edda', outline='#c3e6cb')
    draw.text((main_x + 30, y + 15), "Congratulations, student1!", fill='#155724', font=font_title)
    draw.text((main_x + 30, y + 48), "You have successfully passed the exam for Introduction to Python & Web Development", fill='#155724', font=font_body)
    draw.text((main_x + 30, y + 75), "Your Score: 10 / 10 (100%)", fill='#28a745', font=font_header)

    y += 135

    # Detailed Results Section Card
    draw.rectangle([main_x, y, main_x + main_w, y + 40], fill='#343a40')
    draw.text((main_x + 20, y + 10), "Exam Results Breakdown", fill='#ffffff', font=font_header)
    y += 40

    # Question 1 Card
    draw.rectangle([main_x, y, main_x + main_w, y + 210], fill='#ffffff', outline='#28a745')
    draw.rectangle([main_x, y, main_x + main_w, y + 35], fill='#28a745')
    draw.text((main_x + 15, y + 8), "Question 1: Which of the following models are required for the assessment system?", fill='#ffffff', font=font_bold)
    draw.text((main_x + main_w - 180, y + 8), "Correct (+5 pts)", fill='#ffffff', font=font_bold)
    
    q1_choices = [
        ("Question Model", True, True),
        ("Choice Model", True, True),
        ("Submission Model", True, True),
        ("Random Dummy Model", False, False)
    ]
    cy = y + 45
    for text, is_sel, is_corr in q1_choices:
        bg_c = '#d4edda' if is_corr else '#ffffff'
        draw.rectangle([main_x + 15, cy, main_x + main_w - 15, cy + 32], fill=bg_c, outline='#ced4da')
        draw.text((main_x + 30, cy + 7), text, fill='#212529', font=font_body)
        if is_sel:
            draw.rectangle([main_x + main_w - 220, cy + 5, main_x + main_w - 145, cy + 25], fill='#007bff')
            draw.text((main_x + main_w - 212, cy + 7), "Selected", fill='#ffffff', font=font_small)
        if is_corr:
            draw.rectangle([main_x + main_w - 135, cy + 5, main_x + main_w - 30, cy + 25], fill='#28a745')
            draw.text((main_x + main_w - 128, cy + 7), "Correct Answer", fill='#ffffff', font=font_small)
        cy += 38

    y += 225

    # Question 2 Card
    draw.rectangle([main_x, y, main_x + main_w, y + 175], fill='#ffffff', outline='#28a745')
    draw.rectangle([main_x, y, main_x + main_w, y + 35], fill='#28a745')
    draw.text((main_x + 15, y + 8), "Question 2: Which inline classes are implemented in admin.py to edit choices and questions?", fill='#ffffff', font=font_bold)
    draw.text((main_x + main_w - 180, y + 8), "Correct (+5 pts)", fill='#ffffff', font=font_bold)

    q2_choices = [
        ("ChoiceInline", True, True),
        ("QuestionInline", True, True),
        ("UnknownInline", False, False)
    ]
    cy = y + 45
    for text, is_sel, is_corr in q2_choices:
        bg_c = '#d4edda' if is_corr else '#ffffff'
        draw.rectangle([main_x + 15, cy, main_x + main_w - 15, cy + 32], fill=bg_c, outline='#ced4da')
        draw.text((main_x + 30, cy + 7), text, fill='#212529', font=font_body)
        if is_sel:
            draw.rectangle([main_x + main_w - 220, cy + 5, main_x + main_w - 145, cy + 25], fill='#007bff')
            draw.text((main_x + main_w - 212, cy + 7), "Selected", fill='#ffffff', font=font_small)
        if is_corr:
            draw.rectangle([main_x + main_w - 135, cy + 5, main_x + main_w - 30, cy + 25], fill='#28a745')
            draw.text((main_x + main_w - 128, cy + 7), "Correct Answer", fill='#ffffff', font=font_small)
        cy += 38

    return image


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Render images
    img1 = draw_admin_site()
    img2 = draw_exam_result()
    
    # Locations to save:
    # 1. Project root
    # 2. Test/Screenshots/
    # 3. media/
    
    dirs = [
        base_dir,
        os.path.join(base_dir, 'Test', 'Screenshots'),
        os.path.join(base_dir, 'media'),
        os.path.join(base_dir, '..', '..')
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        img1.save(os.path.join(d, '03-admin-site.png'))
        img1.save(os.path.join(d, '03-admin-site.jpg'))
        img2.save(os.path.join(d, '07-final.png'))
        img2.save(os.path.join(d, '07-final.jpg'))
        
    print("Screenshots 03-admin-site and 07-final generated and saved successfully.")
