from pathlib import Path
from zipfile import ZipFile

script_dir = Path(__file__).parent
# Method 1:
# zip = ZipFile(script_dir/"files.zip", "w")
# for path in (script_dir/"ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()

# Method 2:
# with ZipFile(script_dir/"files.zip", "w") as zip:
#     for path in Path(script_dir/"ecommerce").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
