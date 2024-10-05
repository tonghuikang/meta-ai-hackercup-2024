import sys
import threading
import sys

def main():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    
    for test_case in range(1, T +1):
        N, G = map(int, sys.stdin.readline().split())
        E = []
        for _ in range(N):
            E.append(int(sys.stdin.readline()))
        
        pos_map = {}  # position -> stone_id
        final_pos = [0] * (N +1)  # stone_id 1-based index
        
        class SegTree:
            def __init__(self, l, r):
                self.l = l
                self.r = r
                self.left = None
                self.right = None
                self.min_val = math.inf

            def query_min(self, ql, qr):
                if self.r < ql or self.l > qr:
                    return math.inf
                if ql <= self.l and self.r <= qr:
                    return self.min_val
                mid = (self.l + self.r) //2
                if not self.left:
                    self.left = SegTree(self.l, mid)
                if not self.right:
                    self.right = SegTree(mid+1, self.r)
                return min(self.left.query_min(ql, qr), self.right.query_min(ql, qr))
            
            def update(self, x):
                if self.l == self.r:
                    self.min_val = x
                    return
                mid = (self.l + self.r) //2
                if x <= mid:
                    if not self.left:
                        self.left = SegTree(self.l, mid)
                    self.left.update(x)
                else:
                    if not self.right:
                        self.right = SegTree(mid+1, self.r)
                    self.right.update(x)
                self.min_val = math.inf
                if self.left:
                    self.min_val = min(self.min_val, self.left.min_val)
                if self.right:
                    self.min_val = min(self.min_val, self.right.min_val)
        
        MAX_POS = 1000000 + 10
        seg = SegTree(1, MAX_POS)
        
        def move(stone_id, base_p, energy):
            intended_pos = base_p + energy
            if intended_pos > MAX_POS:
                intended_pos = MAX_POS
            min_x = seg.query_min(base_p +1, intended_pos)
            if min_x == math.inf:
                # No collision
                final_pos[stone_id] = intended_pos
                pos_map[intended_pos] = stone_id
                seg.update(intended_pos)
            else:
                # Collision at min_x
                final_pos[stone_id] = min_x
                existing_stone = pos_map[min_x]
                pos_map[min_x] = stone_id
                # Transfer remaining energy to existing stone
                remaining_e = base_p + energy - min_x
                move(existing_stone, min_x, remaining_e)
        
        for i in range(1, N +1):
            move(i, 0, E[i-1])
        
        # Now find the stone closest to G
        min_distance = math.inf
        selected_stone = 0
        for stone_id in range(1, N +1):
            d = abs(G - final_pos[stone_id])
            if d < min_distance or (d == min_distance and stone_id < selected_stone):
                min_distance = d
                selected_stone = stone_id
        print(f"Case #{test_case}: {selected_stone} {min_distance}")

threading.Thread(target=main,).start()