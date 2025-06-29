from pathlib import Path
from time import ctime
import shutil

script_dir = Path(__file__).parent
path = script_dir / "ecommerce" / "__init__.py"

# path = Path("ecommerce/__init__.py")
# path = Path() / "ecommerce" / "__init__.py"
# print(path.exists())
# print(path.rename("init.txt"))
# print(path.unlink())
# print(path)
print(path.stat())
print(ctime(path.stat().st_ctime))

# in this way we don't worry about openning and clossing the file.
# print(path.read_bytes())
# print(path.read_text())
# path.write_bytes()
# path.write_text("kjdfkdjf")

# Opening and closing file using open and with
# open("__init__.py", "r")
# with open("__init__.py", "r") as file:
#     ...


source = script_dir / "ecommerce" / "__init__.py"
target = script_dir / "myfile.py"

# this below method to copying the file is little bit TDS
# target.write_text(source.read_text())

shutil.copy(source, target)
