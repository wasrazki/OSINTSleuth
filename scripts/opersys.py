import subprocess

def os_fingerprint(target_ip):
    try:
        # Run Nmap with OS fingerprinting on the target IP
        nmap_command = f"nmap -O {target_ip}"
        result = subprocess.run(nmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # Extract the OS fingerprint from Nmap's output
            os_fingerprint = ""
            lines = result.stdout.split('\n')
            for line in lines:
                if "OS details" in line:
                    os_fingerprint = line.strip()
                    break
            
            if os_fingerprint:
                return os_fingerprint
            else:
                return "OS fingerprint not found."
        else:
            return "Nmap error: " + result.stderr
        
    except Exception as e:
        return "Error: " + str(e)
"""
if __name__ == "__main__":
    target_ip = "aziza.tn"  # Replace with the target IP address
    
    os_info = os_fingerprint(target_ip)
    
    print(f"OS Fingerprint for {target_ip}:\n{os_info}")"""
