
# This is a sample Python script.
from ast import Str
from typing import AnyStr


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(title):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {title}')  # Press ⌘F8 to toggle the breakpoint.
    # hi stephen


def what_is_a_dict(key: str) -> str:
    contact = {"first_name": "Stephen", "last_name": "Gwin", "email": "stephengwin76@gmail.com"}
    print("All items from key: \n", contact.items())
    for k, v in contact.items():
        print(f"Key: {k}, value: {v}")
    return f"Stephen Gwin's {key} is {contact[key]}"

def access_from_a_list(index: int) -> int:
    list_of_numbers = list(range(0, 11))
    # [0,1,2,3,4,5,6,7,8,9,10]
    for number in list_of_numbers:
        print(f"this is the number {number}")
    return list_of_numbers[index]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = what_is_a_dict('email')
    number_at_index=access_from_a_list(3)
    print(number_at_index)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
