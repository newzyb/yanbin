favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

names = ["jen", "hetingcan", "limingxin"]
for name, language in favorite_languages.items():
    if name in names:
        print(f"Thank {name}, you invite {language} poll.")
    else:
        print(f"Sorry {name}, we invite you take part in poll. ")
