import os

# Specify the directory where the images are stored
image_directory = r"C:\path\to\your\image\folder"  # Change this to your actual folder path
names_file = r"C:\path\to\your\image\folder\names.txt"  # Change this to the actual path of your names.txt file

# Read names from the text file
with open(names_file, "r", encoding="utf-8") as file:
    names = [line.strip() for line in file.readlines() if line.strip()]

# Get all image files matching the format "Name (X).png"
files = [f for f in os.listdir(image_directory) if f.startswith("Name (") and f.endswith(".png")]

# Sort files numerically based on the number inside parentheses
files.sort(key=lambda x: int(x.split("(")[1].split(")")[0]))

# Ensure we have the same number of names as files
if len(files) != len(names):
    print(f"Warning: Found {len(files)} images but {len(names)} names in the text file.")
    exit()

# Rename files
for i, file in enumerate(files):
    old_path = os.path.join(image_directory, file)
    new_name = f"{names[i]}.png"
    new_path = os.path.join(image_directory, new_name)

    os.rename(old_path, new_path)
    print(f'Renamed "{file}" → "{new_name}"')

print("Renaming complete!")
