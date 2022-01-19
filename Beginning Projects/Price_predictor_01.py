def new_layer(Input,weights,biases):
    Output=[]
#weights and biases are two dimensional arrays
#gives a new layer given a previous layer and new layers weights and biases
    for p in range(0,10):
        Output.append(0)
        for q in range(0,10):
            i=Input[q]
            w=weights[p][q]
            b=biases[p][q]
            Output[p] = Output[p] + i*w + b
    return Output

def predictor(Input,weights,biases,no_of_layers):
#weights and biases are three dimensional arrays
#gives an output given a input and weights and biases if a neural network
    n= no_of_layers
    layers = [1]
    layers[0]=new_layer(Input,weights[0],biases[0])
    for i in range(1,n+1):
        layers.append(1)
        layers[i]=new_layer(layers[i-1],weights[i],biases[i])
    return layers[n]



def Layers(Input,weights,biases,no_of_layers):
#weights and biases are three dimensional arrays
#gives an output given a input and weights and biases if a neural network
    n= no_of_layers
    layers = [1]
    layers[0]=new_layer(Input,weights[0],biases[0])
    for i in range(1,n+1):
        layers.append(1)
        layers[i]=new_layer(layers[i-1],weights[i],biases[i])
    return layers





def align_layer(Input,weights,biases,OUTPUT):
#Gives weights and biases that when used with given input brings output closer to desired value
    out=new_layer(Input,weights,biases)
    for i in range(0,10):
        d = OUTPUT[i] - out[i]
        for j in range(0,10):
            weights[i][j] = weights[i][j] + d/(Input[j] * 100000)
            biases[i][j] = biases[i][j] + d/100000



            
def req_input(Input,weights,biases,OUTPUT):
#Gives input that when used with weights and biases brings output closer to desired value
    out=new_layer(Input,weights,biases)
    req=[0]*10
    for i in range(0,10):
        for j in range(0,10):
             d = OUTPUT[j] - out[j]
             Input[i]=Input[i] + d/(weights[j][i]*100000)
        req[i]=Input[i]+0
    return req

def req_layers(Input,weights,biases,OUTPUT,n):
    reqlayers=[1]*(n+1)
    layers=Layers(Input,weights,biases,n)
    no=[]
    reqlayers[n]=OUTPUT
    for i in range(0,n):
        no.append(0)
        no[i]=n-1-i
    for p in no:
        reqlayers[p]=req_input(layers[p],weights[p+1],biases[p+1],reqlayers[p+1])
    return reqlayers



def align_weights_biases(Input,weights,biases,OUTPUT,n):
    reqlayers=req_layers(Input,weights,biases,OUTPUT,n)
    layers=Layers(Input,weights,biases,n)
    no=[]
    for i in range(0,n):
        no.append(0)
        no[i]=n-1-i
    for p in no:
        align_layer(layers[p],weights[p+1],biases[p+1],reqlayers[p+1])
    align_layer(Input,weights[0],biases[0],reqlayers[0])
    

    
    
def alignment(Input,weights,biases,OUTPUT,n):
    output= predictor(Input,weights,biases,n)
    
    layer[n]=req(output,weights[n],biases[n],OUTPUT)
    align_layer(layer[n-1],weights[n],biases[n],OUTPUT)
    for i in range(0,n).reverse():
        layer[i]=req(layer[i],weights[i+1],biases[i+1],layer[i+1])
        align_layer(layer[i-1],weights[i],biases[i],layer[i])


























        

