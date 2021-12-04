class Board:
    def __init__(self, rows) -> None:

        # set of numbers on the board
        self.numbers = set([num for row in rows for num in row])

        # set of numbers marked / hit
        self.marked = set()

        # all possible rows and columns
        self.data = rows + list(map(list, zip(*rows)))

        # final score after all numbers in a given row/column are marked
        self.final_score = 0

    def check(self, num):
        if num in self.numbers:
            self.marked.add(num)

            for entry in self.data:
                entry[:] = [x for x in entry if x != num]
                if not entry:
                    self.calculate_score(num)
                    return True

        return False

    def calculate_score(self, num):
        self.final_score = sum((self.numbers - self.marked)) * num


with open("input.txt", "r") as bingo_data:
    boards = []
    rows = []

    lines = bingo_data.readlines()

    for e, line in enumerate(lines):
        # get draws
        if e == 0:
            draws = list(map(int, line.split(",")))
            continue

        # get bingo board row and add to rows
        if line.strip():
            rows.append(list(map(int, line.strip().replace("  ", " ").split(" "))))

        # create new bingo board based on found rows if an empty line is encountered
        # or end of bingo data is reached
        if not line.strip() or e == len(lines) - 1:
            if rows:
                boards.append(Board(rows))
            rows = []


last_winning_board = None

for num in draws:
    found = []
    for board in boards:
        if board.check(num):
            found.append(board)

    for board in found:
        last_winning_board = board
        boards.remove(board)


print(f"Last winning board with final score of: {last_winning_board.final_score}")
