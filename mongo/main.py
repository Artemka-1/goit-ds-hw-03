from config import collection
from pymongo.errors import PyMongoError


def add_cat(name: str, age: int, features: list):
    """Create"""
    try:
        collection.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
        print("Кота додано ✅")
    except PyMongoError as e:
        print(f"Помилка: {e}")


def get_all_cats():
    """Read all"""
    try:
        for cat in collection.find():
            print(cat)
    except PyMongoError as e:
        print(f"Помилка: {e}")


def get_cat_by_name(name: str):
    """Read one"""
    try:
        cat = collection.find_one({"name": name})
        print(cat if cat else "Кота не знайдено ❌")
    except PyMongoError as e:
        print(f"Помилка: {e}")


def update_cat_age(name: str, age: int):
    """Update age"""
    try:
        result = collection.update_one(
            {"name": name},
            {"$set": {"age": age}}
        )
        print("Вік оновлено ✅" if result.modified_count else "Кота не знайдено ❌")
    except PyMongoError as e:
        print(f"Помилка: {e}")


def add_cat_feature(name: str, feature: str):
    """Update features"""
    try:
        result = collection.update_one(
            {"name": name},
            {"$push": {"features": feature}}
        )
        print("Характеристику додано ✅" if result.modified_count else "Кота не знайдено ❌")
    except PyMongoError as e:
        print(f"Помилка: {e}")


def delete_cat(name: str):
    """Delete one"""
    try:
        result = collection.delete_one({"name": name})
        print("Кота видалено ✅" if result.deleted_count else "Кота не знайдено ❌")
    except PyMongoError as e:
        print(f"Помилка: {e}")


def delete_all_cats():
    """Delete all"""
    try:
        collection.delete_many({})
        print("Всі записи видалено ⚠️")
    except PyMongoError as e:
        print(f"Помилка: {e}")
