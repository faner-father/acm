#!/bin/env python
#coding:utf-8

class SequenceLinear(object):
    
    def __init__(self, *elements):
        self._physical_storage = list(elements)

    def travel(self):
        for e in self._physical_storage:
            yield e

    def _mallocate(self, size):
        assert isinstance(size, int) and abs(size)>0
        if size>0:
            self._physical_storage.extend([0] * size)
        else:
            size = min(abs(size), len(self._physical_storage))
            self._physical_storage = (
                self._physical_storage[:len(self._physical_storage)-size]
                )

    def list(self):
        return self._physical_storage[:]

    def insert(self, e, index):
        self._mallocate(1)
        endIndex = len(self._physical_storage) - 1
        index = min([index, endIndex])
        while endIndex>index:
            self._physical_storage[endIndex] = self._physical_storage[endIndex-1]
            endIndex -= 1
        else:
            self._physical_storage[index] = e
        #return self._physical_storage[:]
    
    def remove(self, index):
        assert all((isinstance(index, int), (len(self._physical_storage)> index >= 0)))
        endIndex = len(self._physical_storage) - 1
        while endIndex > index:
            self._physical_storage[index] = self._physical_storage[index+1]
            index += 1
        else:
            self._mallocate(-1)

