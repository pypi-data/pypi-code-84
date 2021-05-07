from data_stack.io.resources import StreamedResource
from data_stack.dataset.iterator import DatasetIterator
import h5py
import torch


class NewsGroupsIterator(DatasetIterator):

    def __init__(self, data_stream: StreamedResource):
        self.h5py_file = h5py.File(data_stream, "r")
        self.samples_dataset = self.h5py_file["samples"]
        self.targets_dataset = self.h5py_file["targets"]

    def __len__(self):
        return len(self.samples_dataset)

    def __getitem__(self, index: int):
        """ Returns the sample and target of the dataset at given index position.
        :param index: index within dataset
        :return: sample, target, tag
        """
        if(len(self) > index):
            target = self.targets_dataset[index].decode("utf-8")
            return torch.Tensor(self.samples_dataset[index]), target, target
        else:
            raise IndexError('index out of range')
