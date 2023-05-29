import sys
from collections import deque
import random
# a progranm that implements the page replacement algorithms
# Libhongo Mko
# Student number: MKXLIB001
# 10/04/2022

def page_generator(num):
    pages = []
    for i in range(num):
        pages.append(random.randint(0,9)) # adding randomly generated pages into the pages list
    return pages

def FIFO(size, pages):
    page_faults = 0
    memory = deque([], maxlen=size) # creating a deque of a fixed size which is an opposite of a que, basically pops out the first element that was added
   
    for i in range(len(pages)): # iterating through the pages
            if pages[i] not in memory and len(memory)<size : # checking whether the page is not in memory and that the memory array is not full
                page_faults +=1
                memory.append(pages[i]) # adding the page in memory
            elif pages[i] in memory: # if the page is in memory we do nothing
                continue 
            elif pages[i] not in memory and len(memory)==size : # checking whether the page is not in memory and whether the array is full
                page_faults +=1
                memory.popleft() # taking out the element that was firstly entered in the deque
                memory.append(pages[i]) # adding the element in the memory

    return page_faults

def LRU(size, pages):
    page_faults = 0
    memory = deque([], maxlen=size) # creating a deque of a fixed size which is an double ended que, basically pops out the any element from both ends(front or back)
   
    for i in range(len(pages)): # iterating through the pages
            if pages[i] not in memory and len(memory)<size : # checking whether the page is not in memory and that the memory array is not full
                page_faults +=1
                memory.appendleft(pages[i]) # adding the page in memory
                
            elif pages[i] in memory: 
                # if the page is in memory we remove it from its current position and add it at the beginning of the deque (left end)
                memory.remove(pages[i])
                memory.appendleft(pages[i])
            elif pages[i] not in memory and len(memory)==size : # checking whether the page is not in memory and whether the array is full
                page_faults +=1
                memory.pop() # taking out the element that is at the end of the deque(right end)
                memory.appendleft(pages[i]) # adding the element in the memory
    
    return page_faults
    
def OPT(size, pages):
    page_faults = 0
    memory = deque([], maxlen=size) # creating a deque of a fixed size which is an double ended que, basically pops out the any element from both ends(front or back)
   
    for i in range(len(pages)): # iterating through the pages
            if pages[i] not in memory and len(memory)<size : # checking whether the page is not in memory and that the memory array is not full
                page_faults +=1
                memory.append(pages[i]) # adding the page in memory
                
            elif pages[i] in memory: 
                # if the page is in memory we remove it from its current position and add it at the beginning of the deque (left end)
                memory.remove(pages[i])
                memory.appendleft(pages[i])
            elif pages[i] not in memory and len(memory)==size : # checking whether the page is not in memory and whether the array is full
                
                ahead_references = []
                for j in range(size): #iterating in the range of the frame size
                    if memory[j] in pages[i+1:]:# checking whether each element in memory does occur in the reference string in the future
                        ahead_references.append(pages[i+1:].index(memory[j])) #adding the index of when the element will be accessed in the reference string
                       
                    else:
                        ahead_references.append(-1) # indicates that it is not referenced in future
                page_faults +=1
                if ahead_references.count(-1) <=0: # checking whether there are elements that wont be referenced in future
                    maxindex = ahead_references.index(max(ahead_references))
                    memory.remove(memory[maxindex])
                    memory.appendleft(pages[i]) # adding at the top of memory
                else:
                    minindex = ahead_references.index(-1)
                    memory.remove(memory[minindex])
                    memory.appendleft(pages[i])# adding at the top of memory

    
    return page_faults
    
def main():
    #...TODO...
    num_pages = 10
    num_frames = int(sys.argv[1])
    pages = page_generator(num_pages)
    print("Generated string:\n"+' '.join([str(elem) for elem in pages]))
    print('FIFO', FIFO(num_frames,pages), 'page faults.')
    print('LRU', LRU(num_frames,pages), 'page faults.')
    print('OPT', OPT(num_frames,pages), 'page faults.')
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [frame size]')
    else:
        main()