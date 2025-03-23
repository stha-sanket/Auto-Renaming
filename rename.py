import os

# List of names in order
names = [
    "list names", "here"
]
files = [f for f in os.listdir() if f.startswith("Name (") and f.endswith(".png")]
files.sort(key=lambda x: int(x.split("(")[1].split(")")[0]))
for i, file in enumerate(files):
    if i < len(names):
        new_name = f"{names[i]}.png"
        os.rename(file, new_name)
        print(f'Renamed "{file}" → "{new_name}"')

print("Renaming complete!")
