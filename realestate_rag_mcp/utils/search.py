from chromadb import Collection

from .utils import search_using_text_with_filter


def search_using_text(collection: Collection, query: str, n_results=5) -> str | None:
    """
    Searches for real estate properties within a collection using a text query. This function
    is used when the user does not provide any other filters or parameters for the search.

    Args:
        collection (Collection): The collection object containing property documents to be searched.
        query (str): The text query input by the user to search for relevant properties.
        n_results (int, optional): The maximum number of search results to return. Defaults to 5.

    Returns:
        str | None: A formatted string containing the top matching property document chunks and their metadata,
        or None if no results are found.

    This function queries the provided collection using the given text query, retrieves the top matching property
    documents, and formats their content and metadata into a readable context string. The context can be used for
    displaying search results or as input for downstream language model processing.
    """

    results = collection.query(query_texts=query, n_results=n_results)

    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""

    for chunk, meta in zip(chunks, metadatas):
        # context += f"[#{meta['number']}] {meta['title']}] \n{chunk}\n\n"
        context += f"[#{meta['title']}] \n{chunk}\n\n"

    return context


def search_within_suburb(collection: Collection, suburb: str, query: str, n_results=5) -> str | None:
    """
    Search for properties within a specific suburb using a text query.
    """

    return search_using_text_with_filter(collection, query, {"suburb": suburb}, n_results)


def search_within_suburb_code(collection: Collection, suburb_code: str, query: str, n_results=5) -> str | None:
    """
    Search for properties within a specific suburb code using a text query.
    """

    return search_using_text_with_filter(collection, query, {"suburb_code": suburb_code}, n_results)
