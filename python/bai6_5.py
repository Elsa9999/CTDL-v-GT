from collections import deque

def bien_doi_st(s, t):
    """
    Transform integer S to integer T with minimum steps using operations:
    multiply by 2 or subtract 1.
    
    Args:
        s: Initial positive integer (S)
        t: Target positive integer (T)
    
    Returns:
        Minimum number of steps to transform S to T, or -1 if not possible
    """
    if s == t:
        return 0  # Base case: If initial number S already equals target T, return 0 steps
    
    # Initialize queue for BFS. Each element is a pair (current_number, steps_taken)
    q = deque([(s, 0)])
    
    # Set to keep track of visited numbers to avoid revisiting
    visited = {s}
    
    while q:
        current_s, steps = q.popleft()  # Get the first element from the queue
        
        # Operation (a): Multiply S by 2
        multiply_s = current_s * 2
        if multiply_s <= 20000 and multiply_s not in visited:
            if multiply_s == t:
                return steps + 1  # Found target, return number of steps
            q.append((multiply_s, steps + 1))
            visited.add(multiply_s)
        
        # Operation (b): Subtract 1 from S
        subtract_s = current_s - 1
        if subtract_s >= 1 and subtract_s not in visited:
            if subtract_s == t:
                return steps + 1  # Found target, return number of steps
            q.append((subtract_s, steps + 1))
            visited.add(subtract_s)
    
    return -1  # Theoretically, should not reach here given the problem constraints


def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        s, t = map(int, input().split())
        print(bien_doi_st(s, t))


if __name__ == "__main__":
    main()