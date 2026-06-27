def find_runner_up():
    try:
        scores = [2, 3, 6, 6, 5]
        
        unique_scores = list(set(scores))
        unique_scores.sort(reverse=True)
        
        if len(unique_scores) > 1:
            print(unique_scores[1])
        else:
            print("No runner-up found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_runner_up()