class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue 
                
                box_id = (i//3,j//3)

                if val in rows[i] or val in columns[j] or val in boxes.get(box_id,set()):
                    return False 

                rows[i].add(val)
                columns[j].add(val)
                boxes.setdefault(box_id, set()).add(val)
        return True