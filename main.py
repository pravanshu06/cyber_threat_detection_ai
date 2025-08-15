import os
import subprocess
import pandas as pd
import joblib

# Project root path
ROOT = os.path.dirname(os.path.abspath(__file__))

def run_command(cmd, cwd=ROOT):
    """Run a shell command and show output live."""
    print(f"\n>> Running: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)

def main():
    print("=== Cyber Security Threat Detection AI ===")

    # Step 1: Generate synthetic dataset
    run_command(["python", "-m", "data.generate_synthetic"])

    # Step 2: Train model
    run_command([
        "python", "-m", "src.train",
        "--data", "data/synthetic_flows.csv",
        "--out", "models/rf_model.joblib"
    ])

    # Step 3: Predict using example input
    run_command([
        "python", "-m", "src.predict",
        "--model", "models/rf_model.joblib",
        "--input", "example_input.csv",
        "--out", "predictions.csv"
    ])

    # Step 4: Show predictions
    predictions_path = os.path.join(ROOT, "predictions.csv")
    if os.path.exists(predictions_path):
        print("\n=== Predictions ===")
        df = pd.read_csv(predictions_path)
        print(df)
    else:
        print("No predictions.csv found!")

if __name__ == "__main__":
    main()
