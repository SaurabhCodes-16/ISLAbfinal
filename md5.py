# md5_hash.py
import hashlib

def md5_hash(data: str) -> str:
    """Return MD5 hex digest of a string."""
    return hashlib.md5(data.encode('utf-8')).hexdigest()


sample = "PATIENTSUGAR120"
print("Input:", sample)
print("MD5   :", md5_hash(sample))
