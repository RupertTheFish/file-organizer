# 📁 File Organizer and Desorganizer

This repository provides two Python scripts:

- `in.py`: Automatically organizes files in a folder into subfolders based on their file types.
- `out.py`: Reverts the organization by moving files back to the root folder and deleting the subfolders.

---

## 📌 Features

### ✅ `in.py` — File Organizer

- Categorizes files by extension:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
  - **Documents**: `.txt`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
  - **PDFs**: `.pdf`
  - **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
  - **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`
  - **Archives**: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
  - **Others**: Everything else

- Skips `in.py` and `out.py` files to avoid recursion.
- Automatically creates folders if they do not exist.

### 🔁 `out.py` — File Desorganizer

- Moves all files from subfolders back to the main directory.
- Deletes the now-empty subdirectories.

---

## 🚀 Usage

### 📌 Prerequisites

- Python 3.x installed

### 🧪 Run the Organizer

```bash
python in.py
```
This will organize all files in the current working directory.

### 🔄 Run the Desorganizer
```
python out.py
```
This will revert the organization and move all files back to the root directory.

### 📂 Example

Before running in.py:
```
your-folder/
├── in.py
├── out.py
├── photo.jpg
├── document.pdf
├── music.mp3

After running in.py:

your-folder/
├── in.py
├── out.py
├── Images/
│   └── photo.jpg
├── Pdfs/
│   └── document.pdf
├── Audio/
│   └── music.mp3

After running out.py:

your-folder/
├── in.py
├── out.py
├── photo.jpg
├── document.pdf
├── music.mp3
```
### 🧼 Notes

    These scripts are designed to be run in the same folder where your files are located.

    It is safe to include these scripts in the folder — they will ignore themselves.

