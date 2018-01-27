#ROT 13 Python Implementation Lachlan Page 

def encode_rot13(text):
    result = ""
    for letter in text:
        shifted_letter = chr(ord(letter)+13)
        result += shifted_letter
    return result 

def decode_rot13(text):
    result = ""
    for letter in text:
        shifted_letter = chr(ord(letter)-13)
        result += shifted_letter
    return result 

decision = input("Decode (0) or Encode(1) ?: ")
while(decision != "q"):
    #Error Checking
    if(decision != "0" and decision != "1"):
        print("TRY AGAIN MAN")
        decision = input("Decode (0) or Encode(1) ?: ")
    elif (decision == "0"):
        #Decode
        user_input = input("Enter text to decode: ")
        decoded_input = decode_rot13(user_input)
        print(user_input + "\n" + decoded_input)
        break
    elif(decision == "1"):
        #Encode
        user_input = input("Enter text to encode: ")
        encoded_input = encode_rot13(user_input)

        print(user_input + "\n" + encoded_input)
        break

