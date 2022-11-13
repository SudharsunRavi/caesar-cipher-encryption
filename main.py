alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(new_text,shift_amt,cipher_direc):
  final_text=""
  for letter in new_text:
    if letter in alphabet:
      old_pos=alphabet.index(letter)
      if direction=="encode":
        new_pos=old_pos+shift_amt
      if direction=="decode":
        new_pos=old_pos-shift_amt
      new_letter=alphabet[new_pos]
      final_text+=new_letter
    else:
      final_text += letter
    
  print("The encoded text is:",final_text)

to_continue=True
while to_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
  text = input("Type your message:").lower()
  shift = int(input("Type the shift number:"))
  shift=shift%26
  caesar_cipher(new_text=text, shift_amt=shift, cipher_direc=direction)
  continue1=input("To continue type 'yes' or type 'no' to exit:")
  if continue1=='no':
    print("Thank you")
    break

