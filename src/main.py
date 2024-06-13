import os
import shutil

from copystatic import copy_static_to_public_directory
from gencontent import generate_page

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files to public directory...")
    copy_static_to_public_directory(static_dir, public_dir)
    
    print("Generating page...")
    generate_page(
        os.path.join(content_dir, "index.md"),
        template_path,
        os.path.join(public_dir, "index.html")
    )


        

main()