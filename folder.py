import os

def print_directory_structure(startpath, max_depth=None, exclude_dirs=None, exclude_ext=None):
    """
    Print directory structure in a tree-like format.
    
    Args:
        startpath: Root directory to start from
        max_depth: Maximum depth to traverse (None for unlimited)
        exclude_dirs: List of directory names to exclude
        exclude_ext: List of file extensions to exclude
    """
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'node_modules', '.venv', 'venv']
    if exclude_ext is None:
        exclude_ext = ['.pyc']
    
    print(f"Project Structure: {os.path.abspath(startpath)}")
    print("=" * 50)
    
    for root, dirs, files in os.walk(startpath):
        # Calculate current depth
        level = root.replace(startpath, '').count(os.sep)
        
        # Skip if beyond max depth
        if max_depth is not None and level > max_depth:
            continue
        
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Filter out files with excluded extensions
        files = [f for f in files if not any(f.endswith(ext) for ext in exclude_ext)]
        
        # Skip empty directories at this level
        if not dirs and not files and level > 0:
            continue
        
        # Print directory
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        print(f"{indent}{os.path.basename(root)}/")
        
        # Print files
        sub_indent = '│   ' * level + '├── '
        for i, f in enumerate(sorted(files)):
            # Different connector for last item
            if i == len(files) - 1 and not dirs:
                sub_indent = '│   ' * level + '└── '
            print(f"{sub_indent}{f}")

def get_project_summary(startpath):
    """Get summary statistics about the project."""
    html_count = css_count = js_count = img_count = other_count = 0
    total_size = 0
    
    for root, dirs, files in os.walk(startpath):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                total_size += os.path.getsize(filepath)
            except OSError:
                pass
            
            ext = os.path.splitext(file)[1].lower()
            if ext == '.html':
                html_count += 1
            elif ext == '.css':
                css_count += 1
            elif ext == '.js':
                js_count += 1
            elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp']:
                img_count += 1
            else:
                other_count += 1
    
    return {
        'html_files': html_count,
        'css_files': css_count,
        'js_files': js_count,
        'image_files': img_count,
        'other_files': other_count,
        'total_size_mb': total_size / (1024 * 1024)
    }

if __name__ == "__main__":
    # Get the current directory or specify your project path
    project_path = input("Enter project path (or press Enter for current directory): ").strip()
    
    if not project_path:
        project_path = "."
    
    if not os.path.exists(project_path):
        print(f"Error: Path '{project_path}' does not exist!")
        exit(1)
    
    print("\n" + "=" * 50)
    print_directory_structure(project_path)
    print("=" * 50)
    
    # Print summary
    summary = get_project_summary(project_path)
    print("\nProject Summary:")
    print(f"HTML files: {summary['html_files']}")
    print(f"CSS files: {summary['css_files']}")
    print(f"JavaScript files: {summary['js_files']}")
    print(f"Image files: {summary['image_files']}")
    print(f"Other files: {summary['other_files']}")
    print(f"Total size: {summary['total_size_mb']:.2f} MB")
    
    # Save to file option
    save_to_file = input("\nSave structure to file? (y/n): ").strip().lower()
    if save_to_file == 'y':
        with open('project_structure.txt', 'w', encoding='utf-8') as f:
            import sys
            original_stdout = sys.stdout
            sys.stdout = f
            print_directory_structure(project_path)
            sys.stdout = original_stdout
        print("Structure saved to 'project_structure.txt'")