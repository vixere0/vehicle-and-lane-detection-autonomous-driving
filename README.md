#  Vehicle & Lane Detection — Autonomous Driving

Real-time vehicle detection and tracking system using **YOLOv8** + **ByteTrack**. Detects and tracks cars, motorcycles, buses, and trucks from video input with FPS display, unique vehicle counting, and trail visualization.

---

##  Demo

> Run the script on a highway video to see bounding boxes, track trails, and live stats.

---

##  Features

- **YOLOv8** object detection (configurable model size)
- **ByteTrack** multi-object tracking
- Detects 4 vehicle classes: `car`, `motorcycle`, `bus`, `truck`
- Color-coded bounding boxes per class
- Motion trail visualization per tracked vehicle
- Live info panel: FPS, frame count, in-frame & total unique vehicles
- GPU (CUDA) support with automatic fallback to CPU
- Save output as `.mp4`

---

##  Installation

**1. Clone the repo**
```bash
git clone https://github.com/vixere0/vehicle-and-lane-detection-autonomous-driving.git
cd vehicle-and-lane-detection-autonomous-driving
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install ultralytics opencv-python torch
```

> For GPU support, install the appropriate [PyTorch CUDA version](https://pytorch.org/get-started/locally/).

---

##  Project Structure

```
vehicle-and-lane-detection-autonomous-driving/
├── data/
│   └── sample_videos/
│       └── highway.mp4         
├── src/
│   └── detect.py                
├── output.mp4                  
└── README.md
```

---

##  Usage

**Basic run (default video):**
```bash
python src/detect.py
```

**Custom video:**
```bash
python src/detect.py --video path/to/video.mp4
```

**Save output:**
```bash
python src/detect.py --video path/to/video.mp4 --save --output result.mp4
```

**All arguments:**

| Argument | Default | Description |
|---|---|---|
| `--video` | `data/sample_videos/highway.mp4` | Input video path |
| `--model` | `yolov8n.pt` | YOLO model weights |
| `--conf` | `0.50` | Confidence threshold |
| `--iou` | `0.45` | NMS IoU threshold |
| `--min-area` | `2500` | Min bounding box area (px²) |
| `--width` | `1280` | Display width |
| `--height` | `720` | Display height |
| `--save` | `False` | Save output video |
| `--no-show` | `False` | Disable live preview |
| `--output` | `output.mp4` | Output filename |

---

##  Class Colors

| Class | Color |
|---|---|
| Car | 🟢 Green |
| Motorcycle | 🟠 Orange |
| Bus | 🔵 Blue |
| Truck | 🔴 Red |

---

##  Requirements

- Python 3.8+
- PyTorch
- OpenCV
- Ultralytics (YOLOv8)

---

##  License

MIT License

