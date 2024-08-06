from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    board = [[0]*9 for _ in range(9)]
    if request.method == 'POST':
        if 'solve' in request.form:
            board = [[int(request.form.get(f'cell-{row}-{col}', 0) or 0) for col in range(9)] for row in range(9)]
            solve_sudoku(board)
        elif 'reset' in request.form:
            return redirect(url_for('index'))
    return render_template('index.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)
