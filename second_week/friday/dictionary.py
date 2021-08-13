dictionary = {
    "name": "Hiskel K.",
    "location": "A.A",
    "height": 1.78,
    "hobbies": ["hobby a", "hobby b", "hobby c"],
    "parents": {
        "father": {
            "occupation": "string",
            "birth date": ""
        },
        "mother": {

        }
    }
}

dictionary["parents"]["father"]["occupation"] = "Pilot"
dictionary["hobbies"].append("hobby d")

print(dictionary)

grades = [[1, 2, 3], [1, 2, 5]]

grades = [
    {"biology": 55, "physics": 33, "chemistry": 47},
    {"biology": 78, "physics": 23, "chemistry": 77},
    {"biology": 44, "physics": 44, "chemistry": 56},
]
