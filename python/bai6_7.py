from collections import deque

# Function to check if two strings differ by exactly one character
def is_one_char_diff(str1, str2):
    if len(str1) != len(str2):
        return False  # If lengths are different, they definitely differ by more than one character
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    return diff_count == 1  # Return True if there's exactly one different character

# Function to find the shortest path between two words in a given word list
def shortest_path(word_list, start_word, end_word):
    q = deque([(start_word, 0)])  # Queue for BFS with (word, distance) pairs
    visited = {start_word}        # Set to track visited words
    
    while q:
        current_word, distance = q.popleft()  # Get the current word and its distance
        
        if current_word == end_word:  # If we've reached the target word
            return distance
        
        for next_word in word_list:
            if next_word not in visited and is_one_char_diff(current_word, next_word):
                # If the next word hasn't been visited and differs by exactly one character
                visited.add(next_word)
                q.append((next_word, distance + 1))
    
    return -1  # If no path is found (according to the problem, there should always be a path)

def main():
    t = int(input())
    for _ in range(t):
        line = input().split()
        n = int(line[0])
        s = line[1]
        t = line[2]
        
        word_list = input().split()[:n]  # Read n words from the next line
        
        print(shortest_path(word_list, s, t))

if __name__ == "__main__":
    main()