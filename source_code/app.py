from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_image', methods=['POST'])
def process_image():
    file = request.files['image']
    npimg = np.fromfile(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Perform image processing to generate a cartoon-like version
    cartoon_img = cartoonize_image(img)

    # Encode cartoon image to send back to client
    _, img_encoded = cv2.imencode('.png', cartoon_img)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    response = {
        'image': img_base64
    }

    return jsonify(response)


@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    file = request.files['image']
    filter_type = request.form['filter']
    npimg = np.fromfile(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if filter_type == 'cartoon':
        processed_img = cartoonize_image(img)
    elif filter_type == 'grayscale':
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'edge_detection':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(gray, 100, 200)
    elif filter_type == 'deep_fry':
        processed_img = deep_fry_image(img)
    elif filter_type == 'belgium':
        processed_img = belgium_filter(img)
    else:
        return jsonify({'error': 'Invalid filter type'}), 400

    # Encode processed image to send back to client
    _, img_encoded = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    response = {
        'image': img_base64
    }

    return jsonify(response)


@app.route('/health')
def health():
    return 'OK'


def cartoonize_image(img):
    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply median blur
    gray = cv2.medianBlur(gray, 5)
    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Apply bilateral filter to smoothen the image
    color = cv2.bilateralFilter(img, 9, 300, 300)
    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def deep_fry_image(img):
    # Increase contrast
    contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=50)
    # Add noise
    noise = np.random.normal(0, 25, img.shape).astype(np.uint8)
    noisy_img = cv2.add(contrast, noise)
    # Apply a strong blur
    blurred = cv2.GaussianBlur(noisy_img, (11, 11), 0)
    # Increase saturation
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = cv2.add(hsv[..., 1], 50)
    saturated = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    # Add a red tint
    red_tint = np.full_like(saturated, (0, 0, 50))
    deep_fried = cv2.addWeighted(saturated, 0.8, red_tint, 0.2, 0)
    # Pixelate the image
    small = cv2.resize(deep_fried, (32, 32), interpolation=cv2.INTER_LINEAR)
    deep_fried = cv2.resize(
        small, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
    return deep_fried


def belgium_filter(img):
    # Define the colors of the Belgian flag
    colors = [
        (0, 0, 0),       # Black
        (0, 255, 255),   # Yellow
        (0, 0, 255)      # Red
    ]

    # Get the width of each section
    height, width, _ = img.shape
    section_width = width // 3

    # Apply the colors to each section
    img[:, :section_width] = colors[0]
    img[:, section_width:2*section_width] = colors[1]
    img[:, 2*section_width:] = colors[2]

    return img


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
