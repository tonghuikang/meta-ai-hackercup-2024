from bisect import bisect_left, bisect_right

def generate_sequences(seq, k, last_digit, digits_list, sequences):
    if len(seq) == k:
        sequences.append(seq.copy())
        return
    for digit in digits_list:
        if digit >= last_digit:
            seq.append(digit)
            generate_sequences(seq, k, digit, digits_list, sequences)
            seq.pop()

def generate_mountains():
    mountains = []
    for k in range(0, 10):  # k from 0 to 9 (max length 19 digits)
        for D_m in range(1, 10):  # Middle digit from 1 to 9
            digits_list = [d for d in range(1, 10) if d != D_m]
            sequences = []
            generate_sequences([], k, 1, digits_list, sequences)
            for seq in sequences:
                mountain_digits = seq + [D_m] + seq[::-1]
                mountain_str = ''.join(map(str, mountain_digits))
                mountain_num = int(mountain_str)
                mountains.append(mountain_num)
    mountains.sort()
    return mountains

def main():
    mountains = generate_mountains()
    T = int(input())
    for case_num in range(1, T + 1):
        A_str, B_str, M_str = input().split()
        A, B, M = int(A_str), int(B_str), int(M_str)
        # Find indices of mountains within [A, B]
        left = bisect_left(mountains, A)
        right = bisect_right(mountains, B)
        count = 0
        # For the numbers in that range, check which ones are divisible by M
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f'Case #{case_num}: {count}')

if __name__ == '__main__':
    main()