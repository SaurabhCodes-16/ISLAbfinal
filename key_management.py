import random
import os
import json
import time
from hashlib import sha256
from datetime import datetime, timedelta

# ---------------------------
# Rabin Cryptosystem Helpers
# ---------------------------
def is_prime(n, k=5):  
    """ Miller-Rabin primality test """
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_large_prime(bits=512):
    """ Generate a large prime congruent to 3 mod 4 """
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1
        if is_prime(p) and p % 4 == 3:
            return p

def rabin_keygen(bits=1024):
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    n = p * q
    return {"public": n, "private": (p, q)}

# ---------------------------
# Centralized Key Manager
# ---------------------------
class KeyManager:
    def __init__(self, storage_file="keys.json"):
        self.storage_file = storage_file
        self.keys = self.load_keys()
    
    def load_keys(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                return json.load(f)
        return {}

    def save_keys(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.keys, f, indent=4)

    def generate_keys_for_entity(self, entity_id, bits=1024):
        keypair = rabin_keygen(bits)
        self.keys[entity_id] = {
            "public": keypair["public"],
            "private": keypair["private"],
            "created_at": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(days=365)).isoformat(),
            "revoked": False
        }
        self.save_keys()
        print(f"[LOG] Keys generated for {entity_id}")
        return self.keys[entity_id]

    def get_public_key(self, entity_id):
        if entity_id in self.keys and not self.keys[entity_id]["revoked"]:
            return self.keys[entity_id]["public"]
        return None

    def revoke_keys(self, entity_id):
        if entity_id in self.keys:
            self.keys[entity_id]["revoked"] = True
            self.save_keys()
            print(f"[LOG] Keys revoked for {entity_id}")

    def renew_keys(self, entity_id, bits=1024):
        if entity_id in self.keys:
            return self.generate_keys_for_entity(entity_id, bits)

    def auto_renew_all(self):
        now = datetime.utcnow()
        for entity, data in self.keys.items():
            if datetime.fromisoformat(data["expires_at"]) <= now and not data["revoked"]:
                self.renew_keys(entity)
                print(f"[LOG] Auto-renewed keys for {entity}")

# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    km = KeyManager()

    # Hospital A requests keys
    hospitalA = km.generate_keys_for_entity("Hospital_A", bits=1024)

    # Get Hospital A’s public key
    print("Public key for Hospital_A:", km.get_public_key("Hospital_A"))

    # Revoke Hospital A’s keys
    km.revoke_keys("Hospital_A")

    # Auto renew after expiry simulation
    km.auto_renew_all()
