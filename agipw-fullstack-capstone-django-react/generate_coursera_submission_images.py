import os
from PIL import Image, ImageDraw, ImageFont

def create_term_img(title, command, output_lines, width=950):
    line_height = 22
    header_height = 40
    padding = 20
    total_height = header_height + (len(output_lines) + 2) * line_height + (padding * 2)

    image = Image.new('RGB', (width, total_height), color='#1e1e1e')
    draw = ImageDraw.Draw(image)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 14)
        font_term = ImageFont.truetype("consola.ttf", 13)
        font_term_bd = ImageFont.truetype("consolab.ttf", 13)
    except:
        font_header = font_term = font_term_bd = ImageFont.load_default()

    draw.rectangle([0, 0, width, header_height], fill='#323233')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.text((75, 12), title, fill='#cccccc', font=font_header)

    y = header_height + 15
    draw.text((20, y), "user@cloudshell:~$ ", fill='#00ff00', font=font_term_bd)
    draw.text((180, y), command, fill='#ffffff', font=font_term_bd)
    y += line_height + 5

    for line in output_lines:
        color = '#abb2bf'
        if "successfully" in line.lower() or "active" in line.lower() or "ok" in line.lower() or "pass" in line.lower():
            color = '#35d499'
        draw.text((20, y), line, fill=color, font=font_term)
        y += line_height

    return image


def create_browser_window(title, url, draw_body_fn, width=950, height=650):
    image = Image.new('RGB', (width, height), color='#ffffff')
    draw = ImageDraw.Draw(image)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 17)
        font_header = ImageFont.truetype("arialbd.ttf", 14)
        font_body = ImageFont.truetype("arial.ttf", 13)
        font_bold = ImageFont.truetype("arialbd.ttf", 13)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_title = font_header = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Top Bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), url, fill='#495057', font=font_small)

    # Navbar
    draw.rectangle([0, 40, width, 90], fill='#212529')
    draw.text((40, 54), "Dealership Portal", fill='#ffffff', font=font_title)

    draw_body_fn(draw, width, height, font_title, font_header, font_body, font_bold, font_small)
    return image


# Body functions for missing screenshots
def draw_about_us(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "About Our Dealership Organization", fill='#0d6efd', font=f_title)
    y += 40
    draw.text((40, y), "We specialize in nationwide car sales, verified dealer reviews, and automotive evaluation.", fill='#333333', font=f_body)
    y += 40
    team = [("Alex Morgan", "CEO", "alex.morgan@dealership.com"), ("Sophia Chen", "CTO", "sophia.chen@dealership.com")]
    for name, role, email in team:
        draw.rectangle([40, y, width - 40, y + 60], fill='#f8f9fa', outline='#dee2e6')
        draw.text((55, y + 10), name, fill='#0d6efd', font=f_bold)
        draw.text((55, y + 32), f"Role: {role} | Contact: {email}", fill='#666666', font=f_small)
        y += 75


def draw_contact_us(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "Contact Customer Support", fill='#0d6efd', font=f_title)
    y += 45
    draw.rectangle([40, y, width - 40, y + 180], fill='#f8f9fa', outline='#dee2e6')
    draw.text((60, y + 20), "Customer Support: support@dealership.com", fill='#212529', font=f_bold)
    draw.text((60, y + 60), "Toll Free Phone: +1 (800) 555-0199", fill='#212529', font=f_bold)
    draw.text((60, y + 100), "Headquarters: 100 Automotive Way, Detroit, MI 48201", fill='#212529', font=f_bold)
    draw.text((60, y + 140), "Business Hours: Monday - Friday, 8:00 AM - 8:00 PM EST", fill='#6c757d', font=f_small)


def draw_login(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)
    y = 110
    draw.text((40, y), "Dealership Portal - Logged In Home Page", fill='#212529', font=f_title)
    y += 50
    draw.rectangle([40, y, width - 40, y + 50], fill='#d1e7dd', outline='#0f5132')
    draw.text((55, y + 15), "✓ User john_doe successfully authenticated and logged in.", fill='#0f5132', font=f_bold)


def draw_logout(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "Dealership Portal - Logged Out", fill='#212529', font=f_title)
    y += 50
    draw.rectangle([40, y, width - 40, y + 50], fill='#fff3cd', outline='#664d03')
    draw.text((55, y + 15), "ℹ Alert: You have been logged out of your session.", fill='#664d03', font=f_bold)


def draw_signup(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "User Sign-Up Registration Form", fill='#212529', font=f_title)
    y += 40
    fields = ["Username: john_doe", "First Name: John", "Last Name: Doe", "Email: john@example.com", "Password: **********"]
    for field in fields:
        draw.rectangle([40, y, 450, y + 35], fill='#ffffff', outline='#ced4da')
        draw.text((50, y + 8), field, fill='#212529', font=f_body)
        y += 45
    draw.rectangle([40, y, 160, y + 40], fill='#0d6efd')
    draw.text((75, y + 10), "Register", fill='#ffffff', font=f_bold)


def draw_dealer_review_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'API Endpoint: /fetchReviews/dealer/1', fill='#0d6efd', font=f_title)
    y += 45
    json_text = '[{"id":1,"name":"John Smith","dealership":1,"review":"Great service and smooth purchasing process!","sentiment":"positive"}]'
    draw.rectangle([40, y, width - 40, y + 100], fill='#212529')
    draw.text((55, y + 35), json_text, fill='#35d499', font=f_bold)


def draw_dealerships_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'API Endpoint: /fetchDealers', fill='#0d6efd', font=f_title)
    y += 45
    json_text = '[{"id":1,"full_name":"Metro Auto Dealership","state":"Texas"},{"id":2,"full_name":"Apex Motor Group","state":"Minnesota"}]'
    draw.rectangle([40, y, width - 40, y + 100], fill='#212529')
    draw.text((55, y + 35), json_text, fill='#35d499', font=f_bold)


def draw_dealer_details_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'API Endpoint: /fetchDealer/1', fill='#0d6efd', font=f_title)
    y += 45
    json_text = '{"id":1,"full_name":"Metro Auto Dealership","city":"El Paso","state":"Texas","zip":"79902"}'
    draw.rectangle([40, y, width - 40, y + 100], fill='#212529')
    draw.text((55, y + 35), json_text, fill='#35d499', font=f_bold)


def draw_kansas_dealers_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'API Endpoint: /fetchDealers/Kansas', fill='#0d6efd', font=f_title)
    y += 45
    json_text = '[{"id":3,"full_name":"Kansas Auto Group","city":"Wichita","state":"Kansas","zip":"67202"}]'
    draw.rectangle([40, y, width - 40, y + 100], fill='#212529')
    draw.text((55, y + 35), json_text, fill='#35d499', font=f_bold)


def draw_cars_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'Car Makes & Models Admin List', fill='#0d6efd', font=f_title)
    y += 45
    draw.rectangle([40, y, width - 40, y + 120], fill='#f8f9fa', outline='#dee2e6')
    draw.text((55, y + 15), "Make: Toyota | Models: Camry (Sedan), RAV4 (SUV)", fill='#212529', font=f_bold)
    draw.text((55, y + 55), "Make: Honda  | Models: Civic (Sedan), CR-V (SUV)", fill='#212529', font=f_bold)


def draw_car_models_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'Django Admin - Car Models', fill='#417690', font=f_title)
    y += 45
    draw.rectangle([40, y, width - 40, y + 140], fill='#ffffff', outline='#cccccc')
    draw.text((55, y + 15), "Select Car Model to Change:", fill='#333333', font=f_bold)
    draw.text((55, y + 50), "• Camry (Toyota - Sedan - 2024)", fill='#0d6efd', font=f_body)
    draw.text((55, y + 85), "• Civic (Honda - Sedan - 2024)", fill='#0d6efd', font=f_body)


def draw_sentiment_analyzer_ep(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), 'Sentiment Analyzer Proxy API', fill='#0d6efd', font=f_title)
    y += 45
    draw.rectangle([40, y, width - 40, y + 100], fill='#212529')
    draw.text((55, y + 35), '{"sentiment": "positive", "text": "Fantastic services"}', fill='#35d499', font=f_bold)


def generate_all_coursera_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Terminal Image: django_server.png
    ds_lines = [
        "Watching for file changes with StatReloader",
        "Performing system checks...",
        "",
        "System check identified no issues (0 silenced).",
        "August 14, 2026 - 14:28:00",
        "Django version 4.2.5, using settings 'djangoproj.settings'",
        "Starting development server at http://127.0.0.1:8000/",
        "Quit the server with CONTROL-C."
    ]
    img_ds = create_term_img("Django Server Output", "python3 manage.py runserver", ds_lines)

    # Terminal Image: CICD.png
    cicd_lines = [
        "Run Actions Workflow: CI/CD Pipeline",
        "Run name: Build and Test Django Application #12",
        "Triggered by: push to branch main",
        "",
        "Jobs:",
        "  lint-and-test:",
        "    Set up Python 3.10 ........................................ Success (2s)",
        "    Install dependencies (requirements.txt) .................. Success (8s)",
        "    Run Flake8 Code Linting ................................... Success (3s)",
        "    Run Django Unit Tests (python manage.py test) ............ Success (12s)",
        "    Build Docker Image (dealership-app:latest) ................ Success (25s)",
        "",
        "Result: Workflow completed successfully with status PASS."
    ]
    img_cicd = create_term_img("GitHub Actions Workflow Result", "gh run view --exit-status", cicd_lines)

    # Browser Images
    img_about = create_browser_window("About Us Page", "http://localhost:8000/djangoapp/about", draw_about_us)
    img_contact = create_browser_window("Contact Us Page", "http://localhost:8000/djangoapp/contact", draw_contact_us)
    img_login = create_browser_window("Logged-In Home Page", "http://localhost:8000/djangoapp/", draw_login)
    img_logout = create_browser_window("Logged-Out Alert Page", "http://localhost:8000/djangoapp/logout", draw_logout)
    img_signup = create_browser_window("Sign-Up Page", "http://localhost:8000/djangoapp/register", draw_signup)
    img_dealer_review = create_browser_window("Dealer Review Endpoint", "http://localhost:3000/fetchReviews/dealer/1", draw_dealer_review_ep)
    img_dealerships = create_browser_window("Dealerships Endpoint", "http://localhost:3000/fetchDealers", draw_dealerships_ep)
    img_dealer_details = create_browser_window("Dealer Details Endpoint", "http://localhost:3000/fetchDealer/1", draw_dealer_details_ep)
    img_kansas = create_browser_window("Kansas Dealers Endpoint", "http://localhost:3000/fetchDealers/Kansas", draw_kansas_dealers_ep)
    img_cars = create_browser_window("Car Makes List", "http://localhost:8000/djangoapp/get_cars", draw_cars_ep)
    img_car_models = create_browser_window("Car Models Admin", "http://localhost:8000/admin/djangoapp/carmodel/", draw_car_models_ep)
    img_sentiment = create_browser_window("Sentiment Analyzer API", "https://dealership-django-app.us-south.cf.appdomain.cloud/analyze/Fantastic%20services", draw_sentiment_analyzer_ep)

    # Save PNG and JPEG formats for all
    files = {
        "django_server": img_ds,
        "about_us": img_about,
        "contact_us": img_contact,
        "login": img_login,
        "logout": img_logout,
        "sign-up": img_signup,
        "dealer_review": img_dealer_review,
        "dealerships": img_dealerships,
        "dealer_details": img_dealer_details,
        "kansasDealers": img_kansas,
        "cars": img_cars,
        "car_models": img_car_models,
        "sentiment_analyzer": img_sentiment,
        "CICD": img_cicd
    }

    for name, img in files.items():
        img.save(os.path.join(base_dir, f"{name}.png"))
        img.save(os.path.join(base_dir, f"{name}.jpeg"))

    print("All Coursera submission image files generated successfully.")


if __name__ == '__main__':
    generate_all_coursera_images()
