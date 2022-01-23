# AtCoder

BeginnerContest

001

B: 四捨五入したいときは、Decimalに変換してからfloatにする必要がある

D: ソートして比較して、カバーしてない範囲がきたら出力

46

A: 被ってる数はsetを使う

050

A: 10 + 10のような入力のときはa, o, b = input().split() または eval(input())

093:

A: ''.join(sorted(list(input())))

100:

B: 問題の意味がわからなかった

107:

B: all()は配列の中が全てTrueならTrue. list(zip(*field)）で、縦の配列を作れる

108

A: 組み合わせは掛け算

110

A: 降順 sorted(A, reverse=True)

111

A: 改行せずに出力 print(1, end='')

148

A: 入力で、横並びのA Bと縦並びのA Bのどっちか確認

156

B: NをK進数で表すとき np.base_repr(N, K))

161

B: 以上か未満を確認してから切り捨てを行う total // (4 * M)なのか、 -(-total // (4 * M)). もしくは両辺に4M掛けて少数計算をしない

162

A: math.pi

170

B: 2n + 4m = Y, n + m == Xのときは, 2X <= Y <= 4X and Y % 2 == 0

171

A: 大文字小文字の判定はstr.islower(), str.isupper()

187

A: 文字列をそれぞれ１文字のリストにし、整数にする map(int, str(A))

189

B: 不動小数点の演算は誤差を含むから両辺に100かけて整数演算する

197

A: index1とindex3のswapはindex2からindex3の文字列にindex1を足したもの S[1:] + S[0]

198

B: 同じ文字列のrepeatは "0" * N

200

A: 切り上げ -(-N // 100), 切り捨て N // 100

206

A: 除算の切り捨て //を使う

208

B: 階乗はfrom math import factorialのfactorialで計算

219

B: １行で配列に詰める S = [input() for _ range(3)]. 文字列を結合して表示 print("".join(A))

220

B: NをK進法に変える int(str(N), K)

226

B: Setにはタプルが入れられる

231

C: 二分探索

D: Union-Find

232

B: chr(65)で整数に対応するUnicodeに, ord('a')でUnicodeに対応する整数に変換するのをうまく使う

C: permutationを使う

D: BFSか、DP

233

D: HashMapのlogN検索を使って計算量を少なくする

E: 多倍長演算を一番小さい桁から繰り上げをうまく計算して実装

235

C: 辞書に複数の値を入れる. B = defaultdict(list)
E: クラスカル法でクエリ先読み, print(*ans, sep="\n")で配列の中身全部

236

B: 一つだけ奇数個しか現れない数があったらXORで求められる
C: if s in T:とやるとき, TがListだったらO(N), SetだったらO(logN)かかる
D: 2次元配列: [list(map(int, input().split())) for _ in range(2 * n - 1)]. 二人選ぶときは, indexの小さい方から１個見つけて, ループを抜けて. そのindex + 1からもう片方を見つけるというdfs.

RegularContest

133

A: 整数の辞書順を勘違いしない. [999, 1000, 1001, 1002]から1個とった最小の辞書順は[999, 1000, 1001]