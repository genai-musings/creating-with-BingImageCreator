import os
from BingImageCreator import ImageGen

class bingImageGen:
    def __init__(self, bing_key, debug_file="./debug.log"):
        """
        Initializes an instance of bingImageGEn.

        Args:
            bing_key (str): Bing API key for image generation.
            debug_file (str, optional): Path to the debug file. Defaults to "./debug.log".
        """
        self.image_generator = ImageGen(bing_key, debug_file)

    def generate_images(self, prompt, output_dir="output", download_count=4):
        """
        Generates and saves images based on the provided prompt.

        Args:
            prompt (str): Prompt for image generation.
            output_dir (str): Path to the output directory to save the generated images.
            download_count (int, optional): Number of images to download. Defaults to 4.
        """
        if not prompt:
            return  # Skip image download when prompt is empty
        images = self.image_generator.get_images(prompt)
        self.image_generator.save_images(images, output_dir=output_dir, download_count=download_count)
