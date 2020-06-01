class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def generate_pascal_row(row_index, previous_row):
            
            pascal_row = []
            for i in range(1, len(previous_row)):
                pascal_row.append(previous_row[i-1] + previous_row[i])
            pascal_row.insert(0, 1)
            pascal_row.insert(len(previous_row), 1)
            return pascal_row
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            previous_row = [1,1]
            for i in range(2, rowIndex+1):
                current_row = generate_pascal_row(i, previous_row)
                previous_row = current_row
            return current_row
            
