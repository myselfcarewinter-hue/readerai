import faiss
import numpy as np
import pickle
import os


index = None
stored_chunks = []


def save_vectors(vectors, chunks):

    global index
    global stored_chunks

    vectors = np.array(vectors)

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    stored_chunks = chunks

    faiss.write_index(
        index,
        "faiss.index"
    )

    with open("chunks.pkl","wb") as f:
        pickle.dump(
            stored_chunks,
            f
        )


def load_vectors():

    global index
    global stored_chunks

    if os.path.exists("faiss.index"):

        index = faiss.read_index(
            "faiss.index"
        )

        with open("chunks.pkl","rb") as f:
            stored_chunks = pickle.load(f)



def search_vectors(query_vector):

    query_vector = np.array(
        [query_vector]
    )

    distance,result = index.search(
        query_vector,
        3
    )

    output=[]

    for i in result[0]:
        output.append(
            stored_chunks[i]
        )

    return output