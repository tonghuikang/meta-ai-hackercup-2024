import sys
import threading

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, K = map(int, sys.stdin.readline().split())
        grid = []
        one_positions = []
        question_positions = []
        rows_with_questions = [[] for _ in range(N)]
        cols_with_questions = [[] for _ in range(N)]
        for i in range(N):
            line = sys.stdin.readline().strip()
            grid.append(line)
            for j, ch in enumerate(line):
                if ch == '1':
                    one_positions.append((i, j))
                elif ch == '?':
                    question_positions.append((i, j))
                    rows_with_questions[i].append(j)
                    cols_with_questions[j].append(i)

        if one_positions:
            min_row = min(pos[0] for pos in one_positions)
            max_row = max(pos[0] for pos in one_positions)
            min_col = min(pos[1] for pos in one_positions)
            max_col = max(pos[1] for pos in one_positions)
            delta_row = max_row - min_row +1
            delta_col = max_col - min_col +1
        else:
            # Need to pick any '?' to start
            if question_positions:
                start_pos = question_positions.pop()
                K -= 1
                min_row = max_row = start_pos[0]
                min_col = max_col = start_pos[1]
                delta_row = 1
                delta_col = 1
                # Remove the selected position from rows_with_questions and cols_with_questions
                rows_with_questions[min_row].remove(min_col)
                cols_with_questions[min_col].remove(min_row)
            else:
                # Should not happen based on problem constraints
                print(f"Case #{case_num}: 0")
                continue

        # Build expansion lists
        min_row_list = []
        max_row_list = []
        min_col_list = []
        max_col_list = []

        for r in range(min_row -1, -1, -1):
            if rows_with_questions[r]:
                min_row_list.append(r)

        for r in range(max_row +1, N):
            if rows_with_questions[r]:
                max_row_list.append(r)

        for c in range(min_col -1, -1, -1):
            if cols_with_questions[c]:
                min_col_list.append(c)

        for c in range(max_col +1, N):
            if cols_with_questions[c]:
                max_col_list.append(c)

        min_row_ptr = 0
        max_row_ptr = 0
        min_col_ptr = 0
        max_col_ptr = 0

        while K > 0:
            candidates = []
            # Decrease min_row
            if min_row_ptr < len(min_row_list):
                area_increase = delta_col
                candidates.append(('min_row', area_increase))

            # Increase max_row
            if max_row_ptr < len(max_row_list):
                area_increase = delta_col
                candidates.append(('max_row', area_increase))

            # Decrease min_col
            if min_col_ptr < len(min_col_list):
                area_increase = delta_row
                candidates.append(('min_col', area_increase))

            # Increase max_col
            if max_col_ptr < len(max_col_list):
                area_increase = delta_row
                candidates.append(('max_col', area_increase))

            if not candidates:
                break  # No more expansions possible

            # Choose the expansion with max area increase
            candidates.sort(key=lambda x: (-x[1], x[0]))  # Sort by area_increase descending
            direction = candidates[0][0]

            if direction == 'min_row':
                min_row = min_row_list[min_row_ptr]
                min_row_ptr += 1
                delta_row = max_row - min_row + 1
            elif direction == 'max_row':
                max_row = max_row_list[max_row_ptr]
                max_row_ptr += 1
                delta_row = max_row - min_row + 1
            elif direction == 'min_col':
                min_col = min_col_list[min_col_ptr]
                min_col_ptr += 1
                delta_col = max_col - min_col +1
            elif direction == 'max_col':
                max_col = max_col_list[max_col_ptr]
                max_col_ptr += 1
                delta_col = max_col - min_col +1

            K -=1

        area = delta_row * delta_col
        print(f"Case #{case_num}: {area}")

threading.Thread(target=main).start()