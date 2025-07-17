from typing import List


class PascalsTriangle:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for numRow in range(numRows):  # numRow is the current row index

            row = [1]

            if numRow > 0:

                for idx in range(1, numRow): # idx is the current index in the row 
                    
                    row.append(prevRow[idx-1] + prevRow[idx])
                row.append(1) # Append 1 at the end of the row
                
                prevRow = row # Save the current row as the previous row for the next iteration
            triangle.append(row)
        
        return triangle
    

sol = PascalsTriangle()
print(sol.generate(1))  # Example usage
