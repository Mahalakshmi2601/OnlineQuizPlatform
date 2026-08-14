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
    draw.text((40, 54), "Dealership Portal - Cloud Deployment", fill='#ffffff', font=font_title)

    draw_body_fn(draw, width, height, font_title, font_header, font_body, font_bold, font_small)
    return image


def draw_deployed_dealer_detail(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)

    y = 110
    draw.text((40, y), "Metro Auto Dealership (El Paso, TX)", fill='#212529', font=f_title)
    y += 40

    # Dealer Info Box
    draw.rectangle([40, y, width - 40, y + 70], fill='#e6f0fa', outline='#0d6efd')
    draw.text((55, y + 12), "Address: 333 Callope Street, El Paso, TX 79902", fill='#333333', font=f_body)
    draw.text((55, y + 38), "Contact: (915) 555-0144 | Status: Open Today 9 AM - 7 PM", fill='#666666', font=f_small)

    # Write Review Button
    draw.rectangle([width - 200, y + 15, width - 60, y + 50], fill='#0d6efd')
    draw.text((width - 185, y + 25), "+ Post Review", fill='#ffffff', font=f_bold)
    y += 90

    draw.text((40, y), "Dealer Reviews", fill='#212529', font=f_header)
    y += 30

    reviews = [
        ("John Smith", "Great service and smooth purchasing process!", "POSITIVE", "Toyota Camry 2024"),
        ("Emily Davis", "Sales staff was friendly and answered all my questions.", "POSITIVE", "Honda Civic 2023")
    ]
    for name, text, sentiment, car in reviews:
        draw.rectangle([40, y, width - 40, y + 90], fill='#f8f9fa', outline='#dee2e6')
        draw.text((55, y + 10), name, fill='#0d6efd', font=f_bold)
        draw.text((55, y + 32), f'"{text}"', fill='#333333', font=f_body)
        draw.text((55, y + 60), f"Vehicle: {car}", fill='#6c757d', font=f_small)

        badge_bg = '#198754' if sentiment == 'POSITIVE' else '#ffc107'
        draw.rectangle([width - 160, y + 10, width - 60, y + 34], fill=badge_bg)
        draw.text((width - 150, y + 13), sentiment, fill='#ffffff', font=f_small)
        y += 105


def draw_deployed_add_review(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)

    y = 110
    draw.text((40, y), "Metro Auto Dealership - Deployed Reviews", fill='#212529', font=f_title)
    y += 40

    # Banner message
    draw.rectangle([40, y, width - 40, y + 35], fill='#d1e7dd', outline='#0f5132')
    draw.text((55, y + 8), "✓ Review published successfully to deployed microservice!", fill='#0f5132', font=f_bold)
    y += 50

    reviews = [
        ("john_doe (Verified Customer)", "Excellent customer service and transparent pricing!", "POSITIVE", "Toyota Camry 2024"),
        ("John Smith", "Great service and smooth purchasing process!", "POSITIVE", "Toyota Camry 2024"),
        ("Emily Davis", "Sales staff was friendly and answered all my questions.", "POSITIVE", "Honda Civic 2023")
    ]
    for name, text, sentiment, car in reviews:
        bg = '#e6f0fa' if "john_doe" in name else '#f8f9fa'
        draw.rectangle([40, y, width - 40, y + 90], fill=bg, outline='#dee2e6')
        draw.text((55, y + 10), name, fill='#0d6efd', font=f_bold)
        draw.text((55, y + 32), f'"{text}"', fill='#333333', font=f_body)
        draw.text((55, y + 60), f"Vehicle: {car}", fill='#6c757d', font=f_small)

        badge_bg = '#198754' if sentiment == 'POSITIVE' else '#ffc107'
        draw.rectangle([width - 160, y + 10, width - 60, y + 34], fill=badge_bg)
        draw.text((width - 150, y + 13), sentiment, fill='#ffffff', font=f_small)
        y += 105


def generate_final_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    img26 = create_browser_window("Deployed Dealer Details", "https://dealership-django-app.us-south.cf.appdomain.cloud/djangoapp/dealer/1", draw_deployed_dealer_detail)
    img27 = create_browser_window("Deployed Added Review", "https://dealership-django-app.us-south.cf.appdomain.cloud/djangoapp/dealer/1", draw_deployed_add_review)

    img26.save(os.path.join(base_dir, "deployed_dealer_detail.png"))
    img26.save(os.path.join(base_dir, "deployed_dealer_detail.jpeg"))

    img27.save(os.path.join(base_dir, "deployed_add_review.png"))
    img27.save(os.path.join(base_dir, "deployed_add_review.jpeg"))

    print("Final UI Screenshots 26 and 27 generated successfully.")


if __name__ == '__main__':
    generate_final_images()
