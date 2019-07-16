class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    deletedValue = self.storage.pop(-1)
    self._sift_down(0)
    return deletedValue

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index <= 0:
      return
    parent_index = (index-1) // 2
    if self.storage[index] > self.storage[parent_index]:
      temp = self.storage[index]
      self.storage[index] = self.storage[parent_index]
      self.storage[parent_index]=temp
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_child = (index*2) + 1
    right_child = (index*2) + 2

    temp = index

    if len(self.storage) > left_child and self.storage[left_child] > self.storage[temp]:
      temp = left_child

    if len(self.storage) > right_child and self.storage[right_child] > self.storage[temp]:
      temp = right_child

    if index is not temp:
      temp2 = self.storage[index]
      self.storage[index] = self.storage[temp]
      self.storage[temp] = temp2
      self._sift_down(temp)
