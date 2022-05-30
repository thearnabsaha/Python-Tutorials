# queue=[]
# print(queue)
# #enqueue #adding items in the queues
# #enqueue from left
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# #dequeue #removing items from the queues
# #dequeue from left
# queue.pop(0)  #we have used pop(0) for deleting items from 0th position i.e. first position
# queue.pop(0)
# queue.pop(0)
# print(queue)

# #enqueue from right
# queue.insert(0,1)  #queue.insert(position,item) #that's how it will add items in queue by first
# queue.insert(0,2)
# queue.insert(0,3)
# print(queue)
# #dequeue from right
# queue.pop()
# queue.pop()
# queue.pop()
# print(queue)


# import collections
# queue=collections.deque()
# print(queue)
# queue.appendleft(10) #it's adding from right
# queue.appendleft(20)
# queue.appendleft(30)
# print(queue)
# queue.pop() #it's removing from right
# queue.pop()
# queue.pop()
# print(queue)
# queue.append(10) #it's adding from left
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.popleft() #it's removing from left
# queue.popleft()
# queue.popleft()
# print(not queue) #to chec it's empty or not


# import queue
# q=queue.Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# print(q)
# q.get()
# q.get()
# q.get()
# print(q)



# low value high Priority
# q=[]
# q.append(10)
# q.append(40)
# q.append(20)
# q.append(30)
# print(q)
# q.sort(reverse=True)
# print(q)
# q.pop(0)
# q.pop(0)
# q.pop(0)
# print(q)

# # high value high Priority
# q=[]
# q.insert(0,10)
# q.insert(0,40)
# q.insert(0,20)
# q.insert(0,30)
# print(q)
# q.sort()
# print(q)
# q.pop()
# q.pop()
# q.pop()
# print(q)

# low value high priority
# import queue
# q=queue.PriorityQueue()
# q.put(20)
# q.put(30)
# q.put(10)
# q.put(40)
# print(q)
# q.get()
# q.get()
# q.get()
# print(q)


# customize PriorityQueue
# q=[]
# q.append((1,'arnab'))
# q.append((4,'amitama'))
# q.append((2,'suborno'))
# q.append((3,'arijit'))
# print(q)
# q.sort() #for low to high
# print(q)
# q.sort(reverse=True)  #for high to low
# print(q)
# q.pop(0)
# q.pop(0)
# q.pop(0)
# print(q)