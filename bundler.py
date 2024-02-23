#! /usr/bin/env python

import os
import zipfile

ZIP_FILE_PATH = "upload.zip"
MODEL_FILES_PATH = "model_files"


def main():
    print("Preparing ZIP archive...")
    with zipfile.ZipFile(ZIP_FILE_PATH, "w") as zip_file:
        zip_file.write("runner.py")
        zip_file.write("modeler-requirements.txt")
        for root, dirs, files in os.walk(MODEL_FILES_PATH):
            for file in files:
                zip_file.write(
                    os.path.join(root, file),
                    os.path.relpath(
                        os.path.join(root, file), os.path.join(MODEL_FILES_PATH, "..")
                    ),
                )
    print("ZIP archive created.")


if __name__ == "__main__":
    main()
