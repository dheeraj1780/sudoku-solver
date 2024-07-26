class Box:
    def __init__(self, matrix, box_id):
        self.box = matrix
        self.box_id = box_id
        self.empty_subBox_ids = self.emptySubBoxes()

    def emptySubBoxes(self):
        subBoxesList = []
        for i in range(3):
            for j in range(3):
                if self.box[i][j] == 0:
                    index = [i, j]
                    subBoxesList.append(index)
        return subBoxesList

def is_valid(boxes, boxid, index, num):
    # Check the box
    box = boxes[boxid - 1].box
    for i in range(3):
        for j in range(3):
            if box[i][j] == num:
                return False
    
    # Check the row
    row_start = (boxid - 1) // 3 * 3
    for box_idx in range(row_start, row_start + 3):
        for j in range(3):
            if boxes[box_idx].box[index[0]][j] == num:
                return False
    
    # Check the column
    col_start = (boxid - 1) % 3
    for box_idx in range(col_start, 9, 3):
        for i in range(3):
            if boxes[box_idx].box[i][index[1]] == num:
                return False

    return True

def solve_sudoku(boxes):
    empty_positions = []

    for box in boxes:
        for i, j in box.empty_subBox_ids:
            empty_positions.append((box.box_id, i, j))

    def solve():
        if not empty_positions:
            return True
        
        box_id, row, col = empty_positions.pop(0)
        box = boxes[box_id - 1]
        
        for num in range(1, 10):
            if is_valid(boxes, box_id, (row, col), num):
                box.box[row][col] = num
                if solve():
                    return True
                box.box[row][col] = 0
        
        empty_positions.insert(0, (box_id, row, col))
        return False

    solve()

def print_sudoku(boxes):
    for i in range(0,,3):
        for j in range(3):
            print(boxes[i].box[j]+boxes[i+1].box[j]+boxes[i+2].box[j])

# Define the initial Sudoku boxes
box1 = Box([[4, 5, 0], [0, 0, 2], [0, 0, 0]], 1)
box2 = Box([[0, 0, 0], [0, 7, 0], [0, 0, 0]], 2)
box3 = Box([[0, 0, 0], [6, 3, 0], [0, 2, 8]], 3)
box4 = Box([[0, 0, 0], [0, 8, 6], [0, 2, 0]], 4)
box5 = Box([[9, 5, 0], [0, 0, 0], [6, 0, 0]], 5)
box6 = Box([[0, 0, 0], [2, 0, 0], [7, 5, 0]], 6)
box7 = Box([[0, 0, 0], [0, 7, 0], [0, 0, 8]], 7)
box8 = Box([[0, 0, 0], [0, 4, 5], [0, 0, 9]], 8)
box9 = Box([[4, 7, 6], [0, 0, 0], [0, 0, 0]], 9)

boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
solve_sudoku(boxes)
print_sudoku(boxes)
