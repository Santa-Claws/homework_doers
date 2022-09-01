def calculator(x_axis_movenment, y_axis_movenment, quordinates: tuple[int, int]):
    (x_quor, y_quor) = quordinates
    moved_x = x_axis_movenment + x_quor
    moved_y = y_axis_movenment + y_quor
    movenment = (x_axis_movenment, y_axis_movenment)
    print(f'The x/y axis is {moved_x}/{moved_y}')
    return movenment


def calculator_supplies_and_run(movenment):
    x_quordinatents_input = input('what is the x the quordinate\n')
    y_quordinatents_input = input('what is the y the quordinate\n')
    x_quordinatents_int = int(x_quordinatents_input)
    y_quordinatents_int = int(y_quordinatents_input)
    both_quordinates = (x_quordinatents_int, y_quordinatents_int)
    if not movenment:
        x_axis_input = input('whats the x axis movement (use an integer)\n')
        y_axis_input = input('whats the y axis movement (use an integer)\n')
        movenment = (x_axis_input,y_axis_input)
        calculator(int(x_axis_input),int(y_axis_input) , both_quordinates)

    else:
        x_axis_move, y_axis_move = movenment
        calculator(int(x_axis_move), int(y_axis_move), both_quordinates)



    return movenment


times_input = input('how many quordinates')
i = 0
for i in range(int(times_input)):
        if i == 0:
            movenment = calculator_supplies_and_run(None)
        else:
            calculator_supplies_and_run(movenment)

