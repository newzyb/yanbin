favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

names = ["jen", "hetingcan", "limingxin"]
for name in favorite_languages:
    if name in names:
        language = favorite_languages[name]
        print(f"{name}, thank you take part in {language} poll.")
    else:
        print(f"Sorry {name}, we invite you this poll.")
