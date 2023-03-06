import pydot

graph = pydot.Dot(graph_type='digraph')

# Agregamos los nodos al grafo
node_a = pydot.Node("A")
node_b = pydot.Node("B")
node_c = pydot.Node("C")
node_d = pydot.Node("D")

graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)

# Agregamos las aristas entre los nodos
edge_ab = pydot.Edge(node_a, node_b)
edge_bc = pydot.Edge(node_b, node_c)
edge_cd = pydot.Edge(node_c, node_d)

graph.add_edge(edge_ab)
graph.add_edge(edge_bc)
graph.add_edge(edge_cd)

# Renderizamos el grafo en formato PNG
graph.write_png('ejemplo_red.png')
