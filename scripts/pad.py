import os
import cv2

folder = r"data/labeled/new_moderate"

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    img = cv2.imread(path)

    if img is None:
        continue

    padded = cv2.copyMakeBorder(
        img,
        top=0,
        bottom=0,
        left=77,
        right=78,
        borderType=cv2.BORDER_CONSTANT,
        value=(0, 0, 0)
    )

    cv2.imwrite(path, padded)  # overwrite

print("Done!")