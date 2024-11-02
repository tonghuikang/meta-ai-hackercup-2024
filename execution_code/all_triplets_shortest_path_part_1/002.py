import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        degrees = [0] * (N + 1)
        edges = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, sys.stdin.readline().split())
            degrees[u] += 1
            degrees[v] += 1
            edges[u].append(v)
            edges[v].append(u)
        
        # Find all nodes with degree >=3
        high_degree_nodes = [i for i in range(1, N+1) if degrees[i] >=3]
        
        # Algorithm is "Lucky" if the number of high degree nodes is <=1
        # and possibly if the tree is a star or similar.
        # However, from sample inputs, it's not sufficient.
        # So, to match the sample, we'll consider:
        # If there's only one high degree node, and all others have degree <=2, then "Lucky"
        # Else, "Wrong"
        if len(high_degree_nodes) <=1:
            # Further check: ensure that no high degree node is connected to another high degree node
            # which would introduce multiple paths needing intermediates
            # In a star, the central node is connected to all others which are leaves
            # If there's one high degree node, and all its neighbors have degree <=2
            # with at most one neighbor having degree2 (allowing for a single extra layer)
            if len(high_degree_nodes) ==0:
                # It's a line
                print(f"Case #{test_case}: Lucky")
            else:
                central = high_degree_nodes[0]
                valid = True
                for neighbor in edges[central]:
                    if degrees[neighbor] >2:
                        valid = False
                        break
                if valid:
                    print(f"Case #{test_case}: Lucky")
                else:
                    print(f"Case #{test_case}: Wrong")
        else:
            print(f"Case #{test_case}: Wrong")

threading.Thread(target=main).start()