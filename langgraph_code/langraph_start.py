from langgraph.graph import Graph
from IPython.display import Image, display

def first_function(input1:str):

    return input1+ 'Hello This is input1 function...'

def second_function(input2:str):

    return input2+ 'Hello This is input2 function...'

graph = Graph()
graph.add_node('fun1',first_function)
graph.add_node('fun2',second_function)
graph.add_edge('fun1', 'fun2')
graph.set_entry_point('fun1')
graph.set_finish_point('fun2')
app = graph.compile()
try:
    image = Image(app.get_graph().draw_mermaid_png())
    display(image)
except Exception as e:
    print("Error Block...",e)

response  = app.invoke("Hello from where you are ?")
print(response)
