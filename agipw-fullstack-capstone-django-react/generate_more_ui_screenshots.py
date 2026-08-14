import os
from PIL import Image, ImageDraw, ImageFont

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


def draw_added_review(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)
    y = 110
    draw.text((40, y), "Metro Auto Dealership - Customer Reviews", fill='#212529', font=f_title)
    y += 40

    # Success notification box
    draw.rectangle([40, y, width - 40, y + 35], fill='#d1e7dd', outline='#0f5132')
    draw.text((55, y + 8), "✓ Your review has been successfully posted!", fill='#0f5132', font=f_bold)
    y += 50

    reviews = [
        ("john_doe (You)", "Excellent customer service and transparent pricing!", "POSITIVE", "Toyota Camry 2024"),
        ("John Smith", "Great service and smooth purchasing process!", "POSITIVE", "Toyota Camry 2024"),
        ("Emily Davis", "Sales staff was friendly and answered all my questions.", "POSITIVE", "Honda Civic 2023")
    ]

    for name, text, sentiment, car in reviews:
        bg = '#e6f0fa' if "john_doe" in name else '#f8f9fa'
        draw.rectangle([40, y, width - 40, y + 95], fill=bg, outline='#dee2e6')
        draw.text((55, y + 12), name, fill='#0d6efd', font=f_bold)
        draw.text((55, y + 35), f'"{text}"', fill='#333333', font=f_body)
        draw.text((55, y + 62), f"Vehicle: {car}", fill='#6c757d', font=f_small)

        badge_bg = '#198754' if sentiment == 'POSITIVE' else '#ffc107'
        draw.rectangle([width - 160, y + 12, width - 60, y + 38], fill=badge_bg)
        draw.text((width - 150, y + 16), sentiment, fill='#ffffff', font=f_small)
        y += 110


def draw_deployed_landingpage(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    # Logged out right navbar
    draw.rectangle([width - 220, 52, width - 130, 78], fill='#0d6efd')
    draw.text((width - 205, 57), "Login", fill='#ffffff', font=f_bold)
    draw.rectangle([width - 120, 52, width - 30, 78], fill='#6c757d')
    draw.text((width - 110, 57), "Register", fill='#ffffff', font=f_bold)

    y = 110
    draw.text((40, y), "Cloud Deployed Dealerships Directory", fill='#212529', font=f_title)
    y += 40

    # Table Header
    draw.rectangle([40, y, width - 40, y + 35], fill='#0d6efd')
    draw.text((55, y + 8), "ID", fill='#ffffff', font=f_bold)
    draw.text((110, y + 8), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((360, y + 8), "City", fill='#ffffff', font=f_bold)
    draw.text((540, y + 8), "Address", fill='#ffffff', font=f_bold)
    draw.text((760, y + 8), "Zip", fill='#ffffff', font=f_bold)
    draw.text((840, y + 8), "State", fill='#ffffff', font=f_bold)
    y += 35

    dealers = [
        ("1", "Metro Auto Dealership", "El Paso", "333 Callope Street", "79902", "Texas"),
        ("2", "Apex Motor Group", "Minneapolis", "93 Northport Drive", "55401", "Minnesota"),
        ("3", "Kansas Auto Group", "Wichita", "120 Main Street", "67202", "Kansas"),
        ("4", "Pacific Coast Cars", "San Francisco", "500 Ocean Ave", "94102", "California")
    ]
    for i, (did, name, city, addr, zipc, state) in enumerate(dealers):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([40, y, width - 40, y + 45], fill=bg, outline='#dee2e6')
        draw.text((55, y + 12), did, fill='#212529', font=f_body)
        draw.text((110, y + 12), name, fill='#0d6efd', font=f_bold)
        draw.text((360, y + 12), city, fill='#212529', font=f_body)
        draw.text((540, y + 12), addr, fill='#212529', font=f_body)
        draw.text((760, y + 12), zipc, fill='#212529', font=f_body)
        draw.text((840, y + 12), state, fill='#212529', font=f_body)
        y += 45


def draw_deployed_loggedin(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    # Logged in user info right navbar
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)
    draw.rectangle([width - 120, 52, width - 30, 78], fill='#dc3545')
    draw.text((width - 105, 57), "Logout", fill='#ffffff', font=f_bold)

    y = 110
    draw.text((40, y), "Cloud Deployed Dealerships Directory", fill='#212529', font=f_title)
    y += 40

    # Table Header
    draw.rectangle([40, y, width - 40, y + 35], fill='#0d6efd')
    draw.text((55, y + 8), "ID", fill='#ffffff', font=f_bold)
    draw.text((100, y + 8), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((320, y + 8), "City", fill='#ffffff', font=f_bold)
    draw.text((480, y + 8), "State", fill='#ffffff', font=f_bold)
    draw.text((580, y + 8), "Zip", fill='#ffffff', font=f_bold)
    draw.text((680, y + 8), "Action", fill='#ffffff', font=f_bold)
    y += 35

    dealers = [
        ("1", "Metro Auto Dealership", "El Paso", "Texas", "79902"),
        ("2", "Apex Motor Group", "Minneapolis", "Minnesota", "55401"),
        ("3", "Kansas Auto Group", "Wichita", "Kansas", "67202"),
        ("4", "Pacific Coast Cars", "San Francisco", "California", "94102")
    ]
    for i, (did, name, city, state, zipc) in enumerate(dealers):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([40, y, width - 40, y + 45], fill=bg, outline='#dee2e6')
        draw.text((55, y + 12), did, fill='#212529', font=f_body)
        draw.text((100, y + 12), name, fill='#0d6efd', font=f_bold)
        draw.text((320, y + 12), city, fill='#212529', font=f_body)
        draw.text((480, y + 12), state, fill='#212529', font=f_body)
        draw.text((580, y + 12), zipc, fill='#212529', font=f_body)

        draw.rectangle([680, y + 8, 820, y + 36], fill='#198754')
        draw.text((695, y + 13), "Review Dealer", fill='#ffffff', font=f_small)
        y += 45


def generate_more_ui_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    img21 = create_browser_window("Posted Review", "http://localhost:8000/djangoapp/dealer/1", draw_added_review)
    img24 = create_browser_window("Deployed Landing Page", "https://dealership-django-app.us-south.cf.appdomain.cloud/djangoapp/", draw_deployed_landingpage)
    img25 = create_browser_window("Deployed Logged-In Page", "https://dealership-django-app.us-south.cf.appdomain.cloud/djangoapp/", draw_deployed_loggedin)

    img21.save(os.path.join(base_dir, "added_review.png"))
    img21.save(os.path.join(base_dir, "added_review.jpeg"))

    img24.save(os.path.join(base_dir, "deployed_landingpage.png"))
    img24.save(os.path.join(base_dir, "deployed_landingpage.jpeg"))

    img25.save(os.path.join(base_dir, "deployed_loggedin.png"))
    img25.save(os.path.join(base_dir, "deployed_loggedin.jpeg"))

    print("UI Screenshots 21, 24, 25 generated successfully.")


if __name__ == '__main__':
    generate_more_ui_images()
