import sys
import sys
import sys
from collections import defaultdict

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if ' ' in line:
            E, K = line.rsplit(' ', 1)
        else:
            E = line
            K = '1'
        K = int(K)
        N = len(E)
        dp_max = [0] * (N + 1)
        dp_cnt = [0] * (N + 1)
        dp_max[N] = 0
        dp_cnt[N] = 1
        # Precompute possible digit options for each position
        possible_digits = []
        for c in E:
            if c == '?':
                possible_digits.append([str(d) for d in range(0,10)])
            else:
                possible_digits.append([c])
        # Precompute possible two-digit options for each position
        possible_two_digits = []
        for i in range(N):
            if i+1 >= N:
                possible_two_digits.append([])
                continue
            first = possible_digits[i]
            second = possible_digits[i+1]
            two_digit_options = []
            for d1 in first:
                for d2 in second:
                    num = d1 + d2
                    if '10' <= num <= '26':
                        two_digit_options.append(num)
            possible_two_digits.append(two_digit_options)
        # Compute dp_max and dp_cnt
        for i in range(N-1, -1, -1):
            current_max = -1
            current_cnt = 0
            # 1-digit option
            singles = []
            for d in possible_digits[i]:
                if '1' <= d <= '9':
                    singles.append(d)
            if singles:
                max1 = dp_max[i+1] + 1
                if max1 > current_max:
                    current_max = max1
                    current_cnt = 0
                if max1 == current_max:
                    current_cnt += dp_cnt[i+1] * len(singles)
            # 2-digit option
            if i+1 < N:
                twos = possible_two_digits[i]
                if twos:
                    max2 = dp_max[i+2] + 1
                    if max2 > current_max:
                        current_max = max2
                        current_cnt = 0
                    if max2 == current_max:
                        current_cnt += dp_cnt[i+2] * len(twos)
            dp_max[i] = current_max
            dp_cnt[i] = current_cnt % MOD
        # Now, find the maximum split count
        max_split = dp_max[0]
        # Now, we need to reconstruct the Kth lex largest string
        # Precompute, for each position, the possible choices that lead to dp_max[i]
        # and the number of ways they lead to the end
        choices = [[] for _ in range(N)]
        for i in range(N):
            if dp_max[i] == -1:
                continue
            current_choices = []
            # 1-digit option
            singles = []
            for d in possible_digits[i]:
                if '1' <= d <= '9':
                    singles.append(d)
            for d in singles:
                # Check if choosing this digit leads to dp_max[i]
                if dp_max[i] == dp_max[i+1] + 1:
                    current_choices.append( (d, 1) )  # 1 indicates single digit
            # 2-digit option
            if i+1 < N:
                twos = possible_two_digits[i]
                for num in twos:
                    # Check if choosing this two-digit number leads to dp_max[i]
                    if dp_max[i] == dp_max[i+2] + 1:
                        current_choices.append( (num, 2) )
            choices[i] = current_choices
        # Now, perform the reconstruction
        result = []
        i = 0
        remaining_K = K
        while i < N:
            # At position i, list possible choices that lead to dp_max[i]
            current_choices = []
            # 1-digit options
            singles = []
            for d in possible_digits[i]:
                if '1' <= d <= '9':
                    singles.append(d)
            single_choices = []
            for d in singles:
                if dp_max[i] == dp_max[i+1] + 1:
                    single_choices.append(d)
            # 2-digit options
            two_choices = []
            if i+1 < N:
                twos = possible_two_digits[i]
                for num in twos:
                    if dp_max[i] == dp_max[i+2] + 1:
                        two_choices.append(num)
            # Create list of possible choices with their type
            possible_choices = []
            for d in single_choices:
                possible_choices.append( (d, 1) )
            for num in two_choices:
                possible_choices.append( (num, 2) )
            # Now, sort the choices in descending lex order
            possible_choices_sorted = sorted(possible_choices, key=lambda x: x[0], reverse=True)
            # Now, iterate through the sorted choices and choose the one where cumulative counts >= K
            selected = None
            for choice, typ in possible_choices_sorted:
                if typ == 1:
                    cnt = dp_cnt[i+1]
                else:
                    cnt = dp_cnt[i+2]
                if cnt >= remaining_K:
                    selected = (choice, typ)
                    break
                else:
                    remaining_K -= cnt
            if selected is None:
                # This should not happen as per problem constraints
                break
            # Append the chosen digits to the result
            selected_choice, selected_type = selected
            result.append(selected_choice)
            if selected_type == 1:
                i += 1
            else:
                i += 2
        # Now, among all possible strings that achieve the max split, find the Kth lex largest
        # The above reconstruction already finds the Kth lex largest
        final_string = ''.join(result)
        final_count = dp_cnt[0] % MOD
        print(f"Case #{test_case}: {final_string} {final_count}")
 
if __name__ == "__main__":
    main()