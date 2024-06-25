import codecs
import sys

# Thay đổi mã hóa đầu ra của sys.stdout để hỗ trợ Unicode
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    # Tạo một bảng 2D để lưu trữ kết quả của các tính toán con
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo hàng đầu tiên và cột đầu tiên
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Tính toán khoảng cách Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Xóa ký tự
                               dp[i][j - 1] + 1,    # Thêm ký tự
                               dp[i - 1][j - 1] + 1)  # Thay thế ký tự

    return dp[m][n]


# Ví dụ kiểm tra
s = "kitten"
t = "sitting"
print("Khoảng cách Levenshtein giữa '{}' và '{}' là: {}".format(
    s, t, levenshtein_distance(s, t)))
