import nympy as np

def neuralNetwork(x):
    if x < 0:
        return -1
    else:
        retun 1 

# weights er linjen i grafen.
# weights tallene kommer fra en machine leraning model

def perceptron(inp, weights):
    # Mulighed 1
    np.array(inp) * np.array(weights)

    # Mulighed 2
    for nr in range(len(inp)):
        output.append(inp[nr] * weights[nr])
    #return activation_functionsum(sum(output))

    # mulighed 3
    dot_pruduct = sum([ i * w for i, w in zip(inp, weights)]) # zip bygger tupler ud af lister.
    
    return 



