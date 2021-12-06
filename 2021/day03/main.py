import numpy as np


def main():

    # input = open('sample_input.txt', 'r')
    input = open('input.txt', 'r')

    data = []

    for line in input.readlines():
        data.append(line.strip())

    splitted_data = []
    for d in data:
        s = [char for char in d]
        splitted_data.append(s)

    
    m = np.array(splitted_data)

    gamma_rate = []
    epsilon_rate = []

    for t in m.T:
        number_of_zeros = 0
        number_of_ones = 0
        for i in t:
            if i == '0':
                number_of_zeros += 1
            else:
                number_of_ones += 1
        
        if number_of_zeros > number_of_ones:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')


    # print(gamma_rate)
    # print(epsilon_rate)

    g = ''.join(gamma_rate)
    e = ''.join(epsilon_rate)

    print(gamma_rate)
    print(epsilon_rate)
    b_g = bin(int('0b' + g, 2))
    b_e = bin(int('0b' + e, 2))

    print(b_g)
    print(b_e)

    d_g = int(b_g, 2)
    d_e = int(b_e, 2)

    print(f"GAMMA RATE: {d_g}")
    print(f"EPSILON RATE: {d_e}")
    print(f"POWER CONSUMPTION: {d_g * d_e}")


    return 0

if __name__ == "__main__":
    main()