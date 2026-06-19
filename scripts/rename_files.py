import os

folder = r"C:\Users\ASUS\Desktop\Image Data\images"

files = sorted(os.listdir(folder))

new_folder = r"C:\Users\ASUS\Desktop\Road Classification Project\data\raw"

for i, filename in enumerate(files, start=1):

    old_path = os.path.join(folder, filename)

    ext = os.path.splitext(filename)[1]

    new_name = f"road_img_{i:04d}{ext}"

    new_path = os.path.join(new_folder, new_name)

    os.rename(old_path, new_path)

print("Rename succesfully completed")