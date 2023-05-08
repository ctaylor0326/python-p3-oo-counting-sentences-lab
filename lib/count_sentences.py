#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == (str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    basic_string = self.value.replace("?", ".").replace("!", ".").replace(",", "")
    sentence_list = []
    for sentence in basic_string.split("."):
        if sentence != "":
          sentence_list.append(sentence)
    return len(sentence_list)
  
  
  value = property(get_value, set_value)