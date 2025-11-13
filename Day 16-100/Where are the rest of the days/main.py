    for body_part in range(len(body)-1,0,1):
        new_x = body[body_part - 1].xcor()
        new_y = body[body_part - 1].ycor()
        body[body_part].goto(new_x, new_y)