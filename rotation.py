from typing import Tuple


# (-y, x)
def counterclock_90_rotation(quordinates: Tuple[int, int]):
    x_quor, y_quor = quordinates
    y_quor = y_quor - (y_quor * 2)
    new_quordinates = (y_quor, x_quor)
    return new_quordinates

def clock_90_rotation(quordinates):
    x_quor, y_quor = quordinates
    x_quor = x_quor - (x_quor * 2)
    new_quordinates = (y_quor, x_quor)
    return new_quordinates

def rotation_180(quordinates):
    x_quor, y_quor = quordinates
    y_quor = y_quor - (y_quor * 2)
    x_quor = x_quor - (x_quor *2)
    new_quordinates = (x_quor, y_quor)
    return new_quordinates

num_of_quordinates_input = input('how many quordinates\n')
rotation_input = input('whats the rotation (ex. 90 counterclock) (ex. 90 clock) (just type 180 for 180 degrees)\n')
total_quors = []
for i in range(int(num_of_quordinates_input)):
    x_input = input(f'whats the x value for quordinate number {i + 1}\n')
    y_input = input(f'whats the y value for quordinate number {i + 1}\n')
    quors = (int(x_input), int(y_input))
    if rotation_input == '90 counterclock':
        final_quors = counterclock_90_rotation(quors)
    elif rotation_input == '90 clock':
        final_quors = clock_90_rotation(quors)
    elif rotation_input == '180':
        final_quors = rotation_180(quors)
    total_quors.append(f'quordinate number {i + 1}')
    total_quors.append(final_quors)
    total_quors.append('|||')
print(total_quors)

