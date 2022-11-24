import sys


# 先别想太复杂，搞 最大公约数、多个分数 聚合之类的，就直接拆，也能过
def egypt_score(s: str):
    numerator, denominator = s.split("/")
    out_s = ""
    for i in range(int(numerator)):
        if i != int(numerator) - 1:
            out_s += "1/" + denominator + "+"
        else:
            out_s += "1/" + denominator
    print(out_s)


for line in sys.stdin:
    egypt_score(line.strip())
