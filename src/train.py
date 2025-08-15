"""Train a RandomForest classifier on the synthetic data and save model + scaler."""
import argparse, os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.utils import load_data, fit_scaler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/synthetic_flows.csv')
    parser.add_argument('--out', default='models/rf_model.joblib')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    X, y = load_data(args.data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = fit_scaler(X_train)
    X_train_s = scaler.transform(X_train)
    X_test_s = scaler.transform(X_test)

    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    clf.fit(X_train_s, y_train)

    preds = clf.predict(X_test_s)
    print(classification_report(y_test, preds, digits=4))

    # Save both model and scaler together
    joblib.dump({'model': clf, 'scaler': scaler}, args.out)
    print(f"Saved model+scaler to {args.out}")

if __name__ == '__main__':
    main()
