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

proc day_2a(lines: seq[int]) : int =
  return 0

proc day_2b(lines: seq[int]) : int =
  return 0

let lines = getLines("input")
echo day_2a(lines)
echo day_2b(lines)
