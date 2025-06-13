## Probabilistic Graphical Models using Python (pgmpy)
from IPython.display import Image
from pgmpy.utils import get_example_model

if __name__ == '__main__':
    discrete_bn = get_example_model('asia')
    viz = discrete_bn.to_graphviz()
    viz.draw('asia.png', prog='neato')
    Image('asia.png')
