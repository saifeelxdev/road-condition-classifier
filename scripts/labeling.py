import os
import cv2
import shutil

folder = r"data/New Data/sih_road_dataset/very_poor"
files = sorted(os.listdir(folder), reverse=True)

new_folder = r"data/New Data/sih_road_dataset/new_poor"
good_road = r"data/labeled/good"
moderate_road = r"data/labeled/moderate"
poor_road = r"data/labeled/poor"

for i, filename in enumerate(files):

    print(f"{i+1}/{len(files)}")
    print(f"GOOD --> {len(os.listdir(good_road))}")
    print(f"MODERATE --> {len(os.listdir(moderate_road))}")
    print(f"POOR --> {len(os.listdir(poor_road))}")
    path = os.path.join(folder, filename)

    img = cv2.imread(path)

    cv2.imshow("Road labeler", img)

    
    key = cv2.waitKey(0)
   

    if key == ord('q'):
        print("Task terminated")
        break

    elif key == ord('s'):
        continue

    elif key == ord('g'):
        if not os.path.exists(os.path.join(good_road, filename)):
            shutil.copy2(path, good_road)
    
    elif key == ord('m'):
        if not os.path.exists(os.path.join(moderate_road, filename)):
            shutil.copy2(path, moderate_road)

    elif key == ord('p'):
        if not os.path.exists(os.path.join(poor_road, filename)):
            shutil.copy2(path, poor_road)

    os.system('cls')
cv2.destroyAllWindows()

        
