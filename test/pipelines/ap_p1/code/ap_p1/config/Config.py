from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, ap1_v1: str=None):
        self.spark = None
        self.update(ap1_v1)

    def update(self, ap1_v1: str="test"):
        self.ap1_v1 = ap1_v1
        pass
