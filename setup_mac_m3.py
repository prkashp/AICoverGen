#!/usr/bin/env python3
"""
Mac M3 Setup Script for AICoverGen
This script helps set up AICoverGen on Mac M3 systems with proper device detection.
"""

import os
import sys
import subprocess
import platform

def check_mac_m3():
    """Check if running on Mac M3 system"""
    if platform.system() != "Darwin":
        return False
    
    # Check for Apple Silicon
    try:
        result = subprocess.run(['uname', '-m'], capture_output=True, text=True)
        return result.stdout.strip() == 'arm64'
    except:
        return False

def install_dependencies():
    """Install Mac M3 compatible dependencies"""
    print("Installing Mac M3 compatible dependencies...")
    
    # Install requirements with timeout and better error handling
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_mac_m3.txt', '--timeout', '300'], 
                              capture_output=True, text=True, timeout=600)
        if result.returncode != 0:
            print(f"Installation failed: {result.stderr}")
            return False
        print("Dependencies installed successfully!")
        return True
    except subprocess.TimeoutExpired:
        print("Installation timed out. Try installing manually with: pip install -r requirements_mac_m3.txt")
        return False

def setup_environment():
    """Set up environment variables for Mac M3"""
    print("Setting up environment for Mac M3...")
    
    # Set environment variables for MPS
    os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
    os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'
    
    print("Environment configured for Mac M3 with MPS support")

def main():
    if not check_mac_m3():
        print("This script is designed for Mac M3 systems. Use regular requirements.txt for other systems.")
        return
    
    print("Setting up AICoverGen for Mac M3...")
    install_dependencies()
    setup_environment()
    print("Setup complete! You can now run AICoverGen with MPS acceleration.")
    print("Use: python src/main.py or python src/webui.py")

if __name__ == "__main__":
    main()
