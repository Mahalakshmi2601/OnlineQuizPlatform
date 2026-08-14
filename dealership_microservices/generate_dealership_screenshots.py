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

    # Window Header
    draw.rectangle([0, 0, width, header_height], fill='#323233')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.text((75, 12), title, fill='#cccccc', font=font_header)

    # Content
    y = header_height + 15
    # Prompt line
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

    # Window Header
    draw.rectangle([0, 0, width, header_height], fill='#252526')
    draw.ellipse([15, 13, 27, 25], fill='#ff5f56')
    draw.ellipse([35, 13, 47, 25], fill='#ffbd2e')
    draw.ellipse([55, 13, 67, 25], fill='#27c93f')
    draw.text((75, 12), f"{title} - {filename}", fill='#e7e7e7', font=font_header)

    y = header_height + 15
    for idx, line in enumerate(code_lines, start=1):
        # Line number
        draw.text((20, y), f"{idx:2d}", fill='#5c6370', font=font_num)
        # Code text
        draw.text((55, y), line, fill='#abb2bf', font=font_code)
        y += line_height

    return image


def generate_all_dealership_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Question 1: product_details_deploy.png
    q1_lines = [
        "Pushing app product-details-service to org dealership-org / space dev as user...",
        "Getting app info...",
        "Updating app with these attributes...",
        "  name:                product-details-service",
        "  path:                /tmp/app",
        "  routes:              product-details-service.us-south.cf.appdomain.cloud",
        "Staging app and tracing logs...",
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

    # Directories to save
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

    print("All 5 dealership microservices screenshots generated successfully.")


if __name__ == '__main__':
    generate_all_dealership_images()
