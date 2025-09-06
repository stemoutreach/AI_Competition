
#!/usr/bin/env python3
"""
OpenCV Image Capture for FTC Datasets
-------------------------------------
- Works with USB webcams / laptop cameras.
- Press 'c' to capture a frame, 'q' to quit.
- Saves images under datasets/raw/<label>/IMG_<timestamp>.jpg
- Also appends a manifest CSV with (filepath,label).

Usage:
  python capture_images_opencv.py --label pixel --outdir datasets/raw --camera 0 --width 640 --height 480

Tip: Create multiple labels (e.g., 'yellow', 'purple', 'background') and run
the script once per label.
"""
import argparse, os, time, csv
from pathlib import Path
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", type=str, default="object", help="class label for this session")
    ap.add_argument("--outdir", type=str, default="datasets/raw", help="root output directory")
    ap.add_argument("--camera", type=int, default=0, help="camera index (0 is default)")
    ap.add_argument("--width", type=int, default=640, help="capture width")
    ap.add_argument("--height", type=int, default=480, help="capture height")
    ap.add_argument("--max", type=int, default=0, help="optional max captures (0 = unlimited)")
    args = ap.parse_args()

    label_dir = Path(args.outdir) / args.label
    label_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = Path(args.outdir) / "manifest.csv"
    manifest_exists = manifest_path.exists()

    cap = cv2.VideoCapture(args.camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    if not cap.isOpened():
        raise SystemExit("ERROR: Could not open camera index %d" % args.camera)

    print("[INFO] Press 'c' to capture, 'q' to quit.")
    count = 0
    with open(manifest_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not manifest_exists:
            writer.writerow(["filepath","label","timestamp"])
        while True:
            ok, frame = cap.read()
            if not ok:
                print("[WARN] Failed to read frame")
                continue

            # overlay capture count and label
            overlay = frame.copy()
            cv2.putText(overlay, f"label: {args.label}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.putText(overlay, f"captured: {count}", (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.imshow("Capture (c=capture, q=quit)", overlay)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                ts = time.strftime("%Y%m%d_%H%M%S")
                fname = f"IMG_{ts}_{count:04d}.jpg"
                fpath = str(label_dir / fname)
                cv2.imwrite(fpath, frame)
                writer.writerow([fpath, args.label, ts])
                csvfile.flush()
                count += 1
                if args.max and count >= args.max:
                    print("[INFO] Reached max captures; exiting.")
                    break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[DONE] Saved {count} images to {label_dir}")
    print(f"[INFO] Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
