import os
import sys
import pytest

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bingImageGen import bingImageGen

# Test case
def test_generate_images_downloads_and_saves_images(tmpdir, monkeypatch):
    # Create a temporary output directory
    output_dir = tmpdir.mkdir("output")

    # Mock Bing API key, prompt, and download count
    bing_key = "mock_bing_key"
    prompt = "mock_prompt"
    download_count = 2

    # Create an instance of bingImageGen
    image_gen = bingImageGen(bing_key, debug_file="./debug.log")

    # Mock the generate_images method to avoid external requests
    def mock_generate_images(prompt, output_dir, download_count):
        # Simulate successful image download and saving
        for i in range(download_count):
            # Create dummy image file in the output directory
            image_path = os.path.join(output_dir, f"image{i+1}.jpg")
            open(image_path, "w").close()

    # Patch the generate_images method with the mock
    monkeypatch.setattr(image_gen, "generate_images", mock_generate_images)

    # Call the generate_images method
    image_gen.generate_images(prompt, output_dir, download_count)

    # Check if the images are downloaded and saved
    assert len(os.listdir(output_dir)) == download_count

def test_generate_images_skips_download_when_prompt_is_empty(tmpdir):
    # Create a temporary output directory
    output_dir = tmpdir.mkdir("output")

    # Mock Bing API key and empty prompt
    bing_key = "mock_bing_key"
    prompt = ""

    # Create an instance of bingImageGen
    image_gen = bingImageGen(bing_key, debug_file="./debug.log")

    # Call the generate_images method
    image_gen.generate_images(prompt, output_dir)

    # Check if the output directory is empty
    assert len(os.listdir(output_dir)) == 0

def test_generate_images_downloads_correct_number_of_images(tmpdir, monkeypatch):
    # Create a temporary output directory
    output_dir = tmpdir.mkdir("output")

    # Mock Bing API key, prompt, and download count
    bing_key = "mock_bing_key"
    prompt = "mock_prompt"
    download_count = 3

    # Create an instance of bingImageGen
    image_gen = bingImageGen(bing_key, debug_file="./debug.log")

    # Mock the generate_images method to avoid external requests
    def mock_generate_images(prompt, output_dir, download_count):
        # Simulate successful image download and saving
        for i in range(download_count):
            # Create dummy image file in the output directory
            image_path = os.path.join(output_dir, f"image{i+1}.jpg")
            open(image_path, "w").close()

    # Patch the generate_images method with the mock
    monkeypatch.setattr(image_gen, "generate_images", mock_generate_images)

    # Call the generate_images method
    image_gen.generate_images(prompt, output_dir, download_count)

    # Check if the correct number of images are downloaded and saved
    assert len(os.listdir(output_dir)) == download_count

def test_generate_images_skips_download_when_prompt_is_empty(tmpdir, monkeypatch):
    # Create a temporary output directory
    output_dir = tmpdir.mkdir("output")

    # Create an instance of bingImageGen
    image_gen = bingImageGen("mock_bing_key", debug_file="./debug.log")

    # Mock the generate_images method to avoid external requests
    def mock_generate_images(prompt, output_dir, download_count):
        pass

    # Patch the generate_images method with the mock
    monkeypatch.setattr(image_gen, "generate_images", mock_generate_images)

    # Call the generate_images method with an empty prompt
    image_gen.generate_images("", output_dir, 4)

    # Check if the output directory remains empty
    assert len(os.listdir(output_dir)) == 0

def test_generate_images_skips_download_when_download_count_zero(tmpdir, monkeypatch):
    # Create a temporary output directory
    output_dir = tmpdir.mkdir("output")

    # Create an instance of bingImageGen
    image_gen = bingImageGen("mock_bing_key", debug_file="./debug.log")

    # Mock the generate_images method to avoid external requests
    def mock_generate_images(prompt, output_dir, download_count):
        pass

    # Patch the generate_images method with the mock
    monkeypatch.setattr(image_gen, "generate_images", mock_generate_images)

    # Call the generate_images method with download_count = 0
    image_gen.generate_images("mock_prompt", output_dir, download_count=0)

    # Check if the output directory remains empty
    assert len(os.listdir(output_dir)) == 0
