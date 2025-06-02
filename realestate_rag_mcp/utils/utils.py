from chromadb import Collection


def search_using_text_with_filter(collection: Collection, query: str, search_filter: dict, n_results=5) -> str | None:
    results = collection.query(query_texts=query, n_results=n_results, where=search_filter)

    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""

    for chunk, meta in zip(chunks, metadatas):
        # context += f"[#{meta['number']}] {meta['title']}] \n{chunk}\n\n"
        context += f"[#{meta['title']}] \n{chunk}\n\n"

    return context
