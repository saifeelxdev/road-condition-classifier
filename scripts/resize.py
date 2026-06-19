import os
import cv2
import numpy as np

source_folder = r"data/labeled/moderate"
output_folder = r"data/labeled/new_moderate"

os.makedirs(output_folder, exist_ok=True)

target_w = 640
target_h = 360

for filename in os.listdir(source_folder):
    src_path = os.path.join(source_folder, filename)

    img = cv2.imread(src_path)

    if img is None:
        print(f"Skipping: {filename}")
        continue

    h, w = img.shape[:2]

    # Scale image while maintaining aspect ratio
    scale = min(target_w / w, target_h / h)

    new_w = int(w * scale)
    new_h = int(h * scale)

    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Create black canvas of target size
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)

    # Center the image
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2

    canvas[y_offset:y_offset + new_h,
           x_offset:x_offset + new_w] = resized

    dst_path = os.path.join(source_folder, filename)
    cv2.imwrite(dst_path, canvas)

    print(f"Processed: {filename}")

print("Done! All images saved in 'new_poor'")

