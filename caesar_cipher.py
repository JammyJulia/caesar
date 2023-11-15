alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(text, rotation):  #Encode the text based on the rotation
  result = ""
  for char in text:  #For every character in text
    if (alphabet.find(char) == -1):  #If character is not in alphabet
      result += char
    else:  #If character is in alphabet
      result += (alphabet[(alphabet.find(char) + rotation) % len(alphabet)])
  return result


def decode(text, rotation):  #Decode the text based on the rotation
  result = ""
  for char in text:  #For every character in text
    if (alphabet.find(char) == -1):  #If character is not in alphabet
      result += char
    else:  #If character is in alphabet
      result += (alphabet[(alphabet.find(char) - rotation) % len(alphabet)])
  return result


welcome = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(welcome))

if mode == 1:  #If selected mode is "encrypt"
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encode(text, rotation))
elif mode == 2:  #If selected mode is "decrypt"
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decode(text, rotation))
elif mode == 3:  #If selected mode is "bruteforce"
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
