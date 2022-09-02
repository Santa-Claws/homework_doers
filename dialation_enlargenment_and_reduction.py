def calculator(quoordinates: list, scale_factor):
    ending_quordinates_list = []
    for i in quoordinates:
        ending_quordinates_list.append(i * scale_factor)
    return ending_quordinates_list


scale_factor_input = input('whats the scale factor')
number_of_times = input('how many quordinates')
all_quordinates = []
for i in range(int(number_of_times)):
    x_quordinatents_input = input(f'what is the x the quordinate to number {i}\n')
    y_quordinatents_input = input(f'what is the y the quordinate to number {i}\n')
    all_quordinates.append(int(x_quordinatents_input))
    all_quordinates.append(int(x_quordinatents_input))
    all_quordinates.append('|')
final_quordinates = calculator(all_quordinates, int(scale_factor_input))
print(final_quordinates)
