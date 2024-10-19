import sys
import threading

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for case_num in range(1, T+1):
        input_line = sys.stdin.readline().strip()
        if not input_line:
            input_line = sys.stdin.readline().strip()
        if not input_line:
            continue
        if ' ' in input_line:
            E_str, K_str = input_line.split()
        else:
            E_str = input_line
            K_str = sys.stdin.readline().strip()
        K = int(K_str)
        E = E_str.strip()
        n = len(E)
        # Positions of '?', and possible digits per position
        positions = []
        possible_digits = []
        i = 0
        while i < n:
            if E[i] != '?':
                i +=1
                continue
            # Determine possible digits for position i
            # Default possible digits
            digits = []
            # Check if this is at the end
            if i == n -1:
                # Last position
                if i > 0 and E[i-1] == '2':
                    digits = ['6','5','4','3','2','1']
                else:
                    digits = ['9','8','7','6','5','4','3','2','1']
                positions.append(i)
                possible_digits.append(digits)
                i +=1
                continue
            # Check for consecutive '?' at the end
            if i < n -1 and E[i+1] == '?':
                # Check if at the end
                if i == n -2:
                    # Positions i and i+1 are '?'
                    # Possible two-digit numbers between '11'-'26', excluding '20'
                    two_digit_numbers = []
                    for num in range(26,10,-1):
                        if num != 20:
                            two_digit_numbers.append(str(num))
                    digits_i = []
                    digits_i1 = []
                    for num in two_digit_numbers:
                        digits_i.append(num[0])
                        digits_i1.append(num[1])
                    # Remove duplicates while maintaining order
                    digits_i = list(dict.fromkeys(digits_i))
                    digits_i1 = list(dict.fromkeys(digits_i1))
                    positions.append(i)
                    possible_digits.append(digits_i)
                    positions.append(i+1)
                    possible_digits.append(digits_i1)
                    i +=2
                    continue
            # Default case
            # Possible digits '1' and '2'
            digits = ['2','1']
            positions.append(i)
            possible_digits.append(digits)
            i +=1
        # Now we need to compute the total number of uncorrupted strings
        bases = []
        total_U = 1
        for digits in possible_digits:
            total_U *= len(digits)
        # Check if K is valid
        if K > total_U:
            print(f"Case #{case_num}: IMPOSSIBLE")
            continue
        # Prepare for mapping K-1 to indices
        num_positions = len(positions)
        base_sizes = [len(possible_digits[i]) for i in range(num_positions)]
        # Compute cumulative products for indexing
        cumprod = [1]*num_positions
        for i in range(num_positions-2,-1,-1):
            cumprod[i] = cumprod[i+1]*base_sizes[i+1]
        # Adjust K to zero-based index
        K -=1
        # Map K to indices
        indices = [0]*num_positions
        for i in range(num_positions):
            indices[i] = K // cumprod[i]
            K %= cumprod[i]
        # Build the uncorrupted string
        U_list = list(E)
        for idx, pos in enumerate(positions):
            U_list[pos] = possible_digits[idx][indices[idx]]
        U = ''.join(U_list)
        # Compute D(U) using DP
        n = len(U)
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            if U[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i+1]
            if i+1 < n:
                num = int(U[i:i+2])
                if 10 <= num <=26:
                    dp[i] = (dp[i] + dp[i+2]) % MOD
        D_U = dp[0] % MOD
        print(f"Case #{case_num}: {U} {D_U}")
        
threading.Thread(target=main).start()