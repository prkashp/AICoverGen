#!/usr/bin/env python3
"""
Test script for Mac M3 compatibility
Tests device detection and basic functionality
"""

import sys
import os
sys.path.append('src')

def test_device_detection():
    """Test if device detection works correctly"""
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        
        # Test device availability
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"MPS available: {torch.backends.mps.is_available()}")
        
        # Test device selection logic (from main.py)
        if torch.backends.mps.is_available():
            device = 'mps'
            is_half = False
            print(f"Selected device: {device} (half precision: {is_half})")
        elif torch.cuda.is_available():
            device = 'cuda:0'
            is_half = True
            print(f"Selected device: {device} (half precision: {is_half})")
        else:
            device = 'cpu'
            is_half = False
            print(f"Selected device: {device} (half precision: {is_half})")
            
        return True
    except ImportError as e:
        print(f"Import error: {e}")
        return False

def test_audio_libraries():
    """Test if audio processing libraries work"""
    try:
        import librosa
        import soundfile
        import pydub
        print("Audio libraries imported successfully")
        return True
    except ImportError as e:
        print(f"Audio library import error: {e}")
        return False

def test_rvc_imports():
    """Test if RVC-related imports work"""
    try:
        from rvc import Config
        print("RVC imports successful")
        return True
    except ImportError as e:
        print(f"RVC import error: {e}")
        return False

def main():
    print("Testing Mac M3 compatibility...\n")
    
    tests = [
        ("Device Detection", test_device_detection),
        ("Audio Libraries", test_audio_libraries),
        ("RVC Imports", test_rvc_imports)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Running {test_name} test...")
        result = test_func()
        results.append((test_name, result))
        print(f"{test_name}: {'PASS' if result else 'FAIL'}\n")
    
    # Summary
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ Mac M3 setup is working correctly!")
    else:
        print("❌ Some tests failed. Check the error messages above.")

if __name__ == "__main__":
    main()
