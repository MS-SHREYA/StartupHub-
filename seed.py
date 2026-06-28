from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
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

# Insert into MongoDB
startups_collection.insert_many(startups)

print("Startup data inserted successfully!")