import os, sys, re
import pynmea2

# file_list = ["A", "B", "C", "D", "E", "F", "G"]

# for file in file_list:
#     ln = 1
#     file += ".txt"
#     # print(f'{file}: ')
#     # file = open('examples/data.log', encoding='utf-8')
#     with open(os.path.join(sys.path[0], "origin_data/", file), "r") as f:
#         for line in f.readlines():
#             # line = line.replace("*", ",*")
#             # if not bool(re.match(r"^\$GP", i)):
#             #     print(ln)
#             #
#             # try:
#             #     msg = pynmea2.parse(line)
#             #     # print(repr(msg))
#             # except pynmea2.ParseError as e:
#             #     print('{} - {} : Parse error: {}'.format(file, ln, e))
#             #     continue
#             if bool(re.match(r"^\$GPGSV", line)):
#                 # print(ln)
#                 # print(line.split(","))
#                 # n = len(re.split(',|*', line))
#                 n = len(line.split(","))
#                 if n != 8 and n != 12 and n != 20: # len not 8, 12 ,20
#                     # print(n)
#                     print(f"{file} - {ln} : {line} >> {n}")
                
#                 try:
#                     msg = pynmea2.parse(line)
#                     # print(f"{file} - {ln} : {line} >> {n}")
#                     print(msg)
#                 except pynmea2.ParseError as e :
#                     print(' * * {} - {} : Parse error: {}'.format(file, ln, e))
#             ln += 1

# line = "$GPGSV,4,3,13,19,56,132,39,20,15,248,24,25,07,310,,28,07,176,*7C"
# line1 = "$GPGSV,4,4,13,30,01,138,43"
# line2 = "$GPGSV,4,2,13,09,29,055,39,12,27,280,38,13,09,189,,17,33,138,4273"
# line3 = "$GPGSV,4,4,14,28,04,175,19,30,02,135,*7F"
line4 = "$GPGSV,4,4,13,50,60,166,35*4F"

# print(line1.split(","))
try:
    # msg = pynmea2.parse(line)
    # print(repr(msg))
    # print(pynmea2.parse(line))
    # print(repr(pynmea2.parse(line).snr_4))
    # print(repr(pynmea2.parse(line1).snr_3))
    # print(repr(pynmea2.parse(line2)))
    print(repr(pynmea2.parse(line4)))
except pynmea2.ParseError as e:
    print('Parse error: {}'.format(e))