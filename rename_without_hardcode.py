import os
image_directory = r"C:\path\to\your\image\folder" # add the folder path where all your images are located
names_file = r"C:\path\to\your\image\folder\names.txt" # add the txt file with all the names 
with open(names_file, "r", encoding="utf-8") as file:
    names = [line.strip() for line in file.readlines() if line.strip()]
files = [f for f in os.listdir(image_directory) if f.startswith("Name (") and f.endswith(".png")]
files.sort(key=lambda x: int(x.split("(")[1].split(")")[0]))
if len(files) != len(names):
    print(f"Warning: Found {len(files)} images but {len(names)} names in the text file.")
    exit()

for i, file in enumerate(files):
    old_path = os.path.join(image_directory, file)
    new_name = f"{names[i]}.png"
    new_path = os.path.join(image_directory, new_name)

    os.rename(old_path, new_path)
    print(f'Renamed "{file}" → "{new_name}"')

print("Renaming complete!")
