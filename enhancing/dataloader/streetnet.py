import sys
sys.path.append(r'd:\Documents\repos\VQGAN-pytorch')
from utils import MultiImagePaths
print('Loaded {}'.format(MultiImagePaths.__class__))

class RoadBase(MultiImagePaths):
    def __getitem__(self, item):
        data = super().__getitem__(item)
        return {'image': data}