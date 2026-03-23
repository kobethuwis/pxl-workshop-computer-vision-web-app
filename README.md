# PXL Workshop Computer Vision Web App

## Overview

The PXL Workshop Computer Vision Web App is a simple web application that allows users to upload an image and apply various computer vision filters to it. The available filters include cartoon, grayscale, edge detection, deep fry, and a Belgium flag filter.

## Features

- **Cartoon Filter**: Converts the image into a cartoon-like version.
- **Grayscale Filter**: Converts the image to grayscale.
- **Edge Detection Filter**: Detects edges in the image.
- **Deep Fry Filter**: Applies a deep-fried meme effect to the image.
- **Belgium Filter**: Converts the image to a Belgian flag.

## Prerequisites

- Python 3.10.12
- Extension for VSCode: vscode-pdf
- Extension for VSCode: HashiCorp Terraform

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/pxl-workshop-computer-vision-web-app.git
    cd pxl-workshop-computer-vision-web-app
    ```

2. **Install the required dependencies in a Python venv**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```sh
    python3 source_code/app.py
    ```

4. **Open the web app in your browser**:
    Navigate to `http://127.0.0.1:5000` in your web browser.

5. **Upload an image and apply a filter**:
    - Click on the "Choose File" button to select an image from your computer.
    - Select a filter from the dropdown menu.
    - Click the "Upload" button to apply the selected filter to the image.
    - The processed image will be displayed below the upload form.

## Dependencies

- Flask
- OpenCV
- NumPy
- Base64

## License

This project is licensed under the MIT License.