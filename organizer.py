import os
import shutil

# ----------- STEP 1: Choose folder to organize -----------
folder_path = input("Enter the folder path you want to organize: ").strip()

# Check if folder exists
if not os.path.exists(folder_path):
    print("❌ Folder does not exist! Please check the path again.")
    exit()

# ----------- STEP 2: File type categories -----------
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

# ----------- STEP 3: Create folders if not exist -----------
for category in file_types.keys():
    category_path = os.path.join(folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# ----------- STEP 4: Organize the files -----------
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders created by us
    if os.path.isdir(file_path):
        continue

    file_ext = os.path.splitext(file)[1].lower()
    moved = False

    for category, extensions in file_types.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(folder_path, category, file))
            print(f"Moved: {file} --> {category}")
            moved = True
            break

    # If no match → move to Others
    if not moved:
        shutil.move(file_path, os.path.join(folder_path, "Others", file))
        print(f"Moved: {file} --> Others")

print("\n All files organized successfully!")