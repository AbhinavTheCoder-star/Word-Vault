from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["wordvault"]
collection = db["words"]


def check(check_word):
    
    def check(word_lower):
        word_check = collection.find_one({"word_lower": word_lower})
        return word_check



def add_word(word, meaning, example):
    
    check_word = word.strip().lower()
    check_function = check(check_word)
    document = {
            "word": word,
            "meaning": meaning,
            "example":example,
            "word_lower": word.strip().lower()
            }

    if check_function:
       return True
    else:
        collection.insert_one(document)
        return False

         

# Function to search for word

def get_word(word):
    return collection.find_one({"word":word}, {"_id": 0, "word_lower":0})

def view_words():
    return list(collection.find().sort("word_lower", 1))

def update_word(word, meaning, example):
    word_lower = word.strip().lower()

    result = collection.find_one({"word_lower": word_lower})
    if result:
        collection.update_one(
            {"word_lower" : word_lower},
            {"$set": {"meaning": meaning, "example": example}}
        )


def delete_word(word):
    word_lower = word.strip().lower()
    result = collection.delete_one({"word_lower": word_lower})

    if result.deleted_count > 0:
        return True
    else:
        return False