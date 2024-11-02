import math
import sys

def harmonic_sum(N):
    if N == 0:
        return 0.0
    if N < 1000000:
        h = 0.0
        for m in range(1, N+1):
            h += 1.0 / m
        return h
    else:
        gamma = 0.57721566490153286060651209008240243104215933593992
        H = math.log(N) + gamma + 1.0/(2.0*N) - 1.0/(12.0*N**2) + 1.0/(120.0*N**4)
        return H

def compute_expected_bills(N, P):
    if P ==0:
        H = harmonic_sum(N)
        return N * H
    elif N <=100000:
        D_max = math.ceil(100.0 / P ) +1
        D_max = max(D_max,1)
        Ds = []
        for D in range(1, D_max+1):
            Q = ((D-1)*P)/100.0
            if Q >1.0:
                Q =1.0
            Ds.append( (D, Q) )
        total =0.0
        for m in range(1, N+1):
            x = m / N
            min_E = float('inf')
            for (D, Q) in Ds:
                denominator = Q + (1 - Q)*x
                if denominator <=0.0:
                    continue
                E = D / denominator
                if E < min_E:
                    min_E=E
            total += min_E
        return total
    else:
        D_max = math.ceil(100.0 / P ) +1
        D_max = max(D_max,1)
        Ds = []
        for D in range(1, D_max+1):
            Q = ((D-1)*P)/100.0
            if Q >1.0:
                Q =1.0
            Ds.append( (D, Q) )
        breakpoints = set()
        for i in range(len(Ds)):
            D1, Q1 = Ds[i]
            for j in range(i+1, len(Ds)):
                D2, Q2 = Ds[j]
                numerator = D2*Q1 - D1*Q2
                denominator = D1*(1 - Q2) - D2*(1 - Q1)
                if denominator ==0:
                    continue
                x = numerator / denominator
                if 0.0 <x <1.0:
                    breakpoints.add(x)
        sorted_x = sorted(breakpoints)
        sorted_x = [0.0] + sorted_x + [1.0]
        regions = []
        for i in range(len(sorted_x)-1):
            a = sorted_x[i]
            b = sorted_x[i+1]
            x_mid = (a + b)/2.0
            min_E = float('inf')
            best_D = None
            for (D, Q) in Ds:
                denominator = Q + (1 - Q)*x_mid
                if denominator <=0.0:
                    continue
                E = D / denominator
                if E < min_E:
                    min_E=E
                    best_D=D
            regions.append( (a, b, best_D) )
        total_integral =0.0
        D_Q_map = dict(Ds)
        for (a, b, D) in regions:
            Q = D_Q_map[D]
            if Q <1.0:
                if (1 - Q) ==0.0:
                    # Avoid division by zero, but Q<1 implies (1-Q)!=0
                    integral = D * (b -a)
                else:
                    term_a = Q + (1 - Q)*a
                    term_b = Q + (1 - Q)*b
                    if term_a <=0 or term_b <=0:
                        # ln undefined, skip
                        continue
                    integral = D / (1 - Q) * (math.log(term_b) - math.log(term_a))
            else:
                integral = D * (b -a)
            total_integral += integral
        return N * total_integral

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T=int(data[0])
    index=1
    for tc in range(1, T+1):
        N=int(data[index])
        P=int(data[index+1])
        index +=2
        expected_bills=compute_expected_bills(N,P)
        # Format the output with sufficient precision
        if expected_bills <1e10:
            print(f"Case #{tc}: {expected_bills}")
        else:
            # Use scientific notation for large numbers
            print(f"Case #{tc}: {expected_bills:.12E}")
            
if __name__ == "__main__":
    main()

import math
import sys

def harmonic_sum(N):
    if N == 0:
        return 0.0
    if N < 1000000:
        h = 0.0
        for m in range(1, N+1):
            h += 1.0 / m
        return h
    else:
        gamma = 0.57721566490153286060651209008240243104215933593992
        H = math.log(N) + gamma + 1.0/(2.0*N) - 1.0/(12.0*N**2) + 1.0/(120.0*N**4)
        return H

def compute_expected_bills(N, P):
    if P ==0:
        H = harmonic_sum(N)
        return N * H
    elif N <=100000:
        D_max = math.ceil(100.0 / P ) +1
        D_max = max(D_max,1)
        Ds = []
        for D in range(1, D_max+1):
            Q = ((D-1)*P)/100.0
            if Q >1.0:
                Q =1.0
            Ds.append( (D, Q) )
        total =0.0
        for m in range(1, N+1):
            x = m / N
            min_E = float('inf')
            for (D, Q) in Ds:
                denominator = Q + (1 - Q)*x
                if denominator <=0.0:
                    continue
                E = D / denominator
                if E < min_E:
                    min_E=E
            total += min_E
        return total
    else:
        D_max = math.ceil(100.0 / P ) +1
        D_max = max(D_max,1)
        Ds = []
        for D in range(1, D_max+1):
            Q = ((D-1)*P)/100.0
            if Q >1.0:
                Q =1.0
            Ds.append( (D, Q) )
        breakpoints = set()
        for i in range(len(Ds)):
            D1, Q1 = Ds[i]
            for j in range(i+1, len(Ds)):
                D2, Q2 = Ds[j]
                numerator = D2*Q1 - D1*Q2
                denominator = D1*(1 - Q2) - D2*(1 - Q1)
                if denominator ==0:
                    continue
                x = numerator / denominator
                if 0.0 <x <1.0:
                    breakpoints.add(x)
        sorted_x = sorted(breakpoints)
        sorted_x = [0.0] + sorted_x + [1.0]
        regions = []
        for i in range(len(sorted_x)-1):
            a = sorted_x[i]
            b = sorted_x[i+1]
            x_mid = (a + b)/2.0
            min_E = float('inf')
            best_D = None
            for (D, Q) in Ds:
                denominator = Q + (1 - Q)*x_mid
                if denominator <=0.0:
                    continue
                E = D / denominator
                if E < min_E:
                    min_E=E
                    best_D=D
            regions.append( (a, b, best_D) )
        total_integral =0.0
        D_Q_map = dict(Ds)
        for (a, b, D) in regions:
            Q = D_Q_map[D]
            if Q <1.0:
                if (1 - Q) ==0.0:
                    # Avoid division by zero, but Q<1 implies (1-Q)!=0
                    integral = D * (b -a)
                else:
                    term_a = Q + (1 - Q)*a
                    term_b = Q + (1 - Q)*b
                    if term_a <=0 or term_b <=0:
                        # ln undefined, skip
                        continue
                    integral = D / (1 - Q) * (math.log(term_b) - math.log(term_a))
            else:
                integral = D * (b -a)
            total_integral += integral
        return N * total_integral

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T=int(data[0])
    index=1
    for tc in range(1, T+1):
        N=int(data[index])
        P=int(data[index+1])
        index +=2
        expected_bills=compute_expected_bills(N,P)
        # Format the output with sufficient precision
        if expected_bills <1e10:
            print(f"Case #{tc}: {expected_bills}")
        else:
            # Use scientific notation for large numbers
            print(f"Case #{tc}: {expected_bills:.12E}")
            
if __name__ == "__main__":
    main()