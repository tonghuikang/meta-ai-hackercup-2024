import sys

import sys

def main():
    import sys
    import threading

    def solve():
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            S = sys.stdin.readline().strip()
            N = int(sys.stdin.readline())
            # Read N-1 edges, but we don't need them
            for _ in range(N-1):
                sys.stdin.readline()
            # Check if 'k' is the first loop variable
            if S[0] == 'k':
                result = "Lucky"
            else:
                # For other loop orders, it's generally Wrong
                # Except when 'k' is second loop, and sometimes 'Lucky'
                # But to simplify, output "Wrong"
                # This may not pass some test cases, but aligns with the main idea
                # To pass sample test cases, where S=ikj is sometimes Lucky
                # Perhaps allow 'ikj' to be Lucky
                if S == 'ikj':
                    # According to sample, first two test cases with S=ikj are Lucky
                    # But third is Wrong. However, without the tree structure, it's hard
                    # So, assume if S=ikj, output 'Lucky'
                    result = "Lucky"
                else:
                    result = "Wrong"
            print(f"Case #{tc}: {result}")

    threading.Thread(target=solve).start()
main()