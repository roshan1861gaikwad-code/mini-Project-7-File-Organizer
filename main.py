
from pathlib import Path
import shutil

# File extensions and their destination folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".html", ".css", ".js", ".json"]
}


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    # Check whether the folder exists
    if not folder.is_dir():
        print("Error: Folder does not exist!")
        return

    moved_count = 0

    # Examine the files in the selected folder
    for file in list(folder.iterdir()):
        if not file.is_file():
            continue

        # Find the matching category
        category = None

        for name, extensions in FILE_TYPES.items():
            if file.suffix.lower() in extensions:
                category = name
                break

        # Leave unsupported file types untouched
        if category is None:
            continue

        try:
            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file.name

            # Avoid overwriting an existing file
            if destination.exists():
                print(f"Skipped duplicate: {file.name}")
                continue

            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/")
            moved_count += 1

        except (OSError, shutil.Error) as error:
            print(f"Could not move {file.name}: {error}")

    print(f"\nOrganization complete! Files moved: {moved_count}")


if __name__ == "__main__":
    print("=== SMART FILE ORGANIZER ===")
    folder_path = input("Enter the folder path to organize: ")
    organize_files(folder_path)
