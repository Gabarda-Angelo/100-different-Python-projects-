# Day 6 Project : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json
#SOLUTION 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while not front_is_clear():
#         turn_right()
#     while front_is_clear() and not at_goal():
#         move()
#     if wall_on_right():
#         turn_left()
#         if front_is_clear():
#             if not at_goal():
#                 move()
#     else:
#         turn_right()
#     if wall_in_front():
#         jump()
#     else:
#         if not at_goal():
#             move()
#         turn_right()
#         while front_is_clear() and not at_goal():
#             move()
#         turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         while front_is_clear():
#
#             while wall_in_front():
#                 turn_right()
#             if not at_goal():
#                 move()


#SOLUTION 2 EASIEST and CLEAR


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# inital
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()






