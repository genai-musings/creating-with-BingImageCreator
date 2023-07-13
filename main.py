"""main program entry point"""
import argparse
import os
import logging

from bingImageGen import bingImageGen
from fileUtils import replace_directory

def main():

    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    # Create an ArgumentParser instance
    parser = argparse.ArgumentParser(description='Script for generating and saving images using Bing Image Creator.')

    parser.add_argument('-o', '--output_dir', type=str, default="output", help='Path to the output directory')
    parser.add_argument('-d', '--download_count', type=int, default=4, help='Number of images to download')

    # Parse the command-line arguments
    args = parser.parse_args()

    while True:
        # Prompt for the image description
        print ("\n\nEnter a description of the image you want to generate?")
        print ("Leave input empty and press 'Return' to exit.\n\n")
        prompt = str(input())

        if prompt == "":
            break

        try:

            output_dir = os.path.join(os.getcwd(), args.output_dir)

            if os.path.exists(output_dir) and replace_directory(output_dir) == False:
                print("Exiting...")
                exit()

            # Instantiate the bingImageGen class
            image_generator = bingImageGen(os.getenv('BING_KEY'), debug_file="./debug.log")
            # Generate and save the images
            image_generator.generate_images(prompt, output_dir, args.download_count)

            print("Images generated to ./" + output_dir + "")

        except Exception as exp:
            # Handle the exception
            # Log the error message and exception type
            logging.error(f"Error: {exp}", exc_info=True)
            print("An error occurred, please try again.")

if __name__ == "__main__":
    main()
