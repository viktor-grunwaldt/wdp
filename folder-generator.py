import os

for i in range(1,14):
    try:
        os.mkdir(f"lista{i:02}")
    except FileExistsError as e:
        print(e)
