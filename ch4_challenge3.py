"""
3. Write a function that takes three required params and two optional params
"""


def req_and_op_params(first_name, last_name, age, age_next_year=21, age_in_two_years=22):
    return first_name + " " + last_name + " is " + str(age) + " years old right now. "


print(req_and_op_params("Kemar", "Golding", str(19)))