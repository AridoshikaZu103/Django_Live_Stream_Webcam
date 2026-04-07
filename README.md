# 🎥 Django Live Stream Webcam

A real-time webcam live streaming web application built with **Django** and **OpenCV**. Stream your webcam feed directly in the browser with video recording and screenshot capabilities.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [How It Works](#-how-it-works)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔴 **Live Streaming** | Real-time webcam video feed streamed directly to the browser |
| 🎬 **Video Recording** | Start/stop recording and download as MP4 |
| 📸 **Screenshot Capture** | Take instant screenshots and download as PNG |
| 🪞 **Mirror Mode** | Video is horizontally flipped for a natural mirror experience |
| 📱 **Responsive UI** | Built with Bootstrap 5 for a clean, responsive layout |
| 🖥️ **Dual Streaming** | Server-side (OpenCV) + Client-side (MediaDevices API) streaming support |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.10+**
- **Django 4.2** — Web framework
- **OpenCV (cv2)** — Server-side video capture & frame processing

### Frontend
- **HTML5 / CSS3 / JavaScript**
- **Bootstrap 5.3** — UI styling & responsive layout
- **Font Awesome 6** — Icons
- **MediaRecorder API** — Client-side video recording
- **Canvas API** — Screenshot capture

### Database
- **SQLite3** — Default lightweight database

---

## 📁 Project Structure

```
Django_Live_Stream_Webcam/
│
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database
├── README.md                    # This file
├── RUN.txt                      # Quick-start commands
├── .gitignore                   # Git ignore rules
│
├── video_stream/                # Django project configuration
│   ├── __init__.py
│   ├── settings.py              # Project settings (Django 4.2)
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
│
└── stream/                      # Main streaming app
    ├── __init__.py
    ├── admin.py                 # Admin configuration
    ├── apps.py                  # App configuration
    ├── models.py                # Database models
    ├── views.py                 # VideoCamera class & view logic
    ├── urls.py                  # App-level URL routes
    ├── tests.py                 # Unit tests
    └── templates/
        └── index.html           # Live stream UI template
```

---

## 📌 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher** — [Download Python](https://www.python.org/downloads/)
- **pip** — Python package manager (comes with Python)
- **Git** — [Download Git](https://git-scm.com/downloads)
- **Webcam** — A connected and working webcam/camera device

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AridoshikaZu103/Django_Live_Stream_Webcam.git
cd Django_Live_Stream_Webcam
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django opencv-python
```

> **Note:** If you encounter issues with `opencv-python`, try:
> ```bash
> pip install opencv-python-headless
> ```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Open in Browser

Navigate to: **http://127.0.0.1:8000/**

---

## 🎮 Usage

### Live Stream
- Open the app in your browser — the webcam feed starts automatically.
- **Allow camera/microphone access** when prompted by the browser.

### Video Recording
1. Click **`Start Recording`** to begin recording the webcam feed.
2. Click **`Stop Recording`** to stop — the video file (`recorded_video.mp4`) will download automatically.

### Screenshot
- Click **`Screenshot`** to capture the current frame — the image (`screenshot.png`) will download automatically.

---

## 🔗 API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `GET` | `/` | Home page — renders the live stream UI |
| `GET` | `/video_feed/` | MJPEG video stream endpoint (server-side OpenCV) |
| `GET` | `/admin/` | Django admin panel |

---

## ⚙️ How It Works

### Server-Side Streaming (OpenCV)

```
Webcam → OpenCV VideoCapture → JPEG Encoding → StreamingHttpResponse → Browser
```

1. The `VideoCamera` class captures frames from the webcam using OpenCV (`cv2.VideoCapture(0)`).
2. Each frame is encoded as JPEG.
3. Frames are yielded via a generator function (`generate_frames`).
4. Django's `StreamingHttpResponse` sends frames as a continuous MJPEG stream using `multipart/x-mixed-replace` content type.

### Client-Side Streaming (MediaDevices API)

The `index.html` template also uses the browser's **MediaDevices API** (`navigator.mediaDevices.getUserMedia`) for:
- Displaying the live webcam feed in a `<video>` element.
- Recording video via the **MediaRecorder API**.
- Capturing screenshots via the **Canvas API**.

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Webcam not detected** | Ensure your webcam is connected and not being used by another application. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in `stream/views.py`. |
| **`ModuleNotFoundError: No module named 'cv2'`** | Install OpenCV: `pip install opencv-python` |
| **`ModuleNotFoundError: No module named 'django'`** | Install Django: `pip install django` and ensure your virtual environment is activated. |
| **Browser blocks camera access** | Use `http://127.0.0.1:8000` (localhost). Browsers require HTTPS for camera access on non-localhost origins. |
| **Black/blank video feed** | Check webcam permissions in your OS settings. On Windows: Settings → Privacy → Camera. |
| **Port already in use** | Use a different port: `python manage.py runserver 8080` |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Commit** your changes: `git commit -m "Add my feature"`
4. **Push** to the branch: `git push origin feature/my-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**AridoshikaZu103**

- GitHub: [@AridoshikaZu103](https://github.com/AridoshikaZu103)

---

<p align="center">
  Made with ❤️ using Django & OpenCV
</p>
