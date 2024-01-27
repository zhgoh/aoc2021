import strutils as str # http://nim-lang.org/docs/strutils.html

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

proc day_2a(lines: seq[string]) : int =
  var
    horizontal = 0
    depth = 0

  for line in lines:
    let instructions = line.split(' ')
    if len(instructions) != 2:
      echo "Error, instructions have no units"
      break
    let units = str.parseInt(instructions[1])
    case instructions[0]:
      of "down":
        depth += units
      of "up":
        depth -= units
      of "forward":
        horizontal += units
      else:
        echo "Unknown instructions"
  return depth * horizontal


proc day_2b(lines: seq[string]) : int =
  var
    horizontal = 0
    depth = 0
    aim = 0

  for line in lines:
    let instructions = line.split(' ')
    if len(instructions) != 2:
      echo "Error, instructions have no units"
      break
    let units = str.parseInt(instructions[1])
    case instructions[0]:
      of "down":
        aim += units
      of "up":
        aim -= units
      of "forward":
        horizontal += units
        depth += aim * units
      else:
        echo "Unknown instructions"
  return depth * horizontal

let lines = getLines("input")
#let lines = @[
#  "forward 5",
#  "down 5",
#  "forward 8",
#  "up 3",
#  "down 8",
#  "forward 2"
#]
echo day_2a(lines)
echo day_2b(lines)
