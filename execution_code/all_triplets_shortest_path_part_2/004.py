def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index]); index +=1
    for tc in range(1, T+1):
        S = data[index]; index +=1
        N = int(data[index]); index +=1
        # Skip N-1 edges
        index += 2*(N-1)
        if S[0] == 'k':
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()