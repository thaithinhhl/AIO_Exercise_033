def exercise1(tp, fp, fn):
    # Check if inputs are integers
    if not isinstance(tp, int):
        print("tp must be inta")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return

    # Check if inputs are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    # Calculate precision, recall, and F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Print the results
    print(f"precision is {precision:.10f}")
    print(f"recall is {recall:.10f}")
    print(f"f1-score is {f1_score:.10f}")


# Example usage
exercise1(2, 3, 4)
exercise1('a', 3, 4)
exercise1(2, 'a', 4)
exercise1(2, 3, 'a')
exercise1(2, 3, 0)
exercise1(2.1, 3, 4)
