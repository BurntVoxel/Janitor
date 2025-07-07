import argparse
import os
import sys

def parse_args():
  parser = argparse.ArgumentParser(description="Janitor: Directory cleaning utility.")
  parser.add_argument(
    "path",
    nargs="?",
    default=None,
    help="Path to the working directory (default: current directory)",
  )
  parser.add_argument(
    "-v",
    dest="verbose",
    action="count",
    default=0,
    help="Increase verbosity. Use -vv for very verbose.",
  )
  args = parser.parse_args()

  # Prefer named argument if both are given
  raw_path = args.working_dir if args.working_dir is not None else args.path
  if raw_path is None:
    raw_path = os.getcwd()
  # Expand ~ and make absolute
  working_dir = os.path.abspath(os.path.expanduser(raw_path))
  if not os.path.isdir(working_dir):
    print(f"Error: '{working_dir}' is not a valid directory.", file=sys.stderr)
    sys.exit(1)
  return args


def main():
  args = parse_args()
  # Start with indexing the path

  # Verify this:
  FileIndex = {}
# <!> Left off here, look up how to use os.walk()
# end main()

if __name__ == "__main__":
  main()
