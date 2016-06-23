from trapeze import *

def operOR(lay1, lay2):
    # lay - класс trapeze, содержит все отрезка слоя
    
    # поиск всех осей
    axis = []
    for ed in lay1.edges:
        axis.append(ed.first[0])
        axis.append(ed.second[0])
    for ed in lay2.edges:
        axis.append(ed.first[0])
        axis.append(ed.second[0])
    axis = list(set(axis))  # удаляем дубликаты
    axis.sort()  

    # далее...

    