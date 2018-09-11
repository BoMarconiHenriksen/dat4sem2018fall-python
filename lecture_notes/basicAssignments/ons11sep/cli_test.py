"""
Hvordan får du fadt i det som du samler alle linjer ind og samler dem op
"""

import sys

input_lines = sys.stdin.read().split('\n')  # får en liste
output_lines = reversed(input_lines)  # får en omvendt list

# for at skrive noget ud skal deet være en string
output_lines_str = '\n'.join(output_lines)
sys.stdout.write(output_lines_str)

# cat bog.txt | python cli_replace.py sherlock helge | python cli_filter ui

# 'a' in hello
