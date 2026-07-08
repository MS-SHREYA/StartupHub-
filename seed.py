import os
from pymongo import MongoClient

# 1. Grab your Atlas link from Render's environment, or fallback to it directly
# Replace the string below with your real Atlas connection string if running locally on your PC!
MONGO_URI = os.getenv(
    "MONGO_URI", 
    "mongodb+srv://sujithak2020_db_user:MCMsX0ct2dCyiLPE@cluster0.mucs16r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# 2. Connect using the Atlas connection link
client = MongoClient(MONGO_URI)

# Make sure it targets the correct database inside your Atlas cluster
db = client["startuphub"]
startups_collection = db["startups"]

# Delete old startup data (optional)
startups_collection.delete_many({})

# Sample startup data
startups = [
    {
        "startup_name": "HealthAI",
        "description": "AI-based healthcare platform for disease prediction and online consultation.",
        "required_skill": "Python",
        "video_link": "https://www.youtube.com/embed/putoJzHheAE"
    },
    {
        "startup_name": "TravelMate",
        "description": "Smart travel recommendation system.",
        "required_skill": "Frontend",
        "video_link": "https://www.youtube.com/embed/qYNweeDHiyU"
    },
    {
        "startup_name": "EduTech",
        "description": "Online learning platform for students.",
        "required_skill": "Java",
        "video_link": "https://www.youtube.com/embed/ezbJwaLmOeM"
    },
    {
        "startup_name": "FoodExpress",
        "description": "Food delivery application.",
        "required_skill": "Flutter",
        "video_link": "https://www.youtube.com/embed/1icn0OcalkA"
    },
    {
        "startup_name": "FinanceTrack",
        "description": "Personal finance and expense tracker.",
        "required_skill": "React",
        "video_link": "https://www.youtube.com/embed/-EoNrg_DR3s"
    },
    {
        "startup_name": "AgroSmart",
        "description": "AI-based agriculture monitoring platform.",
        "required_skill": "Machine Learning",
        "video_link": "https://www.youtube.com/embed/GmkH-SQMxCs"
    },
    {
        "startup_name": "CareerConnect",
        "description": "Job and internship portal for students.",
        "required_skill": "Python",
        "video_link": "https://www.youtube.com/embed/d_4UD6YEYa8"
    },
    {
        "startup_name": "ShopEase",
        "description": "E-commerce platform.",
        "required_skill": "PHP",
        "video_link": "https://www.youtube.com/embed/fJIsgON3RuM"
    },
    {
        "startup_name": "EventHub",
        "description": "Event management and ticket booking website.",
        "required_skill": "Node.js",
        "video_link": "https://www.youtube.com/embed/Ybz1mQZ2yzQ"
    },
    {
        "startup_name": "FitLife",
        "description": "Fitness and health tracking application.",
        "required_skill": "Android",
        "video_link": "https://www.youtube.com/embed/2zoEo8VgRC8"
    }
]

# Insert into MongoDB Atlas
startups_collection.insert_many(startups)

print("Startup data successfully injected into MongoDB Atlas cloud!")