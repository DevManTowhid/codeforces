def calc_coins(coins):
    # 1. Sort descending
    coins.sort(reverse=True)
    
    total_sum = sum(coins)
    me_sum = 0
    
    # 2. Accumulate and check
    for i in range(len(coins)):
        me_sum += coins[i]
        
        # Must be strictly greater than half the total
        if me_sum > total_sum / 2:
            return i + 1  # i is 0-indexed, so add 1 for the count

# 3. Handle Codeforces Input/Output
if __name__ == "__main__":
    n = int(input())
    # Read the line of space-separated strings, convert each to int, and make a list
    coins = list(map(int, input().split()))
    
    print(calc_coins(coins))