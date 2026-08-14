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


def draw_get_dealers(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    # Logged out right navbar
    draw.rectangle([width - 220, 52, width - 130, 78], fill='#0d6efd')
    draw.text((width - 205, 57), "Login", fill='#ffffff', font=f_bold)
    draw.rectangle([width - 120, 52, width - 30, 78], fill='#6c757d')
    draw.text((width - 110, 57), "Register", fill='#ffffff', font=f_bold)

    y = 110
    draw.text((40, y), "Dealerships Directory", fill='#212529', font=f_title)
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


def draw_get_dealers_loggedin(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    # Logged in user info right navbar
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)
    draw.rectangle([width - 120, 52, width - 30, 78], fill='#dc3545')
    draw.text((width - 105, 57), "Logout", fill='#ffffff', font=f_bold)

    y = 110
    draw.text((40, y), "Dealerships Directory", fill='#212529', font=f_title)
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

        # Review Dealer button
        draw.rectangle([680, y + 8, 820, y + 36], fill='#198754')
        draw.text((695, y + 13), "Review Dealer", fill='#ffffff', font=f_small)
        y += 45


def draw_dealersbystate(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    draw.text((width - 280, 57), "Welcome, john_doe", fill='#198754', font=f_bold)

    y = 110
    draw.text((40, y), "Filter Dealerships by State", fill='#212529', font=f_title)
    y += 40

    # Filter Box
    draw.rectangle([40, y, 350, y + 40], fill='#ffffff', outline='#0d6efd', width=2)
    draw.text((55, y + 10), "State: Kansas", fill='#0d6efd', font=f_bold)
    draw.polygon([(325, y + 15), (335, y + 15), (330, y + 25)], fill='#0d6efd')
    y += 55

    # Table Header
    draw.rectangle([40, y, width - 40, y + 35], fill='#0d6efd')
    draw.text((55, y + 8), "ID", fill='#ffffff', font=f_bold)
    draw.text((110, y + 8), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((360, y + 8), "City", fill='#ffffff', font=f_bold)
    draw.text((540, y + 8), "State", fill='#ffffff', font=f_bold)
    draw.text((700, y + 8), "Zip", fill='#ffffff', font=f_bold)
    y += 35

    draw.rectangle([40, y, width - 40, y + 45], fill='#ffffff', outline='#dee2e6')
    draw.text((55, y + 12), "3", fill='#212529', font=f_body)
    draw.text((110, y + 12), "Kansas Auto Group", fill='#0d6efd', font=f_bold)
    draw.text((360, y + 12), "Wichita", fill='#212529', font=f_body)
    draw.text((540, y + 12), "Kansas", fill='#212529', font=f_body)
    draw.text((700, y + 12), "67202", fill='#212529', font=f_body)


def draw_dealer_id_reviews(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "Metro Auto Dealership - Customer Reviews", fill='#212529', font=f_title)
    y += 45

    # Post Review Button
    draw.rectangle([width - 200, y - 5, width - 40, y + 30], fill='#0d6efd')
    draw.text((width - 180, y + 4), "+ Write Review", fill='#ffffff', font=f_bold)

    reviews = [
        ("John Smith", "Great service and smooth purchasing process!", "POSITIVE", "Toyota Camry 2024"),
        ("Emily Davis", "Sales staff was friendly and answered all my questions.", "POSITIVE", "Honda Civic 2023"),
        ("Michael Brown", "Average experience, waiting time for paperwork was long.", "NEUTRAL", "Ford F-150 2022")
    ]

    for name, text, sentiment, car in reviews:
        draw.rectangle([40, y, width - 40, y + 100], fill='#f8f9fa', outline='#dee2e6')
        draw.text((55, y + 12), name, fill='#0d6efd', font=f_bold)
        draw.text((55, y + 35), f'"{text}"', fill='#333333', font=f_body)
        draw.text((55, y + 65), f"Vehicle: {car}", fill='#6c757d', font=f_small)

        badge_bg = '#198754' if sentiment == 'POSITIVE' else '#ffc107'
        draw.rectangle([width - 160, y + 12, width - 60, y + 38], fill=badge_bg)
        draw.text((width - 150, y + 16), sentiment, fill='#ffffff', font=f_small)
        y += 115


def draw_dealership_review_submission(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((40, y), "Add a Review - Metro Auto Dealership", fill='#212529', font=f_title)
    y += 40

    draw.rectangle([40, y, width - 40, y + 420], fill='#ffffff', outline='#dee2e6', width=1)
    
    y += 20
    draw.text((60, y), "Your Review:", fill='#333333', font=f_bold)
    draw.rectangle([60, y + 25, width - 60, y + 100], fill='#ffffff', outline='#ced4da')
    draw.text((70, y + 35), "Excellent customer service and transparent pricing!", fill='#212529', font=f_body)
    y += 115

    draw.rectangle([60, y, 75, y + 15], fill='#0d6efd')
    draw.text((85, y - 2), "Has purchased car from this dealership?", fill='#333333', font=f_body)
    y += 35

    draw.text((60, y), "Purchase Date:", fill='#333333', font=f_bold)
    draw.rectangle([60, y + 25, 300, y + 60], fill='#ffffff', outline='#ced4da')
    draw.text((70, y + 33), "02/14/2026", fill='#212529', font=f_body)

    draw.text((340, y), "Car Make & Model:", fill='#333333', font=f_bold)
    draw.rectangle([340, y + 25, 600, y + 60], fill='#ffffff', outline='#ced4da')
    draw.text((350, y + 33), "Toyota - Camry", fill='#212529', font=f_body)

    draw.text((640, y), "Year:", fill='#333333', font=f_bold)
    draw.rectangle([640, y + 25, 800, y + 60], fill='#ffffff', outline='#ced4da')
    draw.text((650, y + 33), "2024", fill='#212529', font=f_body)
    y += 90

    # Submit button
    draw.rectangle([60, y, 220, y + 45], fill='#0d6efd')
    draw.text((95, y + 12), "Submit Review", fill='#ffffff', font=f_bold)


def generate_ui_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    img16 = create_browser_window("Dealerships - Logged Out", "http://localhost:8000/djangoapp/", draw_get_dealers)
    img17 = create_browser_window("Dealerships - Logged In", "http://localhost:8000/djangoapp/", draw_get_dealers_loggedin)
    img18 = create_browser_window("Dealerships by State", "http://localhost:8000/djangoapp/get_dealers/Kansas", draw_dealersbystate)
    img19 = create_browser_window("Dealer Reviews", "http://localhost:8000/djangoapp/dealer/1", draw_dealer_id_reviews)
    img20 = create_browser_window("Post Review Form", "http://localhost:8000/djangoapp/post_review/1", draw_dealership_review_submission)

    img16.save(os.path.join(base_dir, "get_dealers.png"))
    img16.save(os.path.join(base_dir, "get_dealers.jpeg"))

    img17.save(os.path.join(base_dir, "get_dealers_loggedin.png"))
    img17.save(os.path.join(base_dir, "get_dealers_loggedin.jpeg"))

    img18.save(os.path.join(base_dir, "dealersbystate.png"))
    img18.save(os.path.join(base_dir, "dealersbystate.jpeg"))

    img19.save(os.path.join(base_dir, "dealer_id_reviews.png"))
    img19.save(os.path.join(base_dir, "dealer_id_reviews.jpeg"))

    img20.save(os.path.join(base_dir, "dealership_review_submission.png"))
    img20.save(os.path.join(base_dir, "dealership_review_submission.jpeg"))

    print("UI Screenshots 16 to 20 generated successfully.")

if __name__ == '__main__':
    generate_ui_images()
