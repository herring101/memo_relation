import h5py
import os

# with h5py.File("embeddings.hdf5", "a") as f:
#     group = f.create_group(file)
#     group.create_dataset("topic", data=topic)
#     group.create_dataset("embeddings", data=embeddings)
# 上のコードで保存したものから情報を取り出して出力する
# for filename in os.listdir("./docs"):
#     if not filename.endswith(".md"):
#         continue
#     filename = "./docs/{}".format(filename)
with h5py.File("embeddings.hdf5", "r") as f:
    for group_name, group in f.items():
        print("Group:", group_name)
        for dataset_name, dataset in group.items():
            print("Dataset:", dataset_name)
            topic = dataset["topic"][()].decode("utf-8")
            embeddings = dataset["embeddings"][()][:10]
            print("Topic:", topic)
            print("Embeddings:", embeddings)
            print()
