def remove_whitespace_characters(text):
  translation_table = str.maketrans("", "", "\r\v\f")
  return text.translate(translation_table)