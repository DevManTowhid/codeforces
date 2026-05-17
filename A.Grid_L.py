import sys
import math

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        p = int(input_data[idx])
        q = int(input_data[idx+1])
        idx += 2
        
        # Total equivalent single segments
        S = p + 2 * q
        
        # Target factor value
        K = 2 * S + 1
        
        found = False
        limit = int(math.isqrt(K))
        
        # Loop through odd factors up to sqrt(K)
        # Start at 3 because n >= 1 implies (2n + 1) >= 3
        for A in range(3, limit + 1, 2):
            if K % A == 0:
                B = K // A
                
                # Derive n and m from factors
                n = (A - 1) // 2
                m = (B - 1) // 2
                
                # Check the L-shape constraint
                if q <= min(n * (m + 1), m * (n + 1)):
                    results.append(f"{n} {m}")
                    found = True
                    break
        
        if not found:
            results.append("-1")
            
    print("\n".join(results))

if __name__ == '__main__':
    solve()