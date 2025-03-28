def pascals_triangle(rows):
    
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        row = [1]
        
        for j in range(1, i + 1):
            next_num = row[j-1] * (i - j + 1) // j
            row.append(next_num)
        
        row_str = ' '.join(map(str, row))
        print(spaces + row_str)
        
pascals_triangle(5)
