from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from encoder.encoder_factory import EncoderFactory
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN

app = Flask(__name__)
encoder = EncoderFactory.initialize_encoder('BOWVariation')

def read_data():
    df = pd.read_csv('dataframe/data.csv')
    return df

def alpha(i, n):
    return (n - i) * 1 / n

def dbscan_method(eps, min_samples, df, method):
    X = np.array(df[method].tolist())
    X_scaled = StandardScaler().fit_transform(X)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit_predict(X_scaled)
    df[str('dbscan_'+ method)] = clusters

    return df

def kmeans_method(n_clusters, df, method):
    X = np.array(df[method].tolist())
    X_scaled = StandardScaler().fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(X_scaled)
    df[str('kmeans_'+ method)] = clusters

    return df


@app.route('/proteins-classification/data', methods=['GET'])
def get_data():
    df = read_data()
    return jsonify({'data': df.to_dict(orient='records')})


@app.route('/proteins-classification/dbscan/vectorMaxN', methods=['POST'])
def dbscan_vectorMaxN():
    data = request.get_json()
    eps, min_samples = float(data.get('eps')), int(data.get('min_samples'))

    df = read_data()
    n = df['sequence'].apply(len).max()
    df['vectorMaxN'] = df['sequence'].apply(lambda x: encoder.get_vector_byMaxN(x, alpha, n))
    

    dbscan = dbscan_method(eps, min_samples, df, 'vectorMaxN')
    data = dbscan['sequence'].tolist()
    cluster = dbscan['dbscan_vectorMaxN'].tolist()

    return jsonify({'data': data, 'cluster': cluster})

@app.route('/proteins-classification/dbscan/vectorSeqN', methods=['POST'])
def dbscan_vectorSeqN():
    data = request.get_json()
    eps, min_samples = float(data.get('eps')), int(data.get('min_samples'))

    df = read_data()
    df['vectorSeqN'] = df['sequence'].apply(lambda x: encoder.get_vector_bySeqN(x, alpha))
    dbscan = dbscan_method(eps, min_samples, df, 'vectorSeqN')
    data = dbscan['sequence'].tolist()
    cluster = dbscan['dbscan_vectorSeqN'].tolist()

    return jsonify({'data': data, 'cluster': cluster})

@app.route('/proteins-classification/kmeans/vectorMaxN', methods=['POST'])
def kmeans_vectorMaxN():
    data = request.get_json()
    n_clusters = int(data.get('n_clusters'))

    df = read_data()
    n = df['sequence'].apply(len).max()
    df['vectorMaxN'] = df['sequence'].apply(lambda x: encoder.get_vector_byMaxN(x, alpha, n))

    kmeans = kmeans_method(n_clusters, df, 'vectorMaxN')
    data = kmeans['sequence'].tolist()
    cluster = kmeans['kmeans_vectorMaxN'].tolist()

    return jsonify({'data': data, 'cluster': cluster})

@app.route('/proteins-classification/kmeans/vectorSeqN', methods=['POST'])
def kmeans_vectorSeqN():
    data = request.get_json()
    n_clusters = int(data.get('n_clusters'))

    df = read_data()
    df['vectorSeqN'] = df['sequence'].apply(lambda x: encoder.get_vector_bySeqN(x, alpha))
    kmeans = kmeans_method(n_clusters, df, 'vectorSeqN')
    data = kmeans['sequence'].tolist()
    cluster = kmeans['kmeans_vectorSeqN'].tolist()

    return jsonify({'data': data, 'cluster': cluster})

if __name__ == '__main__':
    app.run()



    
    


