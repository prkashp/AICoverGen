# AICoverGen - Mac M3 Compatibility Guide

This guide provides instructions for running AICoverGen on Mac M3 (Apple Silicon) systems.

## Quick Setup

### Option 1: Automated Setup (Recommended)
```bash
python setup_mac_m3.py
```

### Option 2: Manual Setup
```bash
pip install -r requirements_mac_m3.txt
```

## Key Changes for Mac M3

### Dependencies Modified
- **PyTorch**: Uses MPS-compatible version instead of CUDA
- **ONNX Runtime**: CPU version instead of GPU version
- **Device Detection**: Auto-detects MPS, CUDA, or CPU

### Performance Notes
- **MPS Acceleration**: Uses Apple's Metal Performance Shaders for GPU acceleration
- **Half Precision**: Disabled on MPS (not supported)
- **Memory Management**: Optimized for Apple Silicon architecture

## Usage

Run the same commands as the original project:

```bash
# WebUI
python src/webui.py

# CLI
python src/main.py -i "song.mp3" -dir "voice_model" -p 0
```

## Device Detection Logic

The system automatically detects the best available device:
1. **MPS** (Mac M1/M2/M3) - Primary choice for Apple Silicon
2. **CUDA** (NVIDIA GPU) - For systems with NVIDIA cards
3. **CPU** - Fallback option

## Troubleshooting

### Common Issues
1. **MPS Fallback Warnings**: Set `PYTORCH_ENABLE_MPS_FALLBACK=1`
2. **Memory Issues**: Reduce batch sizes or use CPU mode
3. **Audio Processing**: Ensure ffmpeg and sox are installed via Homebrew

### Installation Commands
```bash
# Install system dependencies
brew install ffmpeg sox

# Install Python dependencies
pip install -r requirements_mac_m3.txt
```

## Performance Comparison

| Device | Speed | Memory Usage | Quality |
|--------|-------|--------------|---------|
| MPS    | Fast  | Moderate     | High    |
| CPU    | Slow  | Low          | High    |

## Files Modified

- `requirements_mac_m3.txt` - Mac M3 compatible dependencies
- `src/main.py` - Auto device detection
- `src/rvc.py` - MPS half-precision fix
- `setup_mac_m3.py` - Automated setup script
