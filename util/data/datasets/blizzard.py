from torch.utils.data import Dataset


class BLIZZARD(Dataset):

    def __init__(self, path):
        self.path = path

    def __get_item__(self, ind):
        pass
