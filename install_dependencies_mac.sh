#!/bin/bash

# Mac M3 Dependencies Installation Script
# This script installs system dependencies required for AICoverGen on Mac

echo "Installing system dependencies for AICoverGen on Mac..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install ffmpeg (required for audio processing)
echo "Installing ffmpeg..."
brew install ffmpeg

# Install sox (required for audio effects)
echo "Installing sox..."
brew install sox

# Install libsndfile (required for soundfile Python package)
echo "Installing libsndfile..."
brew install libsndfile

# Install additional audio libraries
echo "Installing additional audio libraries..."
brew install libsamplerate
brew install libsoxr

echo "System dependencies installation complete!"
echo ""
echo "Next steps:"
echo "1. Create virtual environment: python3 -m venv venv_mac_m3"
echo "2. Activate it: source venv_mac_m3/bin/activate"
echo "3. Install Python packages: pip install -r requirements_mac_m3.txt"
