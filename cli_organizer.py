import os
import shutil
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("folder_name", help="name of folder", type=str)
args = parser.parse_args()

folder = f"./{args.folder_name}"

video_extensions = [
    "webm","mkv","flv","vob","ogv","ogg","mov",
    "avi","qt","wmv","rm","asf","amv","mp4",
    "m4p","m4v","mpg","mp2","mpeg","mpe","mpv",
    "svi","3gp","3g2","mxf","roq","nsv","f4v",
    "f4p","f4a","f4b","mod","mts","m2ts","ts"
]

document_extensions = [
    "txt","pdf","doc","docx","odt","rtf","xls","xlsx","ods",
    "csv","ppt","pptx","odp","html","htm","xml","json"
]

image_extensions = [
    "jpg","jpeg","png","gif","bmp","tiff","webp","avif"
]

dirs = {
    "VIDEOS": [],
    "IMAGES": [],
    "DOCUMENTS": [],
    "OTHERS": []
}

if not os.path.isdir(folder):
    print(f"Error! The folder {folder} does not exist.")
    exit()

files = os.listdir(folder)

for f in files:
    if f in dirs:
        continue
    full_path = os.path.join(folder, f)
    if not os.path.isfile(full_path):
        continue
    p = Path(full_path)
    extension = p.suffix
    if not extension:
        dirs["OTHERS"].append(full_path)
        continue
    e = extension[1:].lower()
    if e in video_extensions:
        dirs["VIDEOS"].append(full_path)
    elif e in image_extensions:
        dirs["IMAGES"].append(full_path)
    elif e in document_extensions:
        dirs["DOCUMENTS"].append(full_path)
    else:
        dirs["OTHERS"].append(full_path)

print("\nSummary:")
for category, fls in dirs.items():
    print(f"  {category:<10} : {len(fls)} files")

vid_dir = f"./{args.folder_name}/VIDEOS"
img_dir = f"./{args.folder_name}/IMAGES"
doc_dir = f"./{args.folder_name}/DOCUMENTS"
oth_dir = f"./{args.folder_name}/OTHERS"

os.makedirs(vid_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)
os.makedirs(doc_dir, exist_ok=True)
os.makedirs(oth_dir, exist_ok=True)

for category, fls in dirs.items():
    if category == "VIDEOS":
        for vid in fls:
            dest = os.path.join(vid_dir, os.path.basename(vid))
            if not os.path.exists(dest):
                shutil.move(vid, vid_dir)
    elif category == "IMAGES":
        for img in fls:
            dest = os.path.join(img_dir, os.path.basename(img))
            if not os.path.exists(dest):
                shutil.move(img, img_dir)
    elif category == "DOCUMENTS":
        for doc in fls:
            dest = os.path.join(doc_dir, os.path.basename(doc))
            if not os.path.exists(dest):
                shutil.move(doc, doc_dir)
    elif category == "OTHERS":
        for oth in fls:
            dest = os.path.join(oth_dir, os.path.basename(oth))
            if not os.path.exists(dest):
                shutil.move(oth, oth_dir)

print("\nDone! Files organized successfully.")
