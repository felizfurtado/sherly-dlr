# create_structure.py - Run this to create organized structure
import os
import shutil

def create_organized_structure():
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Create new directories
    directories = [
        'css',
        'js',
        'images',
        'images/icons',
        'images/gallery',
        'images/team',
        'images/logos',
        'fonts',
        'downloads'
    ]
    
    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)
    
    print("Created organized structure!")
    
    # Suggest moving files (you'll need to do this manually or with shutil)
    print("\nSuggested organization:")
    print("1. Move all HTML files to root (keep them there)")
    print("2. Move all CSS to /css folder")
    print("3. Create a main.css in /css")
    print("4. Move all images to appropriate /images subfolders")
    print("5. Extract assets.zip and organize contents")

if __name__ == "__main__":
    create_organized_structure()