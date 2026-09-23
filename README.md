# Computer Vision Session 1

This repository contains two Computer Vision tasks implemented using Python, OpenCV, NumPy, and Object-Oriented Programming (OOP).

## Tasks

### 1. Mini Painter

A simple interactive drawing application that allows the user to:

* Draw circles, rectangles, and polygons.
* Select colors using the keyboard.
* Draw shapes using the mouse.
* Display the current shape and color.
* Save the drawn canvas.

#### Controls

| Key | Action           |
| --- | ---------------- |
| `C` | Select Circle    |
| `R` | Select Rectangle |
| `P` | Select Polygon   |
| `1` | White            |
| `2` | Red              |
| `3` | Green            |
| `4` | Blue             |
| `5` | Yellow           |
| `W` | Save the drawing |
| `Q` | Quit             |

#### Run

From the `mini_painter` directory:

```bash
python main.py
```

---

### 2. Object Counter

A color-based object detection and counting application.

The application:

* Loads a BGR image.
* Converts the image from BGR to HSV.
* Applies color-based thresholding.
* Detects contours.
* Draws bounding boxes around detected objects.
* Counts objects of the selected color.
* Allows detecting different colors without restarting the program.

#### Controls -

| Key | Action               |
| --- | -------------------- |
| `1` | Detect Red objects   |
| `2` | Detect Green objects |
| `3` | Detect Blue objects  |
| `Q` | Quit                 |

#### Run -

From the project root:

```bash
python -m object_counter.main
```

The test image is located at:

```text
test_images/image.png
```

---

## Project Structure

```text
CV_Session1/
│
├── mini_painter/
│   ├── __init__.py
│   ├── main.py
│   ├── painter.py
│   ├── canvas.py
│   ├── color_manager.py
│   └── shapes/
│       ├── shape.py
│       ├── circle.py
│       ├── rectangle.py
│       └── polygon.py
│
├── object_counter/
│   ├── __init__.py
│   ├── main.py
│   ├── object_counter.py
│   ├── image_processor.py
│   ├── color_detector.py
│   └── contour_detector.py
│
├── test_images/
│   └── image.png
│
├── docs/
│   ├── user_manual.md
│   └── technical_document.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* OpenCV
* NumPy
* Object-Oriented Programming (OOP)

## Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Documentation

Detailed documentation is available in the `docs/` directory:

* `user_manual.md` — instructions for using the applications.
* `technical_document.md` — technical implementation details, libraries, architecture, and design decisions.
