# docs

メモの管理ツールです。
embeddingsで関連を抽出し、グラフを作成することができます。

## Usage

.envにOPENAI_API_KEYを設定する

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

VSCodeのタスクで以下のことが行えます。（未完成なので、一部動作しません）

NewFile: 新しいファイルを作成します。
UpdateRelation : 関連を更新します。
UpdateGraph : グラフを更新します。
ShowHighRelationDocs : 関連の強いドキュメント一覧を表示します。
