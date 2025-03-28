# Image Renaming Script

This script renames image files in a folder based on a list of names from a text file. The images are assumed to be named in the format `Name (X).png` where `X` is a number. The script will rename the images according to the names provided in the `names.txt` file.

## Requirements

- Python 3.x
- `os` module (built-in)

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/image-renaming-script.git
   cd image-renaming-script

2. Update the script with the correct paths to your image folder and the `names.txt` file:
- `image_directory` - The folder where your images are located.
- `names_file` - The text file containing the list of names to use for renaming.

- Example:
  ```bash
  image_directory = r"C:\path\to\your\image\folder"  # Update this path
   names_file = r"C:\path\to\your\image\folder\names.txt"  # Update this path
3. Ensure that your names.txt file contains one name per line. For example:
   ```bash
      Alice
      Bob
      Charlie
4. Run the Script
     ``` bash
         python rename_images.py
5. The script will rename the images in the specified directory according to the list of names in names.txt. If the number of images does not match the number of names, a warning will be displayed.
