T = int(input())
peaks = []
# Precompute all possible peaks
for k in range(0, 9):  # k from 0 to 8
    max_D1 = 9 - k
    for D_1 in range(1, max_D1 + 1):
        ascending_digits = [D_1 + i for i in range(k + 1)]
        # Ensure no digit is greater than 9
        if any(d > 9 for d in ascending_digits):
            continue
        descending_digits = ascending_digits[:-1][::-1]
        digits = ascending_digits + descending_digits
        number = int(''.join(map(str, digits)))
        peaks.append(number)

# Process each test case
for case_num in range(1, T + 1):
    A_str = input().strip()
    while A_str == '':
        A_str = input().strip()
    A, B, M = map(int, A_str.strip().split())
    count = 0
    for peak in peaks:
        if A <= peak <= B and peak % M == 0:
            count += 1
    print(f'Case #{case_num}: {count}')