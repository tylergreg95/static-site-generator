import os, shutil

def copy_static_to_public_directory(static_path, public_path):
    if not os.path.exists(static_path):
        return ValueError(f"No such directory: {static_path}")
    if not os.path.exists(public_path):
        os.mkdir(public_path)
    static_contents = os.listdir(static_path)
    for file in static_contents:
        path = os.path.join(static_path, file)
        if os.path.isdir(path):
            os.mkdir(os.path.join(public_path, file))
            print(f"Copying: {static_path}/{file}/")
            if len(os.listdir(os.path.join(static_path, file))) > 0:
                copy_static_to_public_directory(os.path.join(static_path, file), os.path.join(public_path, file))
        if os.path.isfile(path):
            shutil.copy(path, os.path.join(public_path, file))
            print(f"Copying: {static_path}/{file}")