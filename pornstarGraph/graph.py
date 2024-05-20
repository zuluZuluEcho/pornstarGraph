import networkx as nx


def make_graph(pornstars: set[str]) -> nx.Graph:
    """
    Receives a set of unique pornstars, and makes a graph of it.
    """
    graph: nx.Graph = nx.Graph()

    graph.add_nodes_from(pornstars)

    return graph


def add_edges(graph: nx.Graph, frequency_per_pornstar_pair: dict[tuple[str, str], int]) -> nx.Graph:
    """
    Adds edges to a graph, with the weight of each edges being the frequency of a pornstar pair.
    """
    for pornstar_pair, frequency in frequency_per_pornstar_pair.items():
        pornstar1: str = pornstar_pair[0]
        pornstar2: str = pornstar_pair[1]

        if not (frequency == 0):
            graph.add_edge(pornstar1, pornstar2, weight=frequency_per_pornstar_pair[pornstar_pair])

    return graph


def size_gigant_component_after_deletion_node(graaf: nx.Graph, knoop: str | int) -> int:
    """
    Returns the size of a graph after the deletion of a given node.
    """
    graph_without_node: nx.Graph = graaf.copy()
    graph_without_node.remove_node(knoop)

    components: list[str | int] = list(nx.connected_components(graph_without_node))
    gigant_component: str | int = max(components, key=len)

    size_gigant_component: str | int = len(gigant_component)

    return size_gigant_component


def frequencies_degrees(graph: nx.Graph) -> dict[str | int, int]:
    """
    Returns the frequency of each degree in a graph.
    """
    frequency_per_degree: dict[str | int, int] = {degree[1]: sum(1 for node in graph.nodes() if graph.degree(node) == degree[1]) for degree in graph.degree()}

    return frequency_per_degree


def amount_of_edges_needed_for_complete_graph(graph: nx.Graph) -> int:
    """
    Return the required amount of edges need to make a graph complete.
    """
    aantal_lijnen_graaf: int = graph.number_of_edges()
    aantal_lijnen_complete_graaf: int = nx.complete_graph(len(graph)).number_of_edges()

    aantal_lijnen_voor_compleet: int = aantal_lijnen_complete_graaf - aantal_lijnen_graaf

    return aantal_lijnen_voor_compleet
