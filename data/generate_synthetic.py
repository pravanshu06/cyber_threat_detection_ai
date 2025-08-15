"""Generate a small synthetic dataset resembling network connection features.
Output: data/synthetic_flows.csv
"""
import os
import numpy as np
import pandas as pd

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_flows.csv")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

rng = np.random.default_rng(42)
n = 2000
# Features: duration (s), src_bytes, dst_bytes, packets, protocol (0=tcp,1=udp), flags, connections_last_min
duration = rng.exponential(scale=1.0, size=n)
src_bytes = rng.poisson(300, size=n) + (rng.integers(0, 2000, size=n) * (rng.random(n) < 0.05))
dst_bytes = rng.poisson(250, size=n)
packets = np.clip((src_bytes + dst_bytes) // 100 + rng.integers(1, 10, size=n), 1, None)
protocol = rng.choice([0,1], size=n, p=[0.8,0.2])
flags = rng.integers(0, 8, size=n)
connections_last_min = rng.poisson(2, size=n)

# Generate label: 0 benign, 1 malicious (simple rule + noise)
score = (src_bytes > 1500).astype(int) + (duration > 10).astype(int) + (flags > 5).astype(int)
prob_mal = 1 / (1 + np.exp(-0.8*(score - 1)))  # logistic-ish
label = (rng.random(n) < prob_mal).astype(int)

df = pd.DataFrame({
    "duration": duration,
    "src_bytes": src_bytes,
    "dst_bytes": dst_bytes,
    "packets": packets,
    "protocol": protocol,
    "flags": flags,
    "connections_last_min": connections_last_min,
    "label": label
})

df.to_csv(OUT, index=False)
print(f"Wrote synthetic dataset to: {OUT}")
