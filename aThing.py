print("this is a string")
name = "Eric"
print(type(name))
fact = "my favorite game is GTA 5"
print("my name is " + name + " and I like " + fact)
# or
print("my name is ", name, " and i like ", fact)
# or
message = "my name is " + name + " and I like " + fact
print(message)

# vars
num = 8
num2 = 14

print(num+num2)

answer = num - num2
print(answer)

# vars
word = "sweet"
word1 = "cool"
word2 = "mean"
word3 = "dark"
word4 = "mate"

print("I took a sip of " + word + " tea that was nice and " + word1 + ". With my " + word + " " + word1 + " tea I ate a " + word2 +
      " steak that was cooked to perfection. It started to get " + word3 + " so me and my " + word4 + " decided to call it a night.")

# update vars to inputs
word = input("Type an adjective ")
word1 = input("Type a name ")
word2 = input("Type another name ")
word3 = input("Type a weapon ")
word4 = input("Type another weapon ")

# new madlib
print("On a " + word + " night " + word1 + " was angerd at " + word2 + " because " + word2 + " wasn't being really nice. " + word1 + " decided to pickup a " + word3 +
      " and proceed to hit " + word2 + " with it. But " + word2 + " didn't like that so " + word2 + " decided to pick up a " + word4 + " and fight " + word1 + " with it. In an epic battle to the death " + word1 + " was victorious.")

input()
