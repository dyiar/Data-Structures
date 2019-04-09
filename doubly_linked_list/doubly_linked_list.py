"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # new_node = ListNode(value = value)
    # new_node.next = self.head
    # new_node.prev = None

    # if self.head is not None:
    #   self.head.prev = new_node

    # self.head = new_node
    # self.length += 1

    if self.head is None:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length +=1
    

  def remove_from_head(self):

    # if self.head is None:
    #   return None
    # elif self.tail is None:
    #   return None
    # else:
    #   p = self.head
    #   self.head = self.head.next
    #   self.head.prev = None
    #   self.length -= 1

    if self.head is None:
      return None
    p = self.head
    self.head.delete()
    self.head = p.next

    if self.length == 1:
      self.tail = None
    self.length -=1
    return p.value


  def add_to_tail(self, value):
    # new_node = ListNode(value = value)
    # new_node.prev = self.tail
    # new_node.next = None

    # if self.tail is not None:
    #   self.tail.next = new_node

    # self.tail = new_node
    # self.length +=1

    if self.tail is None:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length +=1

  def remove_from_tail(self):
    if self.tail is None:
      return None

    old_tail = self.tail
    self.tail.delete()
    self.tail = old_tail.prev
    # if list only had 1 node
    if self.length == 1:
      self.head = None

    self.length -= 1
    return old_tail.value


  def move_to_front(self, node):
    self.head.insert_before(node.value)
    self.head = self.head.prev
    if node is self.tail:
      self.tail = self.tail.prev
    node.delete()

  def move_to_end(self, node):
    self.tail.insert_after(node.value)
    self.tail = self.tail.next
    if node is self.head:
      self.head = self.head.next
    node.delete()

  def delete(self, node):
    if node is self.head:
      self.head = self.head.next
    if node is self.tail:
      self.tail = self.tail.prev
    node.delete()
    self.length -= 1
    
  def get_max(self):
    if self.head is None:
      return None
    
    max_value = self.head.value
    current_node = self.head.next
    while current_node:
      if current_node.value > max_value:
        max_value = current_node.value
      current_node = current_node.next

    return max_value
