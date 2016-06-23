import sys
import logging
from trapeze import *
from operations import *

# логгирование
logging.basicConfig(
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    stream = sys.stdout,
    level  = logging.INFO
)
logger = logging.getLogger("trapezoid")
logger.info("Start programm")

# считывание из файла
logger.info("File reading")
f = open('12 edge')
text = f.read()
f.close()

# разбор файла
logger.info("File parsing")
edgesStr = [] # строки фигур
end = text.find("---- Edges:") # находим строку "---- Shapes:"
# заполняем лист фигур
while end != -1:
    begin = end
    # находим начало и конец след строки
    begin = text.find('\n', begin) + 1
    end   = text.find('\n', begin)
    # добавляем строку в список фигур
    edgesStr.append(text[begin: end])      

# построчный вывод файла
for ln in edgesStr:
    print(ln)

# разбор файла
trapezes = {}
for str in edgesStr:
    # получение номера слоя
    begin = str.find("Edge: M")
    if(begin != -1):
        # получение номера слоя
        begin += len("Edge: M")
        end   = str.find(' ', begin)    
        layerNum = int(str[begin: end])
        tra = addTrapezes(trapezes, layerNum)

        # получение параметра открывающий ли отрезок
        begin = end + 1
        end =  str.find(' ', begin)
        isOpen = bool(str[begin: end])    
        
        begin = str.find('[', end + 1)
        end =  str.find(',', begin)
        coordX1 = int(str[begin+1: end])

        begin = end + 2
        end =  str.find(']', begin)
        coordY1 = int(str[begin: end])

        begin = str.find('[', end + 1)
        end =  str.find(',', begin)
        coordX2 = int(str[begin+1: end])

        begin = end + 2
        end =  str.find(']', begin)
        coordY2 = int(str[begin: end])

        begin = end + 2
        end = str.find('\n', begin)
        tan = float(str[begin: end])

        ed = edge(isOpen, [coordX1, coordY1], [coordX2, coordY2], tan)
        tra.addEdge(ed)        

operOR(trapezes[1], trapezes[2])

logger.info("Stop programm")