from xkcdpass import xkcd_password

# Fill all the necessary info below:

# Token of your bot (get from @BotFather)
token = ""

# Path to JSON file with all data (relative to project root)
db_file = "data/database/database.json"

# Path to list of words used to generate passwords (relative to project root)
words_file = "wrds.txt"

# Minimum/maximum allowed words in password
words_min = 2
words_max = 8

# Do not edit this value!
wordlist = xkcd_password.generate_wordlist(wordfile=words_file, min_length=4, max_length=10, valid_chars="[a-z]")
