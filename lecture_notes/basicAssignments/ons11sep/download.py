"""
if no parameter are given

Usage:
    python download.py [<url>] [<file_name>] #[ ] betyder optional.
"""
from urllib import request as req
import os
import sys


def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


if __name__ == '__main__':
    try:
        # Ingen fejl hopper exception og try over og går til download().
        _, url, file_name = sys.argv
    except:
        try:
            _, url = sys.argv
            # basename tager det sidst i urlen
            # dirname tager det første i urlen
            file_name = os.path.basename(url)
        except Exception as e:
            try:
                # _, url = sys.argv
                # basename tager det sidst i urlen
                # dirname tager det første i urlen

                # Open file og læse den
                cfg_file = 'list_of_files.txt'
                with open(cfg_file) as fp:  # Åbner en fil.
                    for line in fp:
                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)  # stop program. Alt gik godt.
            except:
                #raise e
                print(__doc__)
                sys.exit(1)
    download(url, file_name)

    # study_in_Scarlet_url = 'https://www.gutenberg.org/files/244/244-0.txt'
    # Hvilke argumenter har vi.
    # print(sys.argv)
    # if len(sys.argv == 3):
#    windows_tmp = 'C:\Users'
    # file_name = 'study_in_Scarlet_url.txt'


# Til at bygge path med lige meget om os er windows, linux eller mac.
#    os.path.join('a', 'b')
