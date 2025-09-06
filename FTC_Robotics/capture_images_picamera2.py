
#!/usr/bin/env python3
"""
PiCamera2 Image Capture for FTC Datasets
----------------------------------------
- Uses the Raspberry Pi Camera via picamera2.
- Press 'c' to capture a frame, 'q' to quit.
- Saves images under datasets/raw/<label>/IMG_<timestamp>.jpg
- Also appends a manifest CSV with (filepath,label).

Install:
  sudo apt update && sudo apt install -y python3-picamera2

Run:
  python capture_images_picamera2.py --label pixel --outdir datasets/raw --width 1280 --height 720
"""
import argparse, time, csv
from pathlib import Path

try:
    from picamera2 import Picamera2, Preview
    import cv2
except Exception as e:
    raise SystemExit("PiCamera2 or OpenCV not available. Install with: sudo apt install -y python3-picamera2 python3-opencv\n" + str(e))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", type=str, default="object", help="class label for this session")
    ap.add_argument("--outdir", type=str, default="datasets/raw", help="root output directory")
    ap.add_argument("--width", type=int, default=1280, help="capture width")
    ap.add_argument("--height", type=int, default=720, help="capture height")
    ap.add_argument("--max", type=int, default=0, help="optional max captures (0 = unlimited)")
    args = ap.parse_args()

    label_dir = Path(args.outdir) / args.label
    label_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = Path(args.outdir) / "manifest.csv"
    manifest_exists = manifest_path.exists()

    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (args.width, args.height)})
    picam2.configure(config)
    picam2.start()

    print("[INFO] Press 'c' to capture, 'q' to quit.")
    count = 0
    with open(manifest_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not manifest_exists:
            writer.writerow(["filepath","label","timestamp"])
        while True:
            frame = picam2.capture_array()
            overlay = frame.copy()
            import cv2
            cv2.putText(overlay, f"label: {args.label}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.putText(overlay, f"captured: {count}", (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.imshow("PiCam2 Capture (c=capture, q=quit)", overlay)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                ts = time.strftime("%Y%m%d_%H%M%S")
                fname = f"IMG_{ts}_{count:04d}.jpg"
                fpath = str(label_dir / fname)
                # Save the original frame (no overlay)
                cv2.imwrite(fpath, frame)
                writer.writerow([fpath, args.label, ts])
                csvfile.flush()
                count += 1
                if args.max and count >= args.max:
                    print("[INFO] Reached max captures; exiting.")
                    break

    picam2.stop()
    cv2.destroyAllWindows()
    print(f"[DONE] Saved {count} images to {label_dir}")
    print(f"[INFO] Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
