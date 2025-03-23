import os

# List of names in order
names = [
    "Aakash Rana", "Aarashi", "Aashika Bhandari", "Aashish Rokka", "Aashutosh Basnet",
    "Aayush Chaudhary", "Aayush Dhakal", "Aayushma Pandey", "Aayush Rijal", "Abhinash Guragain",
    "Aditya Thakuri", "Aman Shrestha", "Amrit Rai", "Anjan Lama", "Anshika Mishra",
    "Anuj Gyawali", "Anup Dhakal", "Arjun Sharma Poudel", "Ashok Budha", "Asmita Basnet",
    "Ayub Bantawa", "Bhawana Ojha", "Bikal Shrestha", "Bhargav Basnet", "Bhuwan Joshi",
    "Bibek Pandey", "Bibek Sapkota", "Bishal Lamichhane", "Bishal Regmi", "Bishwas Chaudhary",
    "Binod Lama", "Dipen Shrestha", "David Mandal", "Gaurav Maharjan", "Harikrishna Gautam",
    "Janak Chhatkuli", "Jayed Alam Mansur", "Jeken Maharjan", "Jibachh Yadav", "Jubin Khatri",
    "Karan Bista", "Kritesh Bhattarai", "Matina Maharjan", "Mohit Bhandari", "Mohit Rawal",
    "Mohan Karki", "Miraj Bhattarai", "Nabin Pandey", "Nabin Paudel", "Nayan Banskota",
    "Neesh Nepal", "Nisha Baruwal", "Nita Khatri", "Narayan Ghimire", "Niranjan Ghising",
    "Nishan Rayamajhi", "Nishk Bhattarai", "Om Joshi", "Parisha Shrestha", "Pankaj P",
    "Prabesh Khatiwada", "Prakash Bhattarai", "Prakash Mahara", "Prakashman Singh Thakuri",
    "Prasidda Khadka", "Pramod Bhattarai", "Pranaya Gurung", "Prashna Dhaulakoti", "Prince Maharjan",
    "Poshan Pokhrel", "Pukar Chalishe", "Raj Shrestha", "Rajan Gaihre", "Rajina Gurung",
    "Rijan Shrestha", "Roshan Sunuwar", "Riyana Ghimire", "Sabul Khatri", "Sabin Shrestha",
    "Sachin Acharya", "Sachin Chakradhar", "Sachin Serma", "Sachita Bhandari", "Sadiksha Timilsina",
    "Samyam Giri", "Samreshan Sahani", "Sajal Bista", "Sarthak Basnet", "Shambhu Kumar Kushwaha",
    "Shisir Puri", "Shraddha Tiwari", "Shristika Timalsina", "Shanna Aryal", "Sujal Manandhar",
    "Sujan Rai", "Sulakshan Chandra Ghimire", "Swarnima Kansakar", "Saurav G.C.", "Saurav Pachhai",
    "Subash Banstola", "Subin Satyal", "Sudip Budthapa", "Sudip Majkoti", "Sudarshan Pathak",
    "Sitish Kumar", "Sunita Dangol", "Sufal K.C.", "Santos Ghimire", "Sushil Koirala",
    "Ujjal Koirala", "Viraj Sawad", "Yash Shrestha"
]
files = [f for f in os.listdir() if f.startswith("Name (") and f.endswith(".png")]
files.sort(key=lambda x: int(x.split("(")[1].split(")")[0]))
for i, file in enumerate(files):
    if i < len(names):
        new_name = f"{names[i]}.png"
        os.rename(file, new_name)
        print(f'Renamed "{file}" → "{new_name}"')

print("Renaming complete!")
