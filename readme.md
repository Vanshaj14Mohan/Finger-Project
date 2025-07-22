# 🖐️ Finger Count Project (Right Hand Only)

This project is a **real-time finger counting system** using computer vision. Built with **OpenCV** and **MediaPipe**, it detects and counts fingers on the **right hand only**, and displays the result visually using overlay images and a dynamic interface.

It is inspired by a modular hand tracking system developed earlier and reuses a custom-built `HandTrackingModule.py` for precise hand landmark detection.

---

## 📸 Demo

<p align="center">
  <img src="Output/1.jpg" width="120"/>
  <img src="FingerImage/3.jpg" width="120"/>
  <img src="FingerImage/5.jpg" width="120"/>
</p>

---

## 📦 Project Structure

```

FingerCount/
│
├── FingerCount.py              # Main app for finger counting
├── HandTrackingModule.py       # Custom hand tracking class using MediaPipe
├── FingerImage/                # Overlay images for finger counts
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   └── 5.jpg

````

---

## 🧠 How It Works

1. The webcam captures live video.
2. `HandTrackingModule.py` detects hand landmarks using MediaPipe.
3. Finger tip landmarks (`id`s: 4, 8, 12, 16, 20) are used to detect if a finger is open or closed:
   - **Thumb detection** is based on `x`-axis comparison (right hand only).
   - **Other fingers** are detected using `y`-axis positioning.
4. Total number of extended fingers is calculated.
5. A corresponding image (e.g. `3.jpg` for 3 fingers) is displayed along with a number overlay.

---

## 📌 Features

- ✅ Real-time finger counting
- ✅ Uses a custom hand tracking module
- ✅ Displays corresponding overlay image
- ✅ FPS display for performance monitoring
- ❗ **Right hand only** (thumb detection is hardcoded for right-hand logic)

---

## 🔧 Requirements

- Python 3.x
- OpenCV
- MediaPipe

Install the required libraries with:

```bash
pip install opencv-python mediapipe
````

---

## 🚀 Getting Started

### 1. Clone or Download

```bash
git clone https://github.com/your-username/FingerCount.git
cd FingerCount
```

### 2. Place Finger Images

Add images named `0.jpg` to `5.jpg` in a folder called `FingerImage/`. Each image should visually represent the corresponding number of raised fingers.

### 3. Run the App

```bash
python FingerCount.py
```

Press `q` to quit the window.

---

## 📊 Landmark Reference (MediaPipe IDs)

```
Thumb   : 4
Index   : 8
Middle  : 12
Ring    : 16
Pinky   : 20
```

---

## 🚫 Limitations

* ❗ Only detects **right hand** (thumb detection won't work for the left hand).
* 🤚 One-hand detection only (no multi-hand support).
* 👀 Requires good lighting for optimal accuracy.

---

## 🧩 Future Improvements

* Left-hand detection logic
* Dual hand support
* Gesture recognition (like thumbs-up, peace, etc.)
* Voice output for finger count

---

## 👤 Author

**Made with ❤️ by Vanshaj P Mohan, a Data Science Enthusiast.**

