import shutil
from pathlib import Path

# This is folder path
downloads_path = Path.home() / "Downloads"


# File types and their extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".md", ".pages"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Installers": [".exe", ".dmg", ".msi"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Iterate over files in the downloads folder
for file in downloads_path.iterdir():
    if file.is_file():
        file_ext = file.suffix.lower()
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = downloads_path / folder_name
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_folder / file.name))
                print(f"[MOVED] Przeniesiono '{file.name}' do '{folder_name}'")
                break
        else:
            print(f"[INFO] Plik '{file.name}' nie pasuje do żadnej kategorii")
