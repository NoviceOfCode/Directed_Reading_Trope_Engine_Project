import sys
import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objs as go
import plotly.io as pio
import tkinter as tk
from tkinterweb import HtmlFrame

# Step 1: Prepare your data (same as in the previous example)
doc_embeddings = np.random.rand(10, 300)  # Replace with your actual embeddings
query_embedding = np.random.rand(1, 300)  # Replace with your actual query embedding

all_embeddings = np.vstack([doc_embeddings, query_embedding])

# Perform PCA
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(all_embeddings)

# Separate document and query embeddings
doc_reduced = reduced_embeddings[:-1]
query_reduced = reduced_embeddings[-1]

# Create scatter plot for documents
doc_scatter = go.Scatter3d(
    x=doc_reduced[:, 0],
    y=doc_reduced[:, 1],
    z=doc_reduced[:, 2],
    mode='markers',
    marker=dict(size=8, color='blue'),
    name='Documents'
)

# Create scatter plot for query
query_scatter = go.Scatter3d(
    x=[query_reduced[0]],
    y=[query_reduced[1]],
    z=[query_reduced[2]],
    mode='markers',
    marker=dict(size=10, color='red'),
    name='Query'
)

# Add lines from each document to the query
lines = []
for doc_point in doc_reduced:
    line = go.Scatter3d(
        x=[doc_point[0], query_reduced[0]],
        y=[doc_point[1], query_reduced[1]],
        z=[doc_point[2], query_reduced[2]],
        mode='lines',
        line=dict(color='gray', width=2),
        showlegend=False
    )
    lines.append(line)

# Layout settings
layout = go.Layout(
    title='3D Embedding Space',
    scene=dict(
        xaxis_title='PC1',
        yaxis_title='PC2',
        zaxis_title='PC3'
    )
)

# Combine all plots
fig = go.Figure(data=[doc_scatter, query_scatter] + lines, layout=layout)
fig.write_html('3d_embedding_visualization.html')
# Step 3: Create the Tkinter application and main window
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('3D Embedding Visualization')
        self.geometry('800x600')

        # Create the HTML frame widget
        self.html_frame = HtmlFrame(self, horizontal_scrollbar="auto")
        self.html_frame.pack(fill="both", expand=True)

        # Load the HTML content into the HTML frame
        html_filename = '3d_embedding_visualization.html'
        with open(html_filename, 'r') as file:
            html_content = file.read()
        self.html_frame.load_html(html_content)

# Step 4: Run the Tkinter application
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
