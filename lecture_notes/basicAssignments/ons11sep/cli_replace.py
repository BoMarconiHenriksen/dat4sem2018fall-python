import sys
# sys.stdin Den streamer. Er bedre end sys.stdin.read() da den læser hele filen til memory.

# output_lines = input_lines.replace('Sherlock', 'Helge')
input_lines = sys.stdin.read().split('\n')  # får en liste

for line in input_lines:
    if input_lines[line] == 'Sherlock':
        input_lines[line] == 'Helge'

output_lines_str = '\n'.join(input_lines)
sys.stdout.write(output_lines_str) 

for line in sys.stdin:
    print() 
