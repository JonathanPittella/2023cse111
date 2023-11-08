def main(file, ab, new_ab):
    text_list = read_list(file)
    if len(text_list) >= 72:
        text_list = text_list[1:71]
    elif text_list:
        text_list.por(0)

    count_ab = text_list.count("Alberta")

    print(text_list)
    print()
    print(f"Total number of 'Alberta':{count_ab}")

def read_list(provinces):
    text_list = []

    # Read the content of the file and store each line as a separate element in the list
    with open(provinces, "r") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list

file = "Week 9/provinces.txt"

file = "Week 9/provinces.txt"
ab = "AB"
new_ab = "Alberta"

if __name__ == "__main__":
    main(file, ab, new_ab)



