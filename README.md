# Smart Parking Space Analyzer

A computer vision-based web application for analyzing parking spaces from an input image and identifying whether individual parking spaces are occupied or vacant.

The project uses **Python, Flask, OpenCV, and NumPy** to process parking-area images and display the analysis through a simple web-based interface.

## Project Overview

Finding available parking spaces manually can be time-consuming, especially in large parking areas. This project provides a simple computer vision solution that analyzes a parking-area image and determines the occupancy status of predefined parking spaces.

The application allows the user to:

- Upload a parking-area image
- Analyze predefined parking spaces
- Detect occupied and vacant spaces
- Calculate overall parking occupancy
- Display the analyzed image with parking-space annotations
- View the status of individual parking spaces through the web interface

## Features

- Parking space detection
- Image upload through a web interface
- Computer vision-based occupancy analysis
- Total, occupied, vacant, and occupancy percentage statistics
- Visual indication of vacant and occupied parking spaces
- Flask-based web interface
- Automated testing using Pytest

## Technologies Used

- **Python**
- **Flask**
- **OpenCV**
- **NumPy**
- **HTML**
- **CSS**
- **Pytest**

## Project Structure

```text
smart-parking-ui-project/
â”‚
â”œâ”€â”€ app.py
â”œâ”€â”€ README.md
â”œâ”€â”€ requirements.txt
â”‚
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ config/
â”‚   â”‚   â””â”€â”€ parking_spaces.json
â”‚   â””â”€â”€ input/
â”‚       â””â”€â”€ sample_parking.jpg
â”‚
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â””â”€â”€ parking_analyzer.py
â”‚
â”œâ”€â”€ static/
â”‚   â””â”€â”€ style.css
â”‚
â”œâ”€â”€ templates/
â”‚   â””â”€â”€ index.html
â”‚
â””â”€â”€ tests/
    â””â”€â”€ test_analyzer.py
```

## How the System Works

```text
Input Parking Image
        â†“
Parking Space Configuration
        â†“
Image Processing using OpenCV
        â†“
Analyze Individual Parking Spaces
        â†“
Determine Occupied / Vacant Status
        â†“
Calculate Parking Statistics
        â†“
Display Results in Web Interface
```

## Requirements

Make sure the following are installed:

- Python 3.x
- pip
- A modern web browser

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pallavi050253/smart-parking-ui-project.git
cd smart-parking-ui-project
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

On Windows:

```bash
py -m pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

On Windows:

```bash
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Using the Application

1. Open the web application in a browser.
2. Select a parking-area image.
3. Click **Analyze Parking**.
4. The system processes the image.
5. Parking spaces are classified as occupied or vacant.
6. The application displays:
   - Total parking spaces
   - Occupied spaces
   - Vacant spaces
   - Occupancy percentage
7. The processed image is displayed with parking-space annotations.

## Parking Space Configuration

Parking-space coordinates are stored in:

```text
data/config/parking_spaces.json
```

The configuration defines the regions that the system analyzes in the parking image.

For a different parking layout, the coordinates can be updated according to the parking-space locations in the input image.

## Testing

The project includes automated tests using **Pytest**.

Run:

```bash
python -m pytest -q
```

On Windows:

```bash
py -m pytest -q
```

## Example Output

The application provides parking statistics such as:

```text
Total Spaces: 8
Occupied: 3
Vacant: 5
Occupancy: 37.5%
```

The processed image also displays the status of individual parking spaces.

## Future Improvements

Possible future extensions include:

- Real-time camera/video stream analysis
- Automatic parking-space detection
- Deep-learning-based vehicle detection
- Vehicle counting
- License plate recognition
- Historical occupancy analytics
- Database integration
- Cloud deployment
- Mobile-friendly interface
- Real-time parking availability updates

## Project Purpose

This project demonstrates the application of **Computer Vision and image processing techniques** to a practical parking-management problem. It combines image analysis with a web interface to make the results easier to understand and use.

## Author

**Pallavi Joshi**

B.Tech â€“ Computer Science and Engineering (AIML)  
VIT Bhopal University

## License

This project is created for educational and academic purposes.