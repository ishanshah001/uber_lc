class Solution:
    def rotateTheBox(self, box):
        rows, cols = len(box), len(box[0])

        # Step 1: Apply gravity to each row
        for r in range(rows):
            empty_spot = cols - 1  # rightmost available spot for a stone
            for c in range(cols - 1, -1, -1):
                if box[r][c] == '#':
                    box[r][c], box[r][empty_spot] = '.', '#'
                    empty_spot -= 1
                elif box[r][c] == '*':
                    empty_spot = c - 1  # reset to just before obstacle

        # Step 2: Rotate 90 degrees clockwise
        rotated = [[None] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = box[r][c]

        return rotated