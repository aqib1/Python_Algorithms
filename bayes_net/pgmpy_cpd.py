from pgmpy.utils import get_example_model

if __name__ == '__main__':
    asia_model = get_example_model('asia')
    asia_model_nodes = asia_model.nodes()
    asian_model_edges = asia_model.edges()
    cpds = asia_model.get_cpds()

    print(f"Nodes in model : {asia_model_nodes}\n")
    print(f"Edges in model : {asian_model_edges}\n")
    print(f"CPDs in model : {cpds}\n")