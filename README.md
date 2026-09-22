# iViwer
Image viwer application made by using python labraris tkinter &amp; PIL

# 🖼️ Tkinter Image Viewer

A simple and beginner-friendly **Image Viewer desktop application** built using **Python, Tkinter, and Pillow (PIL)**.

This application loads multiple images from an `img` folder and allows the user to browse through them using **Next (>>) and Previous (<<)** buttons.

## ✨ Features

* 🖼️ View multiple images
* ⏭️ Navigate to the next image
* ⏮️ Navigate to the previous image
* 🚫 Automatically disables navigation buttons at the first/last image
* 🎨 Custom image borders and UI colors
* 🪟 Simple Tkinter desktop interface
* 📁 Loads images from a relative `img` folder
* ❌ Exit button to close the application

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** — GUI development
* **Pillow (PIL)** — Image loading and processing

## 📂 Project Structure

```text
Tkinter/
│
├── iviwer.py
│
└── img/
    ├── 1.jpg
    ├── 2.jpg
    ├── 3.jpg
    ├── 4.jpg
    ├── 5.jpg
    ├── 6.jpg
    ├── 7.jpg
    ├── 8.jpg
    ├── 9.jpg
    └── 10.jpg
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Tkinter
```

### 3. Install Pillow

```bash
pip install pillow
```

> Tkinter is generally included with standard Python installations on Windows.

## ▶️ Run the Application

Run:

```bash
python iviwer.py
```

The application window will open and display the first image.

Use:

* `<<` — Previous image
* `>>` — Next image
* `EXIT` — Close the application

## 📸 Image Folder

The application expects images inside the `img` folder:

```text
img/1.jpg
img/2.jpg
...
img/10.jpg
```

The images are loaded using a relative path:

```python
path = f"img/{i}.jpg"
```

This makes the project portable instead of depending on an absolute Windows path.

## 🎨 Image Processing

Pillow is used to resize the images and add a border:

```python
ImageOps.expand(
    Image.open(path).resize((360, 470)),
    border=5,
    fill="#FE5BAC"
)
```

## 👨‍💻 Author

**Zeeshan**

Built as a Python/Tkinter practice project to learn:

* GUI development
* Event handling
* Functions and callbacks
* Image processing
* Relative file paths
* Tkinter widgets and layouts

## 📄 License

This project is intended for learning and educational purposes.
