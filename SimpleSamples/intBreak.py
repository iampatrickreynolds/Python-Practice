def intBreak(n):
    maxprods = [0, 0, 1]
    for num in range(3, n + 1):
        u1 = [maxprods[i] * maxprods[num - i] for i in range(2, (num + 1) / 2 + 1)]
        u2 = [maxprods[i] * (num - i) for i in range(2, (num + 1) / 2 + 1)]
        u3 = [i * maxprods[num - i] for i in range(2, (num + 1) / 2 + 1)]
        u4 = [i * (num - i) for i in range(2, (num + 1) / 2 + 1)]    
        best = max(map(max, map(max, u1, u2), map(max, u3, u4)))
        maxprods.append(best)
    return maxprods[n]
    
def main():
    for i in range(0, 10):
        print intBreak(i)
        
if __name__ == '__main__':
    main()
        