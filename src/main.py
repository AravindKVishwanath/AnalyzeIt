from flask import Flask, request, jsonify, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json
import google.generativeai as genai
import PIL.Image
import os
app = Flask(__name__, static_url_path='/static')

# Global variable to store the uploaded DataFrame
uploaded_df = None

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_df
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and file.filename.endswith('.csv'):
        uploaded_df = pd.read_csv(file)
        columns = uploaded_df.columns.tolist()
        return jsonify({'columns': columns})
    else:
        return jsonify({'error': 'File is not a CSV'})

@app.route('/plot_graph', methods=['POST'])
def plot_graph():
    global uploaded_df
    if uploaded_df is None:
        return jsonify({'error': 'No file uploaded'})

    data = request.json
    graph_type = data.get('graph_type')
    column1 = data.get('column1')
    column2 = data.get('column2')
    column3 = data.get('column3')  # Third column for 3D graphs

    if column1 not in uploaded_df.columns or column2 not in uploaded_df.columns:
        return jsonify({'error': 'Invalid column selected'})
    
    # Check for column3 only if the graph type is 3D
    if '3d' in graph_type and column3 not in uploaded_df.columns:
        return jsonify({'error': 'Invalid column selected for 3D graph'})

    fig = None
    
    if graph_type == 'scatter':
        fig = px.scatter(uploaded_df, x=column1, y=column2, title=f'Scatter Plot of {column1} vs {column2}')
    elif graph_type == 'bar':
        fig = px.bar(uploaded_df, x=column1, y=column2, title=f'Bar Graph of {column1} vs {column2}')
    elif graph_type == 'line':
        fig = px.line(uploaded_df, x=column1, y=column2, title=f'Line Plot of {column1} vs {column2}')
    elif graph_type == 'histogram':
        fig = px.histogram(uploaded_df, x=column1, title=f'Histogram of {column1}')
    elif graph_type == 'box':
        fig = px.box(uploaded_df, x=column1, y=column2, title=f'Box Plot of {column1} vs {column2}')
    elif graph_type == 'pie':
        fig = px.pie(uploaded_df, names=column1, values=column2, title=f'Pie Chart of {column1} vs {column2}')
    elif graph_type == 'area':
        fig = px.area(uploaded_df, x=column1, y=column2, title=f'Area Plot of {column1} vs {column2}')
    elif graph_type == 'scatter_3d':
        fig = px.scatter_3d(uploaded_df, x=column1, y=column2, z=column3, title=f'3D Scatter Plot of {column1}, {column2}, and {column3}')
    elif graph_type == 'line_3d':
        fig = px.line_3d(uploaded_df, x=column1, y=column2, z=column3, title=f'3D Line Plot of {column1}, {column2}, and {column3}')
    elif graph_type == 'surface_3d':
        fig = px.surface(uploaded_df, x=column1, y=column2, z=column3, title=f'3D Surface Plot of {column1}, {column2}, and {column3}')
    else:
        return jsonify({'error': 'Invalid graph type'})

    # Update layout to ensure all x and y axis contents are displayed
    fig.update_layout(
        xaxis={'autorange': True},
        yaxis={'autorange': True},
        xaxis_tickangle=-45,
        height=600
    )

    graph_json = pio.to_json(fig)
    genai.configure(api_key="AIzaSyBUKMg1RlT62Pn4jdZcTb6ovQ4ESGqB_Q4")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([" I am very strict i only need you to tell what is in the photo maybe a little analysis will also do but you shouldnt give anything else keep it a little lengthy, mention few columns and their trends too, like points and subpoints, What is in this photo?", graph_json])
    print("my response",response.text)
    
    return jsonify({'graph_json': graph_json,'desc':response.text})


if __name__ == '__main__':
    app.run(debug=True, port=5050)

