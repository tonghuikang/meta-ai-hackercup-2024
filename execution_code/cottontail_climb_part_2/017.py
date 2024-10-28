import sys
import itertools
import bisect

def generate_non_decreasing_sequences(k, max_digit):
    if k == 0:
        return [()]
    return list(itertools.combinations_with_replacement(range(1, max_digit +1), k))

def generate_non_increasing_sequences(k, max_digit):
    if k == 0:
        return [()]
    sequences = generate_non_decreasing_sequences(k, max_digit)
    return [tuple(reversed(seq)) for seq in sequences]

def generate_all_mountain_numbers():
    mountains = []
    for k in range(0, 10):
        l = 2 * k +1
        for m in range(1, 10):
            if k ==0:
                mountains.append(m)
                continue
            max_digit = m -1
            if max_digit <1:
                continue
            first_sequences = generate_non_decreasing_sequences(k, max_digit)
            last_sequences = generate_non_increasing_sequences(k, max_digit)
            for first_k in first_sequences:
                for last_k in last_sequences:
                    # Combine to form the number
                    num_digits = first_k + (m,) + last_k
                    number = 0
                    for d in num_digits:
                        number = number *10 + d
                    mountains.append(number)
    mountains = sorted(mountains)
    return mountains

def main():
    import sys
    import threading
    def run():
        mountains = generate_all_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            A_str, B_str, M_str = line.strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the indices
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")
    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()