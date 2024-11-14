import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for test_case in range(1, T+1):
        N = int(input[idx])
        idx +=1
        max_required_speed = 0.0
        min_allowed_speed = math.inf
        for i in range(1, N+1):
            A_i = int(input[idx])
            B_i = int(input[idx+1])
            idx +=2
            # Compute required speed >= i / B_i
            required_speed = i / B_i
            if required_speed > max_required_speed:
                max_required_speed = required_speed
            # If A_i >0, speed <= i / A_i
            if A_i >0:
                allowed_speed = i / A_i
                if allowed_speed < min_allowed_speed:
                    min_allowed_speed = allowed_speed
        # Now check if max_required_speed <= min_allowed_speed
        # If there are no A_i >0, min_allowed_speed remains inf, so no upper bound
        if min_allowed_speed == math.inf:
            # No upper bound
            answer = max_required_speed
        else:
            if max_required_speed <= min_allowed_speed +1e-12:
                answer = max_required_speed
            else:
                answer = -1
        if answer <0:
            print(f"Case #{test_case}: -1")
        else:
            print(f"Case #{test_case}: {answer}")
            
if __name__ == "__main__":
    main()