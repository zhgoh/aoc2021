import strutils as str # http://nim-lang.org/docs/strutils.html

proc getLines(file: string): seq[int] =
  let f = open(file)
  defer:
    f.close()

  var
    line : string
    lines : seq[int]

  while f.read_line(line):
    lines.add(str.parseInt(line))

  return lines

proc day_1a(lines: seq[int]): int =
  if len(lines) < 1:
    return 0

  var
    prev : int = lines[0]
    count : int

  for i in 1..len(lines)-1:
    let current = lines[i]
    if current > prev:
      count += 1
    prev = current
  return count

proc day_1b(lines: seq[int]): int =
  if len(lines) < 3:
    return 0

  let
    # Amount of sliding windows
    total = len(lines) - 2

  var
    prev = lines[0] + lines[1] + lines[2]
    count = 0

  for i in 1..total-1:
    let current = lines[i] + lines[i+1] + lines[i+2]
    if current > prev:
      count += 1
    prev = current
  return count

#let lines = @[199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
let lines = getLines("input")
echo day_1a(lines)
echo day_1b(lines)
