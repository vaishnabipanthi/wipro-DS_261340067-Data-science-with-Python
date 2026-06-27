def sort_colors():
    colors = input("Sample input: ")
    color_list = colors.split('-')
    color_list.sort()
    sorted_colors = '-'.join(color_list)
    print(f"Sample output: {sorted_colors}")

if __name__ == "__main__":
    sort_colors()