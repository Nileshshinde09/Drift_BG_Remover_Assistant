import os
def list_jpeg_files(folder_path):
    jpeg_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            jpeg_files.append(file)
    return jpeg_files