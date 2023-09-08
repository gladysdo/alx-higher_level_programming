#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences based on '.', '?', and ':'
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in ['.', '?', ':']:
            sentences.append(current_sentence.strip())  # Remove leading/trailing spaces
            current_sentence = ""

    # Add the last sentence
    if current_sentence:
        sentences.append(current_sentence.strip())

    # Print the sentences with two new lines after each separator
    for sentence in sentences:
        print(sentence)
        print()
