student=[
    {
        "name":"sumanth",
        "marks":[{"english":60,"science":70},{"eng":50,"mat":50}]
    },
    {
        "name": "sumanth",
        "marks": [{"english": 60, "science": 70}]
    }

]
for i in student:
    print(i["name"])
    for j in i["marks"]:
        print (j["english"])
