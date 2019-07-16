class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if value < self.value:
      if self.left == None:
        self.left = new_node
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right == None:
        self.right = new_node
      else:
        self.right.insert(value)

  def contains(self, target):
    # if self.value == target:
    #   return True
    # if self.left != None:
    #   if self.value <= target:
    #     if self.left.value == target:
    #       return True
    #     else:
    #       BinarySearchTree.contains(self.left,target)
    # elif self.right != None:
    #   if self.value >= target:
    #     if self.right.value == target:
    #       return True
    #     else:
    #       BinarySearchTree.contains(self.right,target)
    # else:
    #   return False

    if self.value == target:
      return True
    elif self.value < target:
      if self.right == None:
        return False
      else:
        return BinarySearchTree.contains(self.right,target)
    else:
      if self.left ==None:
        return False
      else:
        return BinarySearchTree.contains(self.left, target)

  def get_max(self):
    # if self.right:
    #   self.right.get_max()
    # else:
    #   return self.value

    temp = 0
    current = self
    while current is not None:
      temp = max(current.value, temp)
      current = current.right
    return temp

  def for_each(self, cb):
    # if self:
    #   res = self.for_each(self.left)
    #   res.append(self.value)
    #   res = res + self.for_each(self.right)
    # return res

    cb(self.value)
    if self.left is not None:
      self.left.for_each(cb)
    elif self.right is not None:
      self.right.for_each(cb)
    
      