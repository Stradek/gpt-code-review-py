def remove_whitespace_characters(text):
  translation_table = str.maketrans("", "", "\n\t\r\v\f")
  return text.translate(translation_table)