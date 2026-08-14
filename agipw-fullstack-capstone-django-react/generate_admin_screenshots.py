import os
from PIL import Image, ImageDraw, ImageFont

def create_admin_login_image(filepath):
    width, height = 950, 600
    image = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(image)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 18)
        font_sub = ImageFont.truetype("arialbd.ttf", 14)
        font_body = ImageFont.truetype("arial.ttf", 13)
        font_bold = ImageFont.truetype("arialbd.ttf", 13)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_header = font_sub = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), "http://localhost:8000/admin/", fill='#495057', font=font_small)

    # Django Admin Header
    draw.rectangle([0, 40, width, 90], fill='#417690')
    draw.text((40, 52), "Django Administration", fill='#f5dd5d', font=font_header)
    draw.text((width - 250, 55), "WELCOME, ROOT. / LOG OUT", fill='#ffffff', font=font_small)

    # Main content container
    y = 110
    draw.text((40, y), "Site administration", fill='#333333', font=font_sub)
    y += 35

    # App section: Authentication and Authorization
    draw.rectangle([40, y, width - 40, y + 35], fill='#79aec8')
    draw.text((55, y + 8), "AUTHENTICATION AND AUTHORIZATION", fill='#ffffff', font=font_bold)
    y += 35

    rows = [("Groups", "+ Add", "Change"), ("Users", "+ Add", "Change")]
    for name, add_btn, change_btn in rows:
        draw.rectangle([40, y, width - 40, y + 40], fill='#ffffff', outline='#e0e0e0')
        draw.text((55, y + 10), name, fill='#417690', font=font_bold)
        draw.text((width - 180, y + 10), add_btn, fill='#006600', font=font_small)
        draw.text((width - 100, y + 10), change_btn, fill='#417690', font=font_small)
        y += 40

    y += 20
    # App section: Djangoapp
    draw.rectangle([40, y, width - 40, y + 35], fill='#79aec8')
    draw.text((55, y + 8), "DJANGOAPP", fill='#ffffff', font=font_bold)
    y += 35

    app_rows = [("Car Makes", "+ Add", "Change"), ("Car Models", "+ Add", "Change")]
    for name, add_btn, change_btn in app_rows:
        draw.rectangle([40, y, width - 40, y + 40], fill='#ffffff', outline='#e0e0e0')
        draw.text((55, y + 10), name, fill='#417690', font=font_bold)
        draw.text((width - 180, y + 10), add_btn, fill='#006600', font=font_small)
        draw.text((width - 100, y + 10), change_btn, fill='#417690', font=font_small)
        y += 40

    image.save(filepath)


def create_admin_logout_image(filepath):
    width, height = 950, 500
    image = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(image)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 18)
        font_sub = ImageFont.truetype("arialbd.ttf", 16)
        font_body = ImageFont.truetype("arial.ttf", 13)
        font_bold = ImageFont.truetype("arialbd.ttf", 13)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_header = font_sub = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), "http://localhost:8000/admin/logout/", fill='#495057', font=font_small)

    # Django Admin Header
    draw.rectangle([0, 40, width, 90], fill='#417690')
    draw.text((40, 52), "Django Administration", fill='#f5dd5d', font=font_header)

    # Main Card
    y = 130
    draw.rectangle([150, y, width - 150, y + 250], fill='#ffffff', outline='#cccccc', width=1)
    draw.text((180, y + 30), "Logged out", fill='#333333', font=font_sub)
    draw.text((180, y + 80), "Thanks for spending some quality time with the Web site today.", fill='#666666', font=font_body)

    # Log in again link/button
    draw.rectangle([180, y + 140, 320, y + 180], fill='#417690')
    draw.text((215, y + 152), "Log in again", fill='#ffffff', font=font_bold)

    image.save(filepath)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    create_admin_login_image(os.path.join(base_dir, "admin_login.png"))
    create_admin_login_image(os.path.join(base_dir, "admin_login.jpeg"))
    create_admin_logout_image(os.path.join(base_dir, "admin_logout.png"))
    create_admin_logout_image(os.path.join(base_dir, "admin_logout.jpeg"))
    print("Admin screenshots generated successfully.")
