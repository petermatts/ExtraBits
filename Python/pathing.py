from pathlib import Path

# the path to this file
path = Path(__file__)

# full path, resolve call handles things like ../
print(path.resolve().absolute())

# just this file/directory
print(path.name)

# file extension
print(path.suffix)

# file name without extenssion
print(path.stem)

# each part of the path split up as an array
print(path.parts)

# Go up a level
print(path.parent)
print(path.parents[0]) # number in brackets says how many parent levels 0 indexed

# Current working directory
print(path.cwd())

# checks if the path exists
print(path.exists())

# checks if the path is file
print(path.is_file())

# checks if the path is a directory
print(path.is_dir())

# creates the current directory
# path.mkdir(parents=True, exist_ok=True)

# path stats
print(path.stat())

# fill in more as needed...

# unlink deletes a file, rmdir removes a directory
# print(path.unlink())