# 👥 Multi-Face Emotion Detector

A real-time facial emotion recognition system that detects **multiple faces simultaneously** using OpenCV and analyzes their emotions using DeepFace.

---

## 📸 Live Demo

> Detects and labels emotions like **happy**, **sad**, **angry**, **neutral**, and more — in real-time via webcam!

![demo](screenshots/demo.gif) <!-- Optional: Add a GIF or image -->

---

## 🔍 Features

- 🎥 Real-time video stream from webcam
- 👨‍👩‍👧 Detects and analyzes **multiple faces at once**
- 🧠 Uses DeepFace to recognize emotions
- 📊 Displays a probability bar chart for detected emotions
- 🧱 Lightweight and easy to set up

---

## 🧠 Tech Stack

| Component  | Technology      |
|------------|-----------------|
| Face Detection | OpenCV + Haar Cascade |
| Emotion Analysis | DeepFace (Keras + TensorFlow) |
| Language | Python |
| Visualization | OpenCV Drawing Utilities |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multi-face-emotion-detector.git
cd multi-face-emotion-detector
````

### 2. Install Dependencies

We recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one with:

```
opencv-python
deepface
numpy
tensorflow
keras
```

### 3. Download Haar Cascade File

Make sure `haar_face.xml` is present in the project root. You can download it from:
[https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade\_frontalface\_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

Rename it as `haar_face.xml`.

### 4. Run the App

```bash
python main.py
```

Press `d` to quit the application window.

---

## 🖼️ Example Output

Detected faces and their emotions are displayed with labels and emotion bar graphs:

```
[🙂 Happy | 😡 Angry | 😢 Sad | 😐 Neutral]
```

Each face is outlined with a box, and their dominant emotion is labeled in real time.

---

## 📁 Project Structure

```
multi-face-emotion-detector/
├── multiple_live_face_detect.py             # Main application script
├── haar_face.xml       # Haar cascade for face detection
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Author
Shubham S 


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Acknowledgments

* [OpenCV](https://opencv.org/)
* [DeepFace](https://github.com/serengil/deepface)
* Inspired by real-world use cases in mood detection, classroom analytics, and sentiment-based feedback systems.

---



