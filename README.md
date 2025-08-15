# Cyber Security Threat Detection using AI (Example Project)

This is a minimal, runnable example project that demonstrates how to build a simple cyber security threat detection pipeline in Python using machine learning.

Structure:
- data/generate_synthetic.py : creates a synthetic dataset simulating benign/malicious network flows
- src/utils.py              : helper functions (preprocessing, feature names)
- src/train.py              : trains a RandomForest model and saves it as `models/rf_model.joblib`
- src/predict.py            : loads the saved model and runs inference on new CSV inputs
- requirements.txt          : Python dependencies
- example_input.csv         : small sample CSV you can use with predict.py

Notes:
- This is an educational starter project. For production use, replace synthetic data with real labeled network data (e.g., NetFlow/PCAP features), add robust feature engineering, validation, monitoring, and privacy/security controls.
- Run `python -m pip install -r requirements.txt` to install dependencies.
- Train: `python src/train.py --out models/rf_model.joblib`
- Predict: `python src/predict.py --model models/rf_model.joblib --input example_input.csv`
