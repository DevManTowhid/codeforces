import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        c_T = int(input_data[idx])
        c_H = int(input_data[idx+1])
        c_U = int(input_data[idx+2])
        idx += 3
        
        # Start by assuming every block takes 3 rows
        total_rows = 3 * (c_T + c_H + c_U)
        
        # PRIORITY 1: Pair T and U
        # U + T makes a 4x3 block. Saves 2 rows compared to 3+3=6.
        tu_pairs = min(c_T, c_U)
        total_rows -= 2 * tu_pairs
        c_T -= tu_pairs
        
        # PRIORITY 2: Insert T into H gaps
        # Each H has 2 gaps, so it can hold up to 2 T's. Saves 1 row per T.
        th_pairs = min(c_T, 2 * c_H)
        total_rows -= th_pairs
        c_T -= th_pairs
        
        # PRIORITY 3: Chain remaining T's
        # K stacked T's take 2K+1 rows instead of 3K rows. Saves K-1 rows.
        if c_T > 0:
            total_rows -= (c_T - 1)
            
        results.append(str(total_rows))
        
    # Output all results
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()