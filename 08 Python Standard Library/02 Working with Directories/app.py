from pathlib import Path

script_dir = Path(__file__).parent
path = script_dir / "ecommerce"
# path = Path("ecommerce")
# print(path.exists())
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path)
# print(path.iterdir())
# print(Path.cwd())
# print(path.exists())
# for p in path.iterdir():
#     print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# Search files by pattern
# py_files = [p for p in path.glob("/**/*.py")]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
