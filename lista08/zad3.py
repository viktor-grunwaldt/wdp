import numpy as np
alpha = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
alpha_dict = dict(zip(alpha, range(99)))
def frequency_count(s) -> np.array:
    frequency_counter = np.zeros(len(alpha))
    for c in s:
        frequency_counter[alpha_dict[c]] += 1
    
    return frequency_counter
        
def main():
    
    with open("data/popularne_slowa.txt", "r") as f:
        slowa = (f.readlines())
    

if __name__ == "__main__":
    main()