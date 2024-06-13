from textnode import TextNode
import shutil
from copystatic import copy_static_to_public_directory

def main():
    static = "/home/tyler/workspace/github.com/tylergreg95/static-site-generator/static"
    public = "/home/tyler/workspace/github.com/tylergreg95/static-site-generator/public"

    try:
        shutil.rmtree(public)
        print(f"{public} successfully deleted")
    except Exception:
        print("public directory does not exist")

    copy_static_to_public_directory(static, public)




        

main()