"""Load saved model and run predictions on an input CSV file (no labels required)."""
import argparse
import joblib
import pandas as pd
from src.utils import load_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='path to saved joblib model')
    parser.add_argument('--input', required=True, help='CSV file with features (no label required)')
    parser.add_argument('--out', default='predictions.csv', help='output CSV with predictions')
    args = parser.parse_args()

    bundle = joblib.load(args.model)
    model = bundle['model']
    scaler = bundle['scaler']

    X = load_data(args.input)
    Xs = scaler.transform(X)
    preds = model.predict(Xs)
    probs = model.predict_proba(Xs)[:,1] if hasattr(model, 'predict_proba') else None

    out_df = X.copy()
    out_df['prediction'] = preds
    if probs is not None:
        out_df['malicious_score'] = probs
    out_df.to_csv(args.out, index=False)
    print(f"Wrote predictions to {args.out}")

if __name__ == '__main__':
    main()
