# 20.01.21
# formula: Z = n*x + n(n-1)/2
# Z = the number, X = the smallest addend, N = the amount of addends

import math

def output_as_a_summation(x, n):
    output = str(int(x))

    for i in range(1, n):

        output += " + "  + str(int(x+i))

    return output + "\n"

# this func wasn't necessary, but I didn't want to have too many if's and else's in the same place
def x_is_suitable(x, n, bool):
    if bool:
        return x - int(x) == 0 and x > 0
    else:
        # the 'x+n-1 != 0' statement prevents the biggest number from being 0 - like 'x != 0' prevents the smallest from being 0.
        return x - int(x) == 0 and x != 0 and x+n-1 != 0

negative_nums_disabled = None
while True:
    ipt = input('Disable negative nums? (y or n)  ')
    if ipt == 'y':
        negative_nums_disabled = True
        break
    elif ipt != 'n':
        continue
    else:
        break

while True:
    total_summations = 0

    number = input("\nPlease enter a whole number: ")
    try:
        if int(float(number)) == float(number):
            number = int(float(number))
        else:
            continue
    except:
        continue

    number = int(float(number))

    print("\nResult:\n")


    #  n*x + n(n-1) / 2 = z, so n(n-1) / 2 cannot be larger than z:
    # n(n-1) / 2 < z    -->    n(n-1) < 2z    -->    n(n-1) - 2z < 0    -->   n**2 - n - 2z < 0
    # quadratic formula: -1/2 + sqrt(1/4 + 2z) = n --> the lowest impossible value for n
    if negative_nums_disabled:
        biggest_possible_n = math.ceil(-1/2 + math.sqrt(1/4 + 2*number) + 1)
    else:
        biggest_possible_n = 2 * abs(number) + 1

    for n in range(2, biggest_possible_n):

        x = number / n - (n - 1) / 2
        if x_is_suitable(x, n, negative_nums_disabled):

          total_summations += 1
          print(output_as_a_summation(x, n) + " = " + str(number) + " N = " + str(n))

    if total_summations == 1:
        print("\nOnly one summation.\n-----------------------------------------------")

    elif total_summations == 0:
        print("This number cannot be written as a sum of consecutive numbers...\n-----------------------------------------------")

    else:
        print("\n" + str(total_summations) + " different summations...\n------------------------------------------------")
