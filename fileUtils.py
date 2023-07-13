"""fileUtils class."""
import os

def replace_directory(output_dir):
    """
    Replaces a directory and its contents.

    Args:
        output_dir (str): The path to the directory to be replaced.

    Returns:
        bool: True if the directory is replaced, False otherwise.
    """
    # Check if the directory exists and is a valid directory
    if os.path.exists(output_dir) and os.path.isdir(output_dir):
        # Prompt the user for confirmation to replace the directory
        response = input(f"Output directory '{output_dir}' already exists. Do you want to replace it and its contents? (y/n): ")

        # If the user agrees to replace the directory
        if response.lower() == "y":
            print("Replacing...")

            # Remove the existing directory and its contents
            for root, dirs, files in os.walk(output_dir, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)  # Remove files within the directory
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    os.rmdir(dir_path)  # Remove subdirectories within the directory
            os.rmdir(output_dir)  # Remove the directory itself

            return True  # Replaced directory

    return False  # Directory not replaced

