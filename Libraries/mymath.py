import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

# ベクトル(ax, ay)と(bx, by)の外積の大きさ
# 外積が0 = 数直線上
# 外積が正 = A, B, Cと時計回り
# 外積が負 = A, B, Cと半時計回り
def cross(ax, ay, bx, by):
    return ax * by - ay * bx

# 線分ABと線分CDが交差してるかどうか
def is_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    crossABC = cross(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
    crossABD = cross(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
    crossACD = cross(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
    crossBCD = cross(x4 - x3, y4 - y3, x2 - x3, y2 - y3)

    #一直線上に並んでる
    if crossABC == 0 and crossABD == 0 and crossACD == 0 and crossBCD == 0:
        A = (x1, y1) # 点Aの座標
        B = (x2, y2) # 点Bの座標
        C = (x3, y3) # 点Cの座標
        D = (x4, y4) # 点Dの座標

        if A > B:
            tmp = B
            B = A
            A = tmp
        if C > D:
            tmp = D
            D = C
            C = tmp

        # A - B - C - DとC - D - A - B以外のケース
        if max(A, C) <= min(B, D):
            return True
        else:
            return False
    else:
        # 線分ABに対して, Cが時計回り, Dが反時計回り or Cが反時計回り, Dが時計回りかどうか
        check_a = False

        # Cが時計回り, Dが半時計回り
        if crossABC >= 0 and crossABD <= 0:
            check_a = True
        # Cが半時計回り, Dが時計回り
        if crossABC <= 0 and crossABD >= 0:
            check_a = True

        # 線分CDに対して, Aが時計周り, Bが半時計回り or Aが反時計回り, Bが時計回りかどうか
        check_b = False

        # Aが時計周り, Bが半時計回り
        if crossACD >= 0 and crossBCD <= 0:
            check_b = True

        # Aが反時計回り, Bが時計回り
        if crossACD <= 0 and crossBCD >= 0:
            check_b = True

        if check_a and check_b:
            return True
        else:
            return False

# 長針と短針の角度を求める
def clock_theta(h, m):

    # 短針の角度
    h_theta = 30 * h + 0.5 * m

    # 長針の角度
    m_theta = 6 * m

    return math.radians(h_theta - m_theta)

# 二つの円の状態を返す
def circle(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 2 つの円の内部に共通部分は存在しないが、2 つの円は接している
    if d == r1 + r2:
        return 4

    # 一方の円が他方の円を完全に含み、2 つの円は接している
    elif d == abs(r1 - r2):
        return 2

    # 2 つの円の内部に共通部分は存在せず、2 つの円は接していない
    elif d > r1 + r2:
        return 5

    # 2 つの円が互いに交差する
    elif d > abs(r1 - r2):
        return 3

    # 一方の円が他方の円を完全に含み、2 つの円は接していない
    else:
        return 1

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()


if __name__ == "__main__":
    main()
