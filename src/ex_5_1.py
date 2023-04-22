"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__=='__main__':
    parser=argparse.ArgumentParser(
    description='ArgumentParser OBjecct')
    parser.add_argument('infile',help='positional argument--> INFILE')
    args=parser.parse_args()
    btf.line_count(args.infile)
