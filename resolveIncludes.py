### Quick and dirty find-n-replace for \include{}
import re
import sys

include = r'^\\include{([a-zA-Z0-9]+)}$'

def substitute(filename, stack=[]):
  current = [*stack, filename]
  if filename in stack:
    raise RecursionError(f'Cyclic \include detected {" -> ".join(current)}')

  print(f'Resolving \include commands in {filename}')

  lines = []
  f = open(filename)
  for line in f.readlines():
    m = re.match(include, line)
    if m:
      lines.extend(substitute(f'{m.group(1)}.tex', current))
    else:
      lines.append(line)
  return ''.join(lines)

def main(initialFile, outputFile):
  newFile = substitute(initialFile)
  f = open(outputFile, 'w')
  f.write(newFile)
  f.close()

if len(sys.argv) != 3:
  raise ValueError(f'Wrong number of args. Expected usage: python3 script.py <entry> <output>')

[_, entryFile, outFile] = sys.argv

print(f'Entry: {entryFile}')
print(f'Out: {outFile}')

main(entryFile, outFile)