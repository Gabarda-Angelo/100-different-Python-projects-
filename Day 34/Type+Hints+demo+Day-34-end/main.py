# age: int
# name: str
# height: float
# is_human: bool


#we use type hints to give the programmers clarity to code.
#and stating that only of these data type could pass on and could not approving the dynamic typing(changing variable's data type according to its value)
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







