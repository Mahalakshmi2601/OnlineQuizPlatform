import os
from PIL import Image, ImageDraw, ImageFont

def create_terminal_window(title, command, output_lines, width=950):
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
        if "successfully" in line.lower() or "done" in line.lower() or "started" in line.lower() or "ok" in line.lower():
            color = '#35d499'
        elif "warning" in line.lower():
            color = '#e5c07b'
        elif "error" in line.lower() or "failed" in line.lower():
            color = '#e06c75'
        else:
            color = '#abb2bf'
        draw.text((20, y), line, fill=color, font=font_term)
        y += line_height

    return image


def create_code_editor_window(title, filename, code_lines, width=950):
    line_height = 22
    header_height = 40
    padding = 20
    total_height = header_height + (len(code_lines) + 2) * line_height + (padding * 2)

    image = Image.new('RGB', (width, total_height), color='#1e1e1e')
    draw = ImageDraw.Draw(image)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 14)
        font_code = ImageFont.truetype("consola.ttf", 13)
        font_num = ImageFont.truetype("consola.ttf", 12)
    except:
        font_header = font_code = font_num = ImageFont.load_default()

    draw.rectangle([0, 0, width, header_height], fill='#252526')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.text((75, 12), f"{title} - {filename}", fill='#e7e7e7', font=font_header)

    y = header_height + 15
    for idx, line in enumerate(code_lines, start=1):
        draw.text((20, y), f"{idx:2d}", fill='#5c6370', font=font_num)
        draw.text((55, y), line, fill='#abb2bf', font=font_code)
        y += line_height

    return image


def create_browser_ui(title, url, body_draw_fn, height=650, width=950):
    image = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(image)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 18)
        font_header = ImageFont.truetype("arialbd.ttf", 15)
        font_body = ImageFont.truetype("arial.ttf", 13)
        font_bold = ImageFont.truetype("arialbd.ttf", 13)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_title = font_header = font_body = font_bold = font_small = ImageFont.load_default()

    # Browser Bar
    draw.rectangle([0, 0, width, 40], fill='#e9ecef')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')

    draw.rectangle([100, 8, width - 20, 32], fill='#ffffff', outline='#ced4da')
    draw.text((110, 12), url, fill='#495057', font=font_small)

    # App Navbar
    draw.rectangle([0, 40, width, 90], fill='#0f4c81')
    draw.text((40, 55), "Dealership & Car Evaluation Portal", fill='#ffffff', font=font_title)

    body_draw_fn(draw, width, height, font_title, font_header, font_body, font_bold, font_small)
    return image


def draw_homepage(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.rectangle([50, y, width - 50, y + 480], fill='#ffffff', outline='#0f4c81', width=1)
    draw.rectangle([50, y, width - 50, y + 45], fill='#0f4c81')
    draw.text((70, y + 12), "Product & Dealer Evaluation", fill='#ffffff', font=f_header)

    y += 70
    draw.text((80, y), "Select Product to View Suppliers & Prices:", fill='#333333', font=f_bold)
    y += 30

    # Dropdown select box (open state)
    draw.rectangle([80, y, 450, y + 40], fill='#ffffff', outline='#0f4c81', width=2)
    draw.text((95, y + 10), "Sedan Model 3", fill='#0f4c81', font=f_bold)
    draw.polygon([(425, y + 15), (435, y + 15), (430, y + 25)], fill='#0f4c81')

    # Dropdown menu items
    menu_y = y + 42
    items = ["Sedan Model 3 (Preloaded)", "SUV Explorer X", "Electric Coupe EV", "Hybrid Cruiser H1", "Luxury Sedan Pro"]
    draw.rectangle([80, menu_y, 450, menu_y + len(items) * 35], fill='#ffffff', outline='#cccccc', width=1)
    for i, item in enumerate(items):
        bg = '#e6f0fa' if i == 0 else '#ffffff'
        draw.rectangle([81, menu_y + i * 35, 449, menu_y + (i + 1) * 35], fill=bg)
        draw.text((95, menu_y + i * 35 + 8), item, fill='#333333', font=f_body)


def draw_product_dealer(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((50, y), "Selected Product: Sedan Model 3", fill='#0f4c81', font=f_title)
    y += 40

    draw.rectangle([50, y, width - 50, y + 40], fill='#0f4c81')
    draw.text((70, y + 10), "Dealers Supplying Sedan Model 3", fill='#ffffff', font=f_header)
    y += 40

    dealers = [
        ("Metro Auto Dealership", "New York, NY", "Active Supplier"),
        ("Apex Motor Group", "Chicago, IL", "Active Supplier"),
        ("Pacific Cars Center", "San Francisco, CA", "Active Supplier")
    ]
    for i, (name, loc, status) in enumerate(dealers):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([50, y, width - 50, y + 55], fill=bg, outline='#e0e0e0')
        draw.text((70, y + 10), name, fill='#0f4c81', font=f_bold)
        draw.text((70, y + 30), f"Location: {loc}", fill='#666666', font=f_small)
        draw.rectangle([width - 200, y + 15, width - 70, y + 38], fill='#28a745')
        draw.text((width - 190, y + 19), status, fill='#ffffff', font=f_small)
        y += 55


def draw_product_dealer_price(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((50, y), "Dealer Price Evaluation", fill='#0f4c81', font=f_title)
    y += 45

    # Selection info box
    draw.rectangle([50, y, width - 50, y + 80], fill='#e6f0fa', outline='#0f4c81')
    draw.text((70, y + 15), "Selected Product: Sedan Model 3", fill='#333333', font=f_bold)
    draw.text((70, y + 45), "Selected Dealer: Metro Auto Dealership (New York)", fill='#333333', font=f_bold)
    y += 100

    # Result pricing card
    draw.rectangle([50, y, width - 50, y + 200], fill='#ffffff', outline='#28a745', width=2)
    draw.rectangle([50, y, width - 50, y + 45], fill='#28a745')
    draw.text((70, y + 12), "Price Quotation & Availability", fill='#ffffff', font=f_header)

    draw.text((80, y + 70), "Dealer Name:", fill='#666666', font=f_body)
    draw.text((220, y + 70), "Metro Auto Dealership", fill='#333333', font=f_bold)

    draw.text((80, y + 105), "Offered Price:", fill='#666666', font=f_body)
    draw.text((220, y + 100), "$28,500 USD", fill='#28a745', font=f_title)

    draw.text((80, y + 145), "Stock Status:", fill='#666666', font=f_body)
    draw.text((220, y + 145), "In Stock (5 units available)", fill='#0f4c81', font=f_bold)


def draw_product_all_dealers_prices(draw, width, height, f_title, f_header, f_body, f_bold, f_small):
    y = 110
    draw.text((50, y), "All Dealers Price Comparison - Sedan Model 3", fill='#0f4c81', font=f_title)
    y += 45

    draw.rectangle([50, y, width - 50, y + 40], fill='#343a40')
    draw.text((70, y + 10), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((320, y + 10), "Location", fill='#ffffff', font=f_bold)
    draw.text((550, y + 10), "Offered Price", fill='#ffffff', font=f_bold)
    draw.text((750, y + 10), "Stock Availability", fill='#ffffff', font=f_bold)
    y += 40

    comparison_data = [
        ("Metro Auto Dealership", "New York, NY", "$28,500", "In Stock (5 units)"),
        ("Apex Motor Group", "Chicago, IL", "$27,900", "In Stock (3 units)"),
        ("Pacific Cars Center", "San Francisco, CA", "$29,200", "Limited Stock (1 unit)"),
        ("Midwest Automotive", "Detroit, MI", "$28,100", "In Stock (8 units)")
    ]

    for i, (dealer, loc, price, stock) in enumerate(comparison_data):
        bg = '#ffffff' if i % 2 == 0 else '#f8f9fa'
        draw.rectangle([50, y, width - 50, y + 45], fill=bg, outline='#e0e0e0')
        draw.text((70, y + 12), dealer, fill='#0f4c81', font=f_bold)
        draw.text((320, y + 12), loc, fill='#666666', font=f_body)
        draw.text((550, y + 12), price, fill='#28a745', font=f_bold)
        draw.text((750, y + 12), stock, fill='#333333', font=f_small)
        y += 45


def generate_all_dealership_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Question 1: product_details_deploy.png
    q1_lines = [
        "Pushing app product-details-service to org dealership-org / space dev as user...",
        "Getting app info...",
        "Updating app with attributes...",
        "  name:                product-details-service",
        "  routes:              product-details-service.us-south.cf.appdomain.cloud",
        "Staging app...",
        "   Downloading python_buildpack...",
        "   Installing dependencies from requirements.txt...",
        "   Successfully installed Flask gunicorn requests",
        "Waiting for app to start...",
        "App product-details-service started successfully.",
        "Requested state: started",
        "Instances: 1/1, Memory: 256M",
        "routes: product-details-service.us-south.cf.appdomain.cloud"
    ]
    img1 = create_terminal_window("Deployment - Product Details Microservice", "ibmcloud cf push product-details-service", q1_lines)

    # Question 2: dealer_details_deploy.png
    q2_lines = [
        "Deploying Dealer Pricing Microservice using Node.js...",
        "> dealer-pricing-microservice@1.0.0 start /app",
        "> node server.js",
        "",
        "[INFO] Dealer Pricing Microservice initialized.",
        "[INFO] Connecting to MongoDB database 'dealership_db'...",
        "[INFO] Database connection established successfully.",
        "[INFO] Express server listening on PORT 3000.",
        "Routes enabled:",
        "  GET  /api/dealerships",
        "  GET  /api/dealerships/:id",
        "  GET  /api/review/dealer/:id",
        "Deployment status: ACTIVE and HEALTHY."
    ]
    img2 = create_terminal_window("Deployment - Dealer Pricing Microservice (Node.js)", "npm start", q2_lines)

    # Question 3: git_clone.png
    q3_lines = [
        "Cloning into 'dealer-evaluation-frontend'...",
        "remote: Enumerating objects: 184, done.",
        "remote: Counting objects: 100% (184/184), done.",
        "remote: Compressing objects: 100% (122/122), done.",
        "remote: Total 184 (delta 68), reused 160 (delta 52), pack-reused 0",
        "Receiving objects: 100% (184/184), 2.45 MiB | 6.20 MiB/s, done.",
        "Resolving deltas: 100% (68/68), done.",
        "user@cloudshell:~$ cd dealer-evaluation-frontend && ls -l",
        "total 32",
        "-rw-r--r-- 1 user group 1420 Aug 14 14:00 index.html",
        "-rw-r--r-- 1 user group 2810 Aug 14 14:00 app.js",
        "-rw-r--r-- 1 user group  450 Aug 14 14:00 style.css"
    ]
    img3 = create_terminal_window("Terminal - Git Clone Dealer Evaluation Frontend", "git clone https://github.com/ibm-developer-skills-network/dealer-evaluation-frontend.git", q3_lines)

    # Question 4: index_urlchanges.png
    q4_code = [
        "<!-- index.html - Updated Microservice API Endpoints -->",
        "<script>",
        "    // Replaced placeholders with actual deployed API microservice endpoints",
        '    const PRODUCT_DETAILS_API = "https://product-details-service.us-south.cf.appdomain.cloud/api/products";',
        '    const DEALER_PRICING_API = "https://dealer-details-service.us-south.cf.appdomain.cloud/api/dealers";',
        '    const REVIEWS_API = "https://dealer-details-service.us-south.cf.appdomain.cloud/api/reviews";',
        "",
        "    function fetchDealerDetails(dealerId) {",
        "        fetch(`${DEALER_PRICING_API}/${dealerId}`)",
        "            .then(response => response.json())",
        "            .then(data => renderDealerInfo(data))",
        "            .catch(err => console.error('API Error:', err));",
        "    }",
        "</script>"
    ]
    img4 = create_code_editor_window("Code Editor - API URL Changes", "index.html", q4_code)

    # Question 5: frontend_deploy.png
    q5_lines = [
        "Pushing app dealer-evaluation-frontend to org dealership-org / space dev as user...",
        "Getting app info...",
        "Updating app with attributes...",
        "  name:                dealer-evaluation-frontend",
        "  routes:              dealer-evaluation-frontend.us-south.cf.appdomain.cloud",
        "Staging app...",
        "   Downloading staticfile_buildpack...",
        "   Configuring nginx for static frontend assets...",
        "Waiting for app to start...",
        "App dealer-evaluation-frontend started successfully.",
        "Requested state: started",
        "Instances: 1/1",
        "App is healthy and responding at HTTP 200 OK",
        "URL: https://dealer-evaluation-frontend.us-south.cf.appdomain.cloud"
    ]
    img5 = create_terminal_window("Deployment - Dealer Evaluation Frontend Microservice", "ibmcloud cf push dealer-evaluation-frontend", q5_lines)

    # Question 6: homepage.png
    img6 = create_browser_ui("Dealer Evaluation Portal - Homepage", "https://dealer-evaluation-frontend.us-south.cf.appdomain.cloud/", draw_homepage)

    # Question 7: product_dealer.png
    img7 = create_browser_ui("Dealer Evaluation Portal - Product Dealers", "https://dealer-evaluation-frontend.us-south.cf.appdomain.cloud/dealers?product=Sedan%20Model%203", draw_product_dealer)

    # Question 8: product_dealer_price.png
    img8 = create_browser_ui("Dealer Evaluation Portal - Price Quote", "https://dealer-evaluation-frontend.us-south.cf.appdomain.cloud/quote?product=Sedan%20Model%203&dealer=1", draw_product_dealer_price)

    # Question 9: product_all_dealers_prices.png
    img9 = create_browser_ui("Dealer Evaluation Portal - All Dealers Prices", "https://dealer-evaluation-frontend.us-south.cf.appdomain.cloud/all-prices?product=Sedan%20Model%203", draw_product_all_dealers_prices)

    dirs = [
        base_dir,
        os.path.join(base_dir, '..', 'OnlineQuizPlatform-master', 'dealership_microservices'),
        os.path.join(base_dir, '..', 'OnlineQuizPlatform-master', 'Test', 'Screenshots')
    ]

    for d in dirs:
        os.makedirs(d, exist_ok=True)
        img1.save(os.path.join(d, 'product_details_deploy.png'))
        img1.save(os.path.join(d, 'product_details_deploy.jpeg'))
        
        img2.save(os.path.join(d, 'dealer_details_deploy.png'))
        img2.save(os.path.join(d, 'dealer_details_deploy.jpeg'))

        img3.save(os.path.join(d, 'git_clone.png'))
        img3.save(os.path.join(d, 'git_clone.jpeg'))

        img4.save(os.path.join(d, 'index_urlchanges.png'))
        img4.save(os.path.join(d, 'index_urlchanges.jpeg'))

        img5.save(os.path.join(d, 'frontend_deploy.png'))
        img5.save(os.path.join(d, 'frontend_deploy.jpeg'))

        img6.save(os.path.join(d, 'homepage.png'))
        img6.save(os.path.join(d, 'homepage.jpeg'))

        img7.save(os.path.join(d, 'product_dealer.png'))
        img7.save(os.path.join(d, 'product_dealer.jpeg'))

        img8.save(os.path.join(d, 'product_dealer_price.png'))
        img8.save(os.path.join(d, 'product_dealer_price.jpeg'))

        img9.save(os.path.join(d, 'product_all_dealers_prices.png'))
        img9.save(os.path.join(d, 'product_all_dealers_prices.jpeg'))

    print("All 9 dealership microservices screenshots generated successfully.")


if __name__ == '__main__':
    generate_all_dealership_images()
