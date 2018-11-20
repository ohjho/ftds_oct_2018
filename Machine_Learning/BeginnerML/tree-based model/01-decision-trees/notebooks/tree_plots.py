from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
import pydotplus
import numpy as np
import matplotlib.pyplot as plt

def plot_tree(dtree):
    
    dot_data = StringIO()
    export_graphviz(dtree, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    return graph.create_png()




def plot_decsion_bondary(dtree,X,y ,ax , title='', xlabel='' , ylabel=''):

    # Plot the decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plot_step = 0.02
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    Z = dtree.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = ax.contourf(xx, yy, Z, cmap=plt.cm.Accent)
    #Plot points
    ax.scatter(X[:,0],X[:,1],c=y)
    #Labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)