def count_cases(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"No. of Upper case characters : {upper}")
    print(f"No. of Lower case Characters : {lower}")

if __name__ == "__main__":
    sample_str = "The quick Brow Fox"
    count_cases(sample_str)