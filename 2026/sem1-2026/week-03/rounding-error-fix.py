# compare within a tiny range
# 1e-10 = 1 * 10^-10 = 0.0000000001
eps = 1e-10
0.2 - eps <= 1.2 - 1.0 <= 0.2 + eps

# or use the round() function
## round(1.2 - 1.0, 10) == 0.2

