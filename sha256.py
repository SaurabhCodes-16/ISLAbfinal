# sha256_hash.py
import hashlib

def sha256_hash(data: str) -> str:
    """Return SHA-256 hex digest of a string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


sample = "PATIENTSUGAR120"
print("Input:", sample)
print("SHA-256:", sha256_hash(sample))
