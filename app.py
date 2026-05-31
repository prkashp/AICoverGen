import os
import sys
import requests
from pathlib import Path

# Add src/ to path so webui/main imports resolve
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / 'src'))

os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

MDX_DOWNLOAD_LINK = 'https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/'
RVC_DOWNLOAD_LINK = 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/'

mdxnet_models_dir = BASE_DIR / 'mdxnet_models'
rvc_models_dir = BASE_DIR / 'rvc_models'
song_output_dir = BASE_DIR / 'song_output'

for d in (mdxnet_models_dir, rvc_models_dir, song_output_dir):
    d.mkdir(exist_ok=True)


def _dl(link, name, dest):
    target = dest / name
    if target.exists():
        return
    print(f'Downloading {name}...')
    with requests.get(f'{link}{name}', stream=True) as r:
        r.raise_for_status()
        with open(target, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f'  done: {name}')


for model in ['UVR-MDX-NET-Voc_FT.onnx', 'UVR_MDXNET_KARA_2.onnx', 'Reverb_HQ_By_FoxJoy.onnx']:
    _dl(MDX_DOWNLOAD_LINK, model, mdxnet_models_dir)

for model in ['hubert_base.pt', 'rmvpe.pt']:
    _dl(RVC_DOWNLOAD_LINK, model, rvc_models_dir)

from webui import build_app

demo = build_app()
demo.launch()
