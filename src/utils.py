import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "packets",
    "protocol",
    "flags",
    "connections_last_min"
]

def load_data(path):
    df = pd.read_csv(path)
    if 'label' in df.columns:
        X = df[FEATURE_COLUMNS]
        y = df['label']
        return X, y
    else:
        return df[FEATURE_COLUMNS]

def fit_scaler(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler
