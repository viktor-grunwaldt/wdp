import os
import requests


def main():
    if not os.path.isfile("lalka.txt"):
        try:
            result = requests.get("https://wolnelektury.pl/media/book/txt/lalka-tom-pierwszy.txt")
            data = result.text
        except Exception as e:
            print("fetching the book failed")
            print(e)
            return

        with open("lalka.txt", "w") as f:
            f.write(data)
    else:
        with open("lalka.txt", "r") as f:
            data = f.read()


if __name__ == "__main__":
    main()
