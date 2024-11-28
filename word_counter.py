text = input("Enter Your Text: ")

text_chars = len(text)
text_words = len(text.split())
text_sentences = text.count(".")

print(f"Your text has {text_chars} characters, {text_words} words and {text_sentences} sentences ")