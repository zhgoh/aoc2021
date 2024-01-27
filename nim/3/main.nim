import strutils

proc getLines(file: string): seq[string] =
  let f = open(file)
  defer:
    f.close()

  var
    line: string
    lines: seq[string]

  while f.read_line(line):
    lines.add(line)

  return lines

proc day_2a(lines: seq[string]) : int =
  if len(lines) < 1:
    return

  var
    gamma = ""
    epsilon = ""
  for i in 0..len(lines[0]) - 1:
    var
      zero = 0
      one = 0
    for line in lines:
      let bit = parseInt($line[i])
      case bit:
        of 0:
          zero += 1
        of 1:
          one += 1
        else:
          echo "Error, bit not found"
    if zero > one:
      gamma.add("0")
      epsilon.add("1")
    else:
      gamma.add("1")
      epsilon.add("0")

  let g = fromBin[int](gamma)
  let e = fromBin[int](epsilon)
  return g * e

proc filter(lines: seq[string], mode: int): int =
  var
    lines = lines
    i = 0

  while len(lines) > 1:
    var
      zero: seq[int]
      ones: seq[int]

    for j in 0..len(lines)-1:
      let bit = parseInt($lines[j][i])
      case bit:
        of 0:
          zero.add(j)
        of 1:
          ones.add(j)
        else:
          echo "Error"
    i += 1
    let
      len_z = len(zero) - 1
      len_o = len(ones) - 1

    case mode:
      of 0: # Oxygen
       if len_z == len_o or len_o > len_z:
          for i in countdown(len_z, 0):
            lines.del(zero[i])
       else:
          for i in countdown(len_o, 0):
            lines.del(ones[i])
      of 1: # Carbon dioxide
       if len_z == len_o or len_z < len_o:
          for i in countdown(len_o, 0):
            lines.del(ones[i])
       else:
          for i in countdown(len_z, 0):
            lines.del(zero[i])
      else:
        continue

  return fromBin[int](lines[0])

proc day_2b(lines: seq[string]) : int =
  let o2 = filter(lines, 0)
  let co2 = filter(lines, 1)
  return o2 * co2

let lines = getLines("input")
#let lines = @[
#  "00100",
#  "11110",
#  "10110",
#  "10111",
#  "10101",
#  "01111",
#  "00111",
#  "11100",
#  "10000",
#  "11001",
#  "00010",
#  "01010"
#]
echo day_2a(lines)
echo day_2b(lines)
