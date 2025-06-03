import os

from chromadb import PersistentClient
from mcp.server.fastmcp import FastMCP

import realestate_rag_mcp.config as config
from realestate_rag_mcp.utils.search import search_using_text, search_within_suburb, search_within_suburb_code

chroma_client = PersistentClient(path=os.path.expanduser(config.CHROMA_DB_PATH))
collection = chroma_client.get_or_create_collection(
    name=config.CHROMA_COLLECTION_NAME, configuration={"hnsw": {"space": "cosine"}}
)

mcp = FastMCP("realestate_rag_mcp")


@mcp.tool()
def search_properties_using_text(query: str, n_results: int = 5) -> str | None:
    """
    Search properties using text query with no extra filtering.

    Args:
        query (str): The search query.
        n_results (int): Number of results to return.
        filter (dict): Optional filter criteria.

    Returns:
        str | None: Contextual information about the properties or None if no results found.
    """
    return search_using_text(collection, query, n_results)


@mcp.tool()
def search_properties_within_suburb(suburb: str, query: str, n_results: int = 5) -> str | None:
    """
    Search properties within a specific suburb using a text query.

    Args:
        suburb (str): The suburb to filter properties by.
        query (str): The search query.
        n_results (int): Number of results to return.

    Returns:
        str | None: Contextual information about the properties or None if no results found.
    """
    return search_within_suburb(collection, suburb, query, n_results)


@mcp.tool()
def search_properties_within_suburbcode(suburb_code: str, query: str, n_results: int = 5) -> str | None:
    """
    Search properties within a specific suburb using a text query and suburb code.

    suburb code has the format of a number with 4 digits, e.g., 3128, 2000, 3153, etc.

    Args:
        suburb_code (str): The suburb to filter properties by.
        query (str): The search query.
        n_results (int): Number of results to return.

    Returns:
        str | None: Contextual information about the properties or None if no results found.
    """
    return search_within_suburb_code(collection, suburb_code, query, n_results)


if __name__ == "__main__":
    # Initialize and run the server
    print("Starting realestate_rag_mcp server...")
    mcp.run(transport="sse")
