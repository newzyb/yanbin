favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

coders = ["phil", "josh", "david", "becca", "sarah", "matt", "danielle"]
for coder in coders:
    if coder in favorite_languages:
        print(f"Thank you for taking the poll, {coder}! ")
    else:
        print(f"{coder}, what's your favorite programming language?")
