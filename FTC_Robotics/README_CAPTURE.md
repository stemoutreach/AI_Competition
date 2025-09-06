
# Image Capture for FTC ML Datasets

This folder includes two simple tools to help teams **collect images** for training and experimentation.

## Scripts

1. **capture_images_opencv.py** (USB webcams / laptop camera)
   ```bash
   python capture_images_opencv.py --label pixel --outdir datasets/raw --camera 0 --width 640 --height 480
   ```

2. **capture_images_picamera2.py** (Raspberry Pi Camera)
   ```bash
   # Install dependencies (Debian/Raspberry Pi OS)
   sudo apt update && sudo apt install -y python3-picamera2 python3-opencv
   python capture_images_picamera2.py --label pixel --outdir datasets/raw --width 1280 --height 720
   ```

**Controls:** `c` to capture, `q` to quit. Each capture writes a JPG and appends to `manifest.csv` with `(filepath,label,timestamp)`.

## Suggested Folder Structure

```
datasets/
  raw/
    yellow/
      IMG_....jpg
    purple/
      IMG_....jpg
    background/
      IMG_....jpg
  processed/
```

Collect each class separately by running the script with different `--label` values.

## Tips for Better Data
- Vary **lighting**, **distance**, **angles**, and **backgrounds**.
- Keep objects **in focus** and centered at capture time.
- Capture some **negatives** (backgrounds without the object).
- Aim for **balance** across labels (e.g., ~200–300 per class to start).

## Next Steps
- Use `datasets/raw/manifest.csv` to track what you've collected.
- For object **detection** (boxes), use a labeling tool later (e.g., CVAT/LabelImg), or start with the **FTC-ML** portal (video upload + built-in annotator).
- Convert trained models to `.tflite` for on-robot inference (see the workshop notebook for a TFLite example).
