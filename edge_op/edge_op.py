import sys
import logging
from trapeze import *
from operations import *

# ������������
logging.basicConfig(
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    stream = sys.stdout,
    level  = logging.INFO
)
logger = logging.getLogger("trapezoid")
logger.info("Start programm")

# ���������� �� �����
logger.info("File reading")
f = open('12 edge')
text = f.read()
f.close()

# ������ �����
logger.info("File parsing")
edgesStr = [] # ������ �����
end = text.find("---- Edges:") # ������� ������ "---- Shapes:"
# ��������� ���� �����
while end != -1:
    begin = end
    # ������� ������ � ����� ���� ������
    begin = text.find('\n', begin) + 1
    end   = text.find('\n', begin)
    # ��������� ������ � ������ �����
    edgesStr.append(text[begin: end])      

# ���������� ����� �����
for ln in edgesStr:
    print(ln)

# ������ �����
trapezes = {}
for str in edgesStr:
    # ��������� ������ ����
    begin = str.find("Edge: M")
    if(begin != -1):
        # ��������� ������ ����
        begin += len("Edge: M")
        end   = str.find(' ', begin)    
        layerNum = int(str[begin: end])
        tra = addTrapezes(trapezes, layerNum)

        # ��������� ��������� ����������� �� �������
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