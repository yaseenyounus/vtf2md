import hcl2
import os

print(os.getcwd())

with open("variables.tf", 'r') as file:
    tf_dict = hcl2.load(file)

print(tf_dict["variable"])

for x in tf_dict["variable"]:
    print(x)
