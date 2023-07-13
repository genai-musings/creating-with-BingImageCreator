import os
import sys

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fileUtils import replace_directory

def test_replace_directory_replaces_existing_directory(tmpdir, monkeypatch):
    # Create a temporary directory
    existing_dir = tmpdir.mkdir("existing_dir")

    # Create some files and subdirectories within the existing directory
    existing_dir.join("file1.txt").write("File 1")
    existing_dir.join("file2.txt").write("File 2")
    existing_dir.mkdir("subdir")

    # Mock user input to simulate agreeing to replace the directory
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    # Call the replace_directory function
    result = replace_directory(existing_dir)

    # Assert that the directory is replaced
    assert result is True
    assert not existing_dir.exists()

def test_replace_directory_skips_nonexistent_directory(tmpdir, monkeypatch):
    # Do not create a temporary directory

    # Mock user input to simulate agreeing to replace the directory
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    # Call the replace_directory function with a non-existent directory
    directory_path = os.path.join(tmpdir, "new_dir")
    result = replace_directory(directory_path)

    # Assert that the directory is not replaced
    assert result is False


def test_replace_directory_skips_non_directory(tmpdir, monkeypatch):
    # Create a temporary file
    file_path = tmpdir.join("file.txt")
    file_path.write("Test file")

    # Mock user input to simulate agreeing to replace the directory
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    # Call the replace_directory function with a file path
    result = replace_directory(str(file_path))

    # Assert that the file path is not replaced
    assert result is False
    assert file_path.exists()
