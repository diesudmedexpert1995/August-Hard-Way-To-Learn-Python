from sys import argv

script, username = argv

prompt = '> '

print(f"Hello, {username}. I`m script {script}.")
print("I wanna ask some questions to you.")

print(f"Do you like me {username}?")
likes = input(prompt)

print("Where do you live???")
lives = input()

print("What computer you use?")
computer = input(prompt)

print(f"""
    So, you answered {likes} for question Do you like me???
    You live in {lives}. I can`t imagine where is it.
    And you have a {computer} computer. Excellent!
 """)
