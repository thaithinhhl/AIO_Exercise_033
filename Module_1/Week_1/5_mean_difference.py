def md_nre_single_sample(y, y_hat, n, p):
    if n <= 0 or p <= 0:
        print("n and p must be positive integers")
        return

    # Calculate the MD_nRE
    term1 = abs(y) ** (1/n)
    term2 = abs(y_hat) ** (1/n)
    md_nre = abs(term1 - term2) ** p

    return md_nre


# Example usage
print(
    f"md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1) = {md_nre_single_sample(100, 99.5, 2, 1)}")
print(
    f"md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1) = {md_nre_single_sample(50, 49.5, 2, 1)}")
print(
    f"md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1) = {md_nre_single_sample(20, 19.5, 2, 1)}")
print(
    f"md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1) = {md_nre_single_sample(0.6, 0.1, 2, 1)}")
