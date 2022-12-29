#Indexing and Slicing Lab Script

message = input("Enter a message: ") 

print("First Character: ", message[0])
print("Last Character: ", message[-1])
print("Middle Character: ", message[int(len(message) / 2)])
print("Even Characters: ", message[0::2])
print("Odd Characters: ", message[1::2])
print("Reversed Message: ", message[::-1])