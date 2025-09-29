# sha1_hash.py
import hashlib

def sha1_hash(data: str) -> str:
    """Return SHA-1 hex digest of a string."""
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

sample = "PATIENTSUGAR120"
print("Input:", sample)
print("SHA-1 :", sha1_hash(sample))
