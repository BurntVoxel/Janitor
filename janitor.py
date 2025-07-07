import argparse
import os
import re
import sys

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description="File cleanup helper.")
  parser.add_argument(
    "working_dir",
    nargs="?",
    default=None,
    help="Path to the working directory (default: current directory)",
  )
  parser.add_argument(
    "-c",
    "--case-insensitive",
    action="store_true",
    help="Enable case-insensitive filename comparison",
  )
  parser.add_argument(
    "-v",
    "--verbose",
    dest="verbosity",
    action="count",
    default=2,
    help="Increase verbosity. Use -vv for very verbose.",
  )
  parser.add_argument(
    "-q",
    "--quiet",
    dest="quietness",
    action="count",
    default=0,
    help="Decrease verbosity. Use -qq for very quiet.",
  )
  parser.add_argument(
    "-t",
    "--test",
    action="store_true",
    default=True,
    dest="test_mode",
    help="Run in test mode (no changes made)"
  )
  args = parser.parse_args()

  # Combine verbosity and quietness
  args.verbosity = args.verbosity - args.quietness

  # If no working_dir is given, use current directory
  raw_path = args.working_dir
  if raw_path is None:
    raw_path = os.getcwd()
  # Expand ~ and make absolute
  working_dir = os.path.abspath(os.path.expanduser(raw_path))
  if not os.path.isdir(working_dir):
    print(f"Error: '{working_dir}' is not a valid directory.", file=sys.stderr)
    sys.exit(1)
  args.working_dir = working_dir  # Ensure main() always gets a valid path
  return args


def main() -> None:
  args = parse_args()
  print("<!> NOT FUNCTIONAL YET <!>")

  # Function to normalize filenames for similarity comparison.
  # Strips punctuation, numbers, underscores, and "copy" (case-insensitive) from the base name, but keeps the extension.
  # Returns the cleaned name in lowercase for better matching.
  def scrub_filename(file, case_insensitive=True):
    name, ext = os.path.splitext(file)
    name = re.sub(r'[\W\d_]+', ' ', name, flags=re.UNICODE)
    name = re.sub(r'\bcopy\b', "", name, flags=re.IGNORECASE)
    name = name.strip()
    if args.case_insensitive:
      name = name.lower()
      ext = ext.lower()
    return f"{name}{ext}"

  # Start with indexing the path
  # Output needs to be an array of objects with
  #  {full_path, clean_name, size, mod_time, create_time}.
  all_files = []
  filewalker = os.walk(args.working_dir)
  for dirpath, dirnames, filenames in filewalker:
    if args.verbosity >= 1:
      print(f"\nScanning directory: {dirpath}")
    for file in filenames:
      entry = {
        "full_path": os.path.join(dirpath, file),
        "clean_name": scrub_filename(file),
        "size": os.path.getsize(os.path.join(dirpath, file)),
        "mod_time": os.path.getmtime(os.path.join(dirpath, file)),
        "create_time": os.path.getctime(os.path.join(dirpath, file))
      }
      all_files.append(entry)
      if args.verbosity >= 2:
        for key, value in entry.items():
          print(f"  {key}: {value}")
        print("")
    print(all_files)

  if args.verbosity >= 1: print("\nIndexing complete. Now sorting...")
  # Next: Sorting phase

  # Next: Human review

  # Next: Cleanup phase

# end main()

if __name__ == "__main__":
  main()
