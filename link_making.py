import h5py
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def create_graph_json(embedding_file, output_file, similarity_threshold=0.7):
    data = {"nodes": [], "links": []}
    filenames = []
    topics = []
    embeddings = []

    with h5py.File(embedding_file, "r") as f:
        for group_name, group in f.items():
            for dataset_name, dataset in group.items():
                filename = dataset_name
                filenames.append(filename)
                # base64でエンコードされているので、デコードする
                topic = dataset["topic"][()].decode("utf-8")
                topics.append(topic)
                embedding = dataset["embeddings"][()][:10]
                embeddings.append(embedding)
                data["nodes"].append({"id": filename, "group": topic})

    # Compute cosine similarity
    similarities = cosine_similarity(embeddings)

    # Create links
    for i in range(len(filenames)):
        for j in range(i + 1, len(filenames)):
            print(similarities[i][j])
            if similarities[i][j] > similarity_threshold:
                data["links"].append(
                    {
                        "source": filenames[i],
                        "target": filenames[j],
                        "value": similarities[i][j] - similarity_threshold,
                    }
                )

    # Write the data to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


create_graph_json("embeddings.hdf5", "page/graph.json", 0.75)
