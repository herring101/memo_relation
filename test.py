import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
topic_list = []
# ./docs/*.mdをすべて読み込みtopic_listに格納する(ディレクトリは無視する)
for filename in os.listdir("./docs"):
    if not filename.endswith(".md"):
        continue
    with open("./docs/{}".format(filename), "r") as f:
        data = f.readlines()
        topic_list.append(data[0].strip()[2:])

query = """
以下はプログラミングを学んでいる方のmarkdown形式のメモです。
これと同じような感じになるように、何かほかのプログラミングに関するテーマを出力してください。日本語でお願いします。出力するのはメモの内容だけで構いません（「以上が○○に関するメモでございます」とかの説明はいらない）
すでに出力されたテーマは出力しないようにしてください。
すでに出力されたテーマ一覧：{}

```md
# OpenACC Programming 1章

## アクセラレータ

一般的には、処理を向上させるためのハードウェアソフトウェア
「並列処理」によるスループットの高速化（ループ構造に有効）
スループット：単位時間あたりの処理量
アクセラレータ：GPU,Xeon Phi,APUなど
オフロード：CPUに変わって処理させること
CPUとGPUの使用するメモリはPCIバスで高速なデータ転送が行われている

## CPUとアクセラレータ

アクセラレータ（GPU）は動作周波数が極めて低い
SIMD（ベクトル処理）、MIMD（スレッド並列処理）が可能
in-orderで実行処理を行う。命令の並び順を変えることはできない
ベクトル型は、複数のデータに対して同じ命令を同時に実行できる。

## いろいろなアクセラレータ・デバイス

NVIDIA Kepler、Intel Xeon Phi、AMD GPU

## アクセラレータ用のプログラミングモデル

以下から、アクセラレータ・デバイスを「デバイス」と呼ぶ
CPU側のデータをデバイス側に渡す→デバイスが処理→デバイスからCPU側に渡す
このような処理は複雑になるが、できる限り使いやすくしたのがOpenACC
OpenMP4.0のほうは、その規約に適しているデバイスはXeon Phiのみ
OpenACCはマルチベンダーデバイスの仕様策定がなされている。
OpenACCは「プログラム互換性」だけではなく、「性能互換性」も重視している
directivesやclausesを使って、デバイスの性能を引き出すことができる

## オフロード形式のプログラミングモデルの合理性

何でもかんでもアクセラレータにオフロードするのは無駄が多い
「動作クロック周波数」が低いので、処理時間がかかる
```
""".format(
    str(topic_list)
).rstrip()
n = 3

for i in range(3):
    print("topic_list: {}".format(str(topic_list)))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
        ],
    )
    reply = response["choices"][0]["message"]["content"]
    while response["choices"][0]["finish_reason"] != "stop":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query},
                {"role": "assistant", "content": reply},
            ],
        )
        reply += response["choices"][0]["message"]["content"]
        print("not stop")
    print(
        "reply{}: {}...{}".format(
            i, reply[:10].replace("\n", " "), reply[-10:].replace("\n", " ")
        )
    )

    # topic_listに追加する
    topic_list.append(reply.split("\n")[0][2:])

    # ランダムに14桁の数字を生成する
    filename = str(random.randrange(10**13, 10**14))

    # ファイルに保存する
    with open("./docs/{}.md".format(filename), "w") as f:
        f.write(reply)
