# Question 1

Total_Time = int(input( " Please input a number: "))
hours = Total_Time // 3600
minutes = (Total_Time - (hours * 3600)) // 60
seconds = Total_Time - (hours * 3600) - (minutes *60)

print(f'hours: {hours}, minutes: {minutes}, seconds: {seconds}')

import math
# Question 2
side_1 = 3
side_2 = 7
side_3 = 9

# Law of Cosines for each angle
Angle_A_cos = (side_3**2 + side_2**2 - side_1**2) / (2 * side_3 * side_2)
Angle_B_cos = (side_1**2 + side_3**2 - side_2**2) / (2 * side_1 * side_3)
Angle_C_cos = (side_1**2 + side_2**2 - side_3**2) / (2 * side_1 * side_2)

# Convert from radians to degrees
Angle_A = math.degrees(math.acos(Angle_A_cos))
Angle_B = math.degrees(math.acos(Angle_B_cos))
Angle_C = math.degrees(math.acos(Angle_C_cos))

# Print the angles
print(f'Angle A: {Angle_A:.2f} degrees')
print(f'Angle B: {Angle_B:.2f} degrees')
print(f'Angle C: {Angle_C:.2f} degrees')


# Question 3
# 6 numbers
# first condition (last four numbers) palindrome
# second condition (+1 mile) last 5 digits palindrome
# third condition (+1 mile) middle 4 digits formed a palindrome
# fourth condition (+1 mile) all digits formed a palindrome

def is_palindrome(num, l, r):
    num_str = str(num)
    print(num_str)
    return num_str[l:r] == num_str[l:r][::-1]

number = 100000
condition = True


while condition:
   if (is_palindrome(number, 2, 6) and
        is_palindrome(number + 1, 1, 6) and
        is_palindrome(number + 2, 1, 5) and
        is_palindrome(number + 3, 0, 6)):
        palindrome_number = number
        condition = False
   number += 1

print(palindrome_number)









