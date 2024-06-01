alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(text,shiftNum):
#     cipher_text=""
#     for i in text:
#         pos=alphabet.index(i)
#         newPos=pos+shiftNum
#         cipher_text+=alphabet[newPos]
#     print(f"your text is : {cipher_text}")

# def decrypt(text,shiftNum):
#     orginalText=""
#     for i in text:
#         pos=alphabet.index(i)
#         newPos=pos-shift
#         orginalText+=alphabet[newPos]
#     print(f"Your message is : {orginalText}")

# if(dir=="encode"):
#     encrypt(text,shift)
# elif (dir=="decode"):
#     decrypt(text,shift)
# else:
#     print("Invalid Direction")

def caesar(text,shift,dir):
    end_text=""
    if(dir=="decode"):
        shift*=-1
    for letter in text:
        if(letter in alphabet):
            pos=alphabet.index(letter)
            newPos=pos+shift
            end_text+=alphabet[newPos]
        else:
            end_text+=letter
    print(f"Your New text Is {end_text}")

flag=True
while flag:

    dir=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("type your message:\n").lower()
    shift=int(input("Type the Shift Number: \n"))

#if shift input is very large
    shift%=25

    caesar(text,shift,dir)
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if(result=="no"):
        flag=False
        print("GoodBye")

