import os, shutil

FOLDERS = {
    "images"    : [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "videos"    : [".mp4", ".mkv", ".avi", ".mov"],
    "documents" : [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "audio"     : [".mp3", ".wav", ".flac"],
    "code"      : [".py", ".js", ".html", ".css", ".json"],
    "archives"  : [".zip", ".rar", ".tar", ".gz"],
}


def file_organizer(folder_path: str):
    """move and categorize desktop files such as pdf jpg mp3 docx into dedicated subfolders by their file extension type"""
    try:
        for file in os.listdir(folder_path):
            filepath = os.path.join(folder_path, file)
            if os.path.isfile(filepath):
                ext = os.path.splitext(file)[1].lower()
                for folder , extensions in FOLDERS.items():
                    if ext in extensions:
                        dest = os.path.join(folder_path, folder)
                        os.makedirs(dest, exist_ok=True)
                        shutil.move(filepath, dest)
                        break
        return f"> Files organized in {folder_path}"
    except Exception as e:
        return f"> File organizer failed: {str(e)}"