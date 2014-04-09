from abc import ABCMeta, abstractmethod

class Publisher:
  def __init__(self):
    self.__subscribers = []

  def addSubscriber(self, subscriber):
    if not subscriber in self.__subscribers:
      self.__subscribers.append(subscriber)
    else:
      raise ValueError

  def notify(self):
    for subscriber in self.__subscribers:
      subscriber.update(self)

class Subscriber():
  __metaclass__ = ABCMeta

  @abstractmethod
  def update(self, publisher):
    pass

