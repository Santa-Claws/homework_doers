from typing import Tuple


#still working out the errors
#if you have this homework then just use the rotation.py and do the quordinate converting manuely

# (-y, x)
def counterclock_90_rotation_custom_point(quordinates: Tuple[int, int], rotation_point: Tuple[int, int]):
    x_quor, y_quor = quordinates
    rotation_x_quor, rotation_y_quor = rotation_point
    x_quor = x_quor - rotation_x_quor
    y_quor = y_quor - rotation_y_quor
    y_quor = y_quor - (y_quor * 2)
    new_quordinates = (y_quor, x_quor)
    return new_quordinates


def clock_90_rotation_custom_point(quordinates: Tuple[int, int], rotation_point: Tuple[int, int]):
    x_quor, y_quor = quordinates
    rotation_x_quor, rotation_y_quor = rotation_point
    x_quor = x_quor - rotation_x_quor
    y_quor = y_quor - rotation_y_quor
    x_quor = x_quor - (x_quor * 2)
    new_quordinates = (y_quor, x_quor)
    return new_quordinates


def rotation_180_custom_point(quordinates: Tuple[int, int], rotation_point: Tuple[int, int]):
    x_quor, y_quor = quordinates
    rotation_x_quor, rotation_y_quor = rotation_point
    x_quor = x_quor - rotation_x_quor
    y_quor = y_quor - rotation_y_quor
    y_quor = y_quor - (y_quor * 2)
    x_quor = x_quor - (x_quor * 2)
    new_quordinates = (x_quor, y_quor)
    return new_quordinates


num_of_quordinates_input = input('how many quordinates\n')
rotation_input = input('whats the rotation (ex. 90 counterclock) (ex. 90 clock) (just type 180 for 180 degrees)\n')
new_origin_x = input('what are the x quordinates of the point thats being rotated around (type zero if around original origin)\n')
new_origin_y = input('what are the y quordinates of the point thats being rotated around (type zero if around original origin)\n')
new_origin = (int(new_origin_x), int(new_origin_y))
total_quors = []

for i in range(int(num_of_quordinates_input)):
    x_input = input(f'whats the x value for quordinate number {i + 1} in relation to the original origin\n')
    y_input = input(f'whats the y value for quordinate number {i + 1} in relation to the original origin\n')
    quors = (int(x_input), int(y_input))
    if rotation_input == '90 counterclock':
        final_quors = counterclock_90_rotation_custom_point(quors, new_origin)
    elif rotation_input == '90 clock':
        final_quors = clock_90_rotation_custom_point(quors, new_origin)
    elif rotation_input == '180':
        final_quors = rotation_180_custom_point(quors, new_origin)
    total_quors.append(f'quordinate number {i + 1}')
    total_quors.append(final_quors)
    total_quors.append('|||')
print(total_quors)
