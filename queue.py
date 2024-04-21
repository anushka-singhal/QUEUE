queue = []
def enqueue():
  element = int(input("Enter Element"))
  queue.append(element)
  print(queue)

def dequeue():
  if not queue:
    print("Queue is Empty")
  else:
    e = queue.pop(0)
    print("Elements are removed",e)

while True:
  print("Make choice for your operation 1 for Push the element and 2 for Pop the element and 3 to Quit")
  choice = int(input())
  if choice == 1:
    enqueue()
  elif choice == 2:
    dequeue()
  elif choice == 3:
    break
  else:
    print("you make the wrong choice")
