import pickle as pkl
from tqdm import tqdm

with open('/fs/fast/u2023000178/fs_zyl/Huawei_Crystal/crystalformer/data/jarvis__megnet-bulk/train/raw/raw_data.pkl', 'rb') as f:
    data = pkl.load(f)


for d in tqdm(data):
    for k, v in d.items():
        print(k, type(v))
    break