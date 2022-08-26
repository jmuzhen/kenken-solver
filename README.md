# kenken-solver
A fast KenKen solver, written in Python.

## KenKen game
The KenKen game is a variation of Sudoku. It has a square grid which can have any number of rows/columns. 
One example of a KenKen grid is this:

![4x4-72dc4cbbdf6703b668e89907cf51d79f](https://user-images.githubusercontent.com/61100393/186898244-cf5ede8e-4f27-494c-ae85-94e4439e2eb7.png)

## General rules of KenKen puzzles
A solution to a KenKen puzzle must meet the following conditions:
> 1. For a grid with `n` squares in each row and column, the numbers `1 to n` must be used for each row and column.

> 2. The numbers must not be repeated for each row and column.

For example, this is a valid grid:
```
1 2 3
2 3 1
3 1 2
```

> 3. KenKen grids are divided into smaller regions. The numbers in each region must produce a certain specified number when combined using a mathematical operation.

For example, if the text writen on the region is `7+`, then the numbers in the region must add up to 7; if the text is `24x` or `24*`, then the product of the numbers must be 24.

Numbers in a region may be repeated as long as they are in different rows and different columns.

> 4. As a general convention, a "proper" KenKen puzzle should only have one solution, although this is not compulsory.

**More information about the KenKen game can be found on the [Wikipedia page](https://en.wikipedia.org/wiki/KenKen).**

## Algorithm
This program uses the [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking); i.e. it loops through all possible iterations of the grid, and abandons a grid (skips to the next grid) as soon as it determines that a condition is not met.

## Usage
**Run `main.py`.**

First, input the size of the grid; for example, for a 4x4 grid, input `4`;

You will be prompted to enter an "instruction". This is the conditions that you see on each region of the KenKen puzzle.

For example, referring to this puzzle:

![4x4-72dc4cbbdf6703b668e89907cf51d79f](https://user-images.githubusercontent.com/61100393/186898244-cf5ede8e-4f27-494c-ae85-94e4439e2eb7.png)

As shown, the region that contains the squares `(1,1), (1,2), (2,2)` has the condition `16*`. You should input:
```
1,1 1,2 2,2 16*
```

*Note: The order of the squares does not matter. So `1,1 1,2 2,2 16*` is the same as `1,2 2,2 1,1 16*`. Also, `x` and `*` are interchangeable, both denoting multiplication.*

*Note 2: If you have entered the condition wrongly, correct the error by entering the previous line again. For example, if you have entered `1,1 1,2 2,2 14*` by mistake, just enter `1,1 1,2 2,2 16*` into the input line. The new input will override the existing one.*

You will keep being prompted to enter instructions until all the squares have been given a corresponding instruction. The program will then attempt to solve for a solution that meets all of the inputted instructions. If a solution is found, it will be outputted; if not, you will see message stating `No possible answers found.` 

## Running on [repl.it]()
There is an existing repl.it project created by me: https://replit.com/@JMuzhen/kenken-solver?v=1

To run it, click on the link and click on the `▶️ Run` button.

## If you have any queries, feel free to [open an Issue](https://github.com/jmuzhen/kenken-solver/issues/new).
