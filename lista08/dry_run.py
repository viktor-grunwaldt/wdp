def get_data():
    print("Getting data...", end=" " , flush=True)
    with open("data/slowa.txt", "r") as file:
        data = file.read().splitlines()
    print("Data loaded")
    print(len(data), "words loaded")

get_data()