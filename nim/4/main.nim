import strutils as str # http://nim-lang.org/docs/strutils.html
#import sequtils

proc getLines(file: string): seq[string] =
  let f = open(file)
  defer:
    f.close()

  var
    line : string
    lines : seq[string]

  while f.read_line(line):
    lines.add(line)
  return lines


type
  Bingo = tuple[num_elem: int, board: array[25, int]]
  BingoList = tuple[numbers: seq[int], board: seq[Bingo]]
  Pair[T] = tuple[first: T, second: T]
  BoardInfo = tuple[index: int, lastNum: seq[int]]

proc bingo_add(bingo: Bingo, num: int): Bingo =
  var res = bingo
  res.board[res.num_elem] = num
  res.num_elem += 1
  assert res.num_elem <= 25
  return res

proc bingo_clear(bingo: Bingo): Bingo =
  var res = bingo
  res.num_elem = 0
  return res

proc bingo_check(items: seq[int], numbers: seq[int]): bool =
  for i in items:
    var exist = false
    for n in numbers:
      if i == n:
        exist = true
    if not exist:
      return false
  return true

proc bingo_unmarked_sum(bingo: Bingo, numbers: seq[int]): int =
  var sum = 0
  for i in bingo.board:
    var exist = false
    for n in numbers:
      if i == n:
        exist = true
        break
    if not exist:
      sum += i
  return sum

proc bingo_win(bingo: Bingo, numbers: seq[int]): seq[int] =
  for i in countup(0, 4):
    let col = @[
      bingo.board[i],
      bingo.board[i+5],
      bingo.board[i+10],
      bingo.board[i+15],
      bingo.board[i+20]]

    # Check vertical
    let v = bingo_check(col, numbers)
    if v:
      return col

    # Check horizontal
    let j = i * 5
    let row = @[
      bingo.board[j],
      bingo.board[j+1],
      bingo.board[j+2],
      bingo.board[j+3],
      bingo.board[j+4]]

    let h = bingo_check(row, numbers)
    if h:
      return row
  return @[]

proc bingo_all_win(all_bingo: seq[Bingo], numbers: seq[int]): Pair[BoardInfo] =
  var
    first: BoardInfo = (index: -1, lastNum: @[])
    last : BoardInfo = (index: -1, lastNum: @[])

  for i in countup(0, len(all_bingo)-1):
    let b = bingo_win(all_bingo[i], numbers)
    if len(b) > 0:
      if first.index == -1:
        first = (index: i, lastNum: b)
      last = (index: i, lastNum: b)
  return (first: first, second: last)

proc bingo_read_info(lines: seq[string]): BingoList =
  var
    numbers: seq[int]
    bingos: seq[Bingo]
    lines_read = 0
    bingo: Bingo

  for number in lines[0].split(','):
    numbers.add(parseInt(number))

  for i in countup(2, len(lines)):
    if lines_read == 5:
      lines_read = 0
      bingos.add(bingo)
      bingo = bingo_clear(bingo)
      continue

    let line = lines[i].splitWhitespace()
    for number in line:
      bingo = bingo_add(bingo, parseInt(number))
    lines_read += 1

  # echo "Numbers: ", numbers
  # echo "Bingos: ", bingos
  # echo "Bingos: ", len(bingos)
  return (numbers, bingos)


proc day_2a(bingoList: BingoList) : int =
  var numbers: seq[int]
  for num in bingoList.numbers:
    numbers.add(num)

    let win = bingo_all_win(bingoList.board, numbers)
    if win.first.index > 0:
      let sum = bingo_unmarked_sum(bingoList.board[win.first.index], numbers)
      return sum * num
  return 0

proc day_2b(bingoList: BingoList) : int =
  var
    lastIndex = -1
    lastNum   = 0
    lastNumbers: seq[int]

  for i in countup(0, len(bingoList.numbers) - 1, 5):
    let
      numbers = bingoList.numbers[i..i+4]
      win = bingo_all_win(bingoList.board, numbers)

    if win.second.index > 0:
      lastIndex = win.second.index
      lastNum = win.second.lastNums
      lastNumbers = numbers

  if lastIndex <= 0:
     echo "Error: No winners!!!"
     return 0

  echo "Last Index: ", lastIndex
  let sum = bingo_unmarked_sum(bingoList.board[lastIndex], lastNumbers)
  echo "Sum: ", sum
  return sum * lastNum

const
  useInput = false

when useInput:
  let lines = getLines("input")
else:
  let lines = @[
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "              ",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "             ",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "              ",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7"
  ]
let bingoList = bingo_read_info(lines)

echo day_2a(bingoList)
echo day_2b(bingoList)
