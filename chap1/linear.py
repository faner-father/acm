#!/bin/env python
#coding:utf-8

class Linear(object):

    def list(self):
        raise NotImplemented

    def insert(self, e, index):
        raise NotImplemented

    def remove(self, index):
        raise NotImplemented

class SequenceList(Linear):
    
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

class SingleLinkedList(Linear):
   
    class Node(object):
        
        def __init__(self, _data, _next=None):
            self._data = _data
            self._next = _next

        @property
        def data(self):
            return self._data

        def _get_next(self):
            return self._next
        
        def _set_next(self, _next):
            self._next = _next

        next = property(_get_next, _set_next)

        def __str__(self):
            return ','.join([unicode(self.data), str(self.next or 'None')])

        def __repr__(self):
            return self.__str__()

    def __init__(self, *elements):
        assert elements
        header = None
        last = None
        for e in elements:
            current = self.Node(e)
            if last:
                last.next = current
            if not header:
                header = current
            last = current
        self._header = header

    @property
    def header(self):
        return self._header

    def travel(self):
        current = None
        while 1:
            current = self.header if not current else current.next
            if current:
                yield current
            else:
                raise StopIteration

    def list(self):
        return [e for e in self.travel()]

    def insert(self, e, index):
        pre, next = None, self.header
        while index>0:
            pre, next = next, next.next
            if not next:
                index = 0
            else:
                index -= 1
        else:
            new_node = self.Node(e, next)
            if pre:
                pre.next = new_node
            else:
                self._header = new_node

    def remove(self, index):
        pre, dnode = None, self.header
        while index>0:
            pre, dnode = dnode, dnode.next
            if dnode:
                index -= 1
            else:
                index = 0
        else:
            if pre:
                pre.next = dnode.next
            else:
                self._header = dnode.next

