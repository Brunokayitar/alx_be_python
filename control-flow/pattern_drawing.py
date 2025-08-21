pattern_size = int(input("Entr the size of the pattern: "))

current_row = 0

while current_row < pattern_size:
        
     for current_column in range(pattern_size):
          print("*", end="")
    
     print()
     current_row += 1