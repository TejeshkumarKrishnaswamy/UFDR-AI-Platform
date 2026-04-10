import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

def show_network():

    G = nx.Graph()

    G.add_edge("Suspect Device", "Ramesh")
    G.add_edge("Ramesh", "Suresh")
    G.add_edge("Suresh", "Unknown Number")

    fig = plt.figure()
    nx.draw(G, with_labels=True, node_color='red', node_size=2000)

    st.pyplot(fig)
