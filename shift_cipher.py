#Challenge 146 - Shift Code with Ascii and Save to File (no global) + read and decode

import os

def encode(text, shift_number):
  shifted_characters = []
  for letter in text:
    if letter.isalpha():
      if letter.isupper():
        shifted_index  = (((ord(letter) + shift_number) - 65) % 26) + 65
        shifted_letter = chr(shifted_index)
      else:
        shifted_index  = (((ord(letter) + shift_number) - 97) % 26) + 97
        shifted_letter = chr(shifted_index)
    else:
      shifted_letter = letter
    shifted_characters.append(shifted_letter)
    shifted_string = "".join(shifted_characters)
  print(shifted_string)
  return shifted_string

def decode(text, shift_number):
  shifted_characters = []
  for letter in text:
    if letter.isalpha():
      if letter.isupper():
        shifted_index = (((ord(letter) - shift_number) - 65) % 26) + 65
        shifted_letter = chr(shifted_index)
      else:
        shifted_index = (((ord(letter) - shift_number) - 97 ) % 26) + 97
        shifted_letter = chr(shifted_index)
    else:
      shifted_letter = letter
    shifted_characters.append(shifted_letter)
    shifted_string = "".join(shifted_characters)
  print(shifted_string)
  return shifted_string

def save_to_file(file_name, encoded_string):
  with open(file_name, "w") as file:
    file.write(encoded_string)

def read_file(file_name):
  with open(file_name, "r") as file:
    #print(file.read())
    return file.read()

def main():
  while True:
    print("""1) Make a code
2) Decode a Message
3) Read the file
4) Quit\n""")
    selection = int(input("Enter your selection: "))

    if selection == 1:
      text = input("Text: ")
      shift_number = int(input("Shift Number: "))
      encoded_string = encode(text, shift_number)
      save = input("Do you want to save the text? (Y/N)")
      if save == "Y":
        file_name = input("Please enter the name of the file: ")
        save_to_file(file_name, encoded_string)

    elif selection == 2:
      text = input("Text: ")
      shift_number = int(input("Shift Number: "))
      decode(text, shift_number)

    elif selection == 3:
      file_name = input("Please enter the name of the file: ")
      file_content = read_file(file_name)
      decode(file_content, shift_number)

    elif selection == 4:
      break

    else:
      print("Sorry only options 1,2 or 3 are valid.\n")

main()
