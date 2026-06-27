import hashlib
import os
import time

TARGET_FILE = "sensitive_config.txt"

def calculate_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

print("-" * 55)
print("🛡️ CYBER DEFENSE: FILE INTEGRITY MONITOR (FIM) 🛡️")
print("-" * 55)

# Setup a mock file for simulation
if not os.path.exists(TARGET_FILE):
    with open(TARGET_FILE, "w") as f:
        f.write("ALLOW_USERS=ian,admin\nBLOCK_UNKNOWN=TRUE")

# Generate baseline reference hash
baseline_hash = calculate_hash(TARGET_FILE)
print(f"[+] Establishing trusted baseline for: {TARGET_FILE}")
print(f"[+] Baseline Hash: {baseline_hash}\n")
print("[*] Monitoring file system for modifications... (Press Ctrl+C to stop)")

try:
    # Simulating a file modification check
    time.sleep(1)
    
    # Mocking an attacker tampering with the configuration file
    print("\n[!] Simulate Tampering: Attacker appends malicious configuration...")
    with open(TARGET_FILE, "a") as f:
        f.write("\nALLOW_USERS=attacker_root")
        
    # Recalculate hash after change
    current_hash = calculate_hash(TARGET_FILE)
    
    print(f"[*] Current Hash:  {current_hash}")
    print(f"[*] Baseline Hash: {baseline_hash}")
    
    if current_hash != baseline_hash:
        print("\n🚨 ALERT!!! CRITICAL FILE MODIFICATION DETECTED 🚨")
        print(f"⚠️ {TARGET_FILE} has been unauthorizedly tampered with!")
    else:
        print("\n✅ File is secure. Integrity verified.")
        
except KeyboardInterrupt:
    print("\n[-] Monitoring stopped by user.")

print("-" * 55)
