# AtCoder

BeginnerContest

001

B: 四捨五入したいときは、Decimalに変換してからfloatにする必要がある

D: ソートして比較して、カバーしてない範囲がきたら出力

012

B: 0埋め複数 print('%02d:%02d:%02d' % (hh, mm, ss))

027

B: 解けなかった

030

B: AngleH = 30.0 * H + 0.5 * M. AngleM = 6.0 * M 時計苦手

046

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
B: 回転行列, ベクトル

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

183

B: 相似 A:B = C:D, AD = BC

187

A: 文字列をそれぞれ１文字のリストにし、整数にする map(int, str(A))

189

B: 不動小数点の演算は誤差を含むから両辺に100かけて整数演算する

194

B: 1行if res = min(res, A[i] + B[j] if i == j else max(A[i], B[j]))

195

B: 解けなかった. A * 個数 <= W <= B * 個数の範囲で最小と最大求める

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

221

C: 最大値を達成する分離の仕方において、分離後の2変数は数字列として見た時に単調非増加. bit全探索を使って2 ^ 9で調べられる. -> bitが立ってるところがleft, 立ってないとこがright ans = max(ans, left * right)

227

C: 解けなかった. 計算量をルートで見積もれなかった.

220

B: NをK進法に変える int(str(N), K) ex) int("101", 2) -> 5

223

C: 解けなかった. ぶつかる時間を求める -> 時間が0になるまで左から足していく. ans += min(A[i], t * B[i]), t -= min(t, A[i] / B[i]) 

226

B: Setにはタプルが入れられる
D: 解けなかった. (x + 2, y + 4)の移動はxに1を2回, yに2を2回足せばいける. つまりGCDで割ったものをsetにつめる.

229

D: 解けなかった. 累積和 + 尺取法.

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

234

D: heapqを使う. heapq.heapify([3, 2, 1])で, 最小になるように入れ替える.

235

C: 辞書に複数の値を入れる. B = defaultdict(list)
E: クラスカル法でクエリ先読み, print(*ans, sep="\n")で配列の中身全部

236

B: 一つだけ奇数個しか現れない数があったらXORで求められる
C: if s in T:とやるとき, TがListだったらO(N), SetだったらO(logN)かかる
D: 2次元配列: [list(map(int, input().split())) for _ in range(2 * n - 1)]. 二人選ぶときは, indexの小さい方から１個見つけて, ループを抜けて. そのindex + 1からもう片方を見つけるというdfs.

237

D: 逆から見てdequeue
E: ポテンシャルを使ったダイクストラ

238

D: 解けなかった. x XOR y = x + y - 2(x AND y). x XOR y AND x AND y == 0

RegularContest

133

GrandContest

015:

A: 解けなかった. 5 + 5と4 + 6が一緒でという考えでなく、作れる数の範囲を考える.

017: 

A: 解けなかった. 数列の中に奇数があった場合、それ以外を足して、その奇数を含むか含めるかで偶数奇数を決めれる. 偶数も奇数も2^(N-1)通りの選び方がある.

023: 

A: 解けなかった. 部分列とか連続するというキーワードがあったら累積和を取る.

026

A: forの中のiを飛ばす時は、forではなくwhileを使う

A: 整数の辞書順を勘違いしない. [999, 1000, 1001, 1002]から1個とった最小の辞書順は[999, 1000, 1001]

031:

A: 解けなかった. 位置を変えずにアルファベットを選ぶときは、選ぶ選ばないで考える.

046:

A: 解けなかった. 角度を360回ずらせば元の位置に戻る.

MathAndAlgorithm

018: 辞書を使う時は, defaultdict(int)が良い. key見つからなくても0が入るから.

026: 期待値計算わからない

032: 二分探索. index = bisect_left(A, X) Xより１個先のindex

033: ベクトルの内積, 外積

035: 解けなかった. 交差する場合がわからなかった.

036: 解けなかった. 余弦定理, もしくは座標を求めて距離求める. 角度の求め方(radian): theta = math.radians(alpha)

Typical90

004: list(zip(*grid))は遅い.

010: SegTreeの[l, r)に注意.

020: 解けなかった. log2(a) = b * log2(c) log2が取れる -> a = c ** b

022: GCDまではよかったが解けなかった.

032: 解けなかった. (a, b) (c, d)と、ペアで考える時は順列生成して二つずつ取っていく.

033: 解けなかった. 問題の意味がわからなかった.

055: 解けなかった. nC5のときは100 ** 5まで通る. 2 ^ 63 - 1を超えると計算に時間がかかりTLEの原因になる. 時間制限厳しいやつはmainを無くす.

061: dequeueの検索はO(1) q[x - 1]

jsc2021

A: 切り上げはmath.ceil(x)

code-festival-2016-qualc

A: S.rindex("F")で, 右から最初に見つかるindexを返す

nomura2020

B: 解けなかった.

nikkei2019-qual

B: 解けなかった.

code-festival-2017-quala

B: 解けなかった. ボタン操作で反転させるやつは k * (M - l) + l * (N - k)で白黒の数カウントできる.

code-festival-2017-qualc

B: 想定解法で解けなかった. 各A[i]に対して、A[i]が偶数のときは,A[i] - 1, A[i] + 1は奇数. 3^N - 2^eが答え. eはA[i]が偶数であるiの個数をeとする.