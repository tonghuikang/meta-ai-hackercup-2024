To solve this problem efficiently, we need to simulate the stone-throwing process while handling potential collisions between stones. Here's a breakdown of the key steps and insights used to develop the solution:

### Key Findings:

1. **Collision Handling:** 
   - When a stone is thrown, it attempts to reach its intended position. If that position is already occupied by another stone, the thrown stone collides with the stationary stone at that position. The moving stone transfers its remaining energy to the stationary stone, which then attempts to move forward with the transferred energy.

2. **Efficient Position Tracking:** 
   - To efficiently track occupied positions and quickly find the first occupied position within a range, a **Segment Tree** is utilized. This data structure allows us to perform range queries and updates in logarithmic time, which is crucial given the problem's constraints.

3. **Recursive Movement:**
   - The movement and potential chain reactions of stones are handled recursively. When a collision occurs, the existing stone at the occupied position is moved with the remaining energy, potentially causing further collisions.

4. **Final Position Determination:**
   - After all stones have been processed, the final positions of the stones are determined. The stone closest to the goal position \( G \) is identified, and ties are broken by selecting the stone with the lowest index.

### Implementation Steps:

1. **Segment Tree Construction:**
   - A recursive Segment Tree is built to keep track of occupied positions. Each node in the tree represents a range of positions and stores the minimum occupied position within that range. If no positions in the range are occupied, it returns infinity.

2. **Stone Processing:**
   - For each stone, we attempt to place it at its intended position. If that position is occupied, we recursively move the existing stone to a new position based on the remaining energy.

3. **Final Evaluation:**
   - After placing all stones, we iterate through their final positions to determine which stone is closest to the goal. The distance is calculated, and in the case of ties, the stone with the lower index is chosen.

### Python Code:

```python
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
```