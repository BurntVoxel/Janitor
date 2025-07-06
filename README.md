# Janitor
Drive cleanup utility. Deduplication, mostly.

Plan:
- Take working path as argument (default to current path)
- Multiple scan levels:
  - Light: Just file names and dates
  - Heavy: Also checksums
- Index: Run breadth-first search and store the file index.
  - *Scan inside archives! Important!*
- Use a config file for what to ignore, what to assume is trash, etc.
- Analyze list for cleanup actions.
  - Deduplicate: Show sets of files with matching names.
    - Three lists: Matching checksums, Matching stats, Matching name.
    - UI: Offer to add patterns to Ignore or Hitlist
    - UI: ask what to do with each file: Keep all, Keep one, Delete all
  - Take out trash:
    - Check config files for where to clean up and expiration date.
    - Default to check Trash, Downloads, Desktop
    - Delete anything that hasn't been modified for too long.
  - Dusting: Delete known junk files found in hitlist
    - Multiple sublists for multiple types.
    - Cache,
    - Thumbnails
    - Backup versions...
