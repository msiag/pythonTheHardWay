from sys import argv
script, user_name =argv
prompt = '?'

print(f"hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"what are games of zork were {user_name}")
zork  =input(prompt)

print(f"what are games of adventures were {user_name}")

adventures = input(prompt)

print(f"how many copies of zork you have")
zork_copies = input(prompt)

print(f"how many copies of adventures you have")
adventures_copies = input(prompt)
