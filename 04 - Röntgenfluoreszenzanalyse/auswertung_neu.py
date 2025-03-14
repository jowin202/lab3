import numpy as np
import matplotlib.pyplot as plt
from math import log,sqrt

def find_max(data):
    current_max = -100000000000000
    current_index = -1
    for i, element in enumerate(data):
        if element > current_max:
            current_max = element
            current_index = i
    return current_index, current_max


daten_eisen = [8, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 9, 10, 9, 18, 21, 35, 34, 46, 37, 56, 50, 56, 59, 46, 55, 63, 85, 66, 52, 83, 71, 78, 73, 98, 81, 116, 103, 132, 98, 99, 107, 97, 96, 90, 85, 99, 103, 117, 126, 160, 263, 484, 1022, 1941, 3221, 4706, 5657, 5940, 5589, 4938, 4191, 3343, 2637, 2015, 1563, 1127, 967, 780, 597, 455, 259, 155, 95, 45, 23, 16, 17, 9, 12, 6, 13, 4, 12, 9, 8, 10, 5, 9, 10, 4, 6, 8, 21, 25, 23, 33, 36, 35, 37, 39, 33, 28, 24, 30, 21, 19, 11, 14, 24, 9, 8, 10, 7, 9, 7, 7, 10, 11, 10, 3, 6, 6, 5, 7, 11, 8, 13, 7, 10, 9, 9, 16, 10, 10, 3, 3, 5, 7, 7, 4, 3, 0, 1, 3, 3, 1, 6, 1, 3, 8, 4, 2, 1, 3, 3, 4, 4, 4, 1, 5, 5, 3, 1, 4, 3, 4, 0, 4, 2, 6, 1, 3, 5, 4, 6, 6, 19, 3, 11, 6, 11, 20, 18, 20, 20, 23, 12, 15, 8, 3, 4, 4, 6, 4, 8, 3, 4, 3, 7, 4, 0, 2, 6, 5, 3, 3, 7, 5, 4, 3, 5, 1, 1, 1, 1, 3, 6, 1, 3, 6, 3, 0, 2, 4, 3, 2, 2, 1, 6, 3, 1, 3, 4, 4, 2, 1, 4, 4, 5, 1, 5, 3, 2, 0, 0, 1, 3, 2, 0, 1, 2, 1, 4, 0, 1, 4, 2, 1, 0, 5, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 2, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_molybdaen = [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 7, 8, 9, 20, 12, 21, 17, 14, 15, 22, 20, 19, 19, 18, 22, 16, 19, 24, 25, 20, 19, 32, 21, 21, 19, 27, 26, 22, 23, 21, 19, 23, 22, 15, 33, 19, 32, 29, 17, 27, 37, 24, 28, 23, 19, 34, 34, 29, 22, 28, 33, 32, 28, 31, 26, 33, 34, 34, 35, 43, 33, 36, 27, 33, 33, 26, 25, 28, 31, 34, 29, 27, 25, 28, 32, 18, 23, 22, 35, 34, 40, 60, 58, 68, 61, 67, 52, 48, 42, 39, 31, 29, 28, 21, 19, 13, 27, 25, 35, 28, 35, 52, 63, 62, 67, 70, 62, 57, 41, 36, 29, 26, 29, 19, 23, 23, 17, 27, 23, 39, 24, 24, 29, 31, 37, 33, 23, 37, 29, 37, 18, 35, 28, 33, 28, 30, 22, 28, 29, 31, 27, 24, 21, 28, 25, 21, 24, 43, 28, 30, 38, 38, 40, 48, 48, 53, 41, 52, 40, 49, 65, 60, 82, 94, 154, 252, 373, 675, 1142, 1661, 2002, 2073, 2005, 1708, 1484, 1082, 673, 410, 235, 116, 43, 46, 19, 33, 22, 23, 16, 21, 32, 40, 63, 88, 174, 227, 270, 308, 291, 276, 219, 181, 122, 71, 62, 23, 19, 10, 7, 3, 2, 1, 8, 0, 2, 0, 1, 1, 0, 0, 6, 0, 1, 0, 3, 1, 0, 2, 1, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1, 1, 1, 1, 3, 0, 0, 2, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 3, 0, 3, 2, 2, 1, 2, 2, 5, 0, 2, 3, 1, 2, 1, 2, 0, 2, 0, 1, 0, 2, 2, 1, 3, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 4, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 1, 1, 1, 0, 1, 1, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_nickel = [16, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 6, 7, 11, 14, 29, 27, 30, 46, 49, 46, 47, 45, 56, 62, 73, 54, 73, 67, 69, 68, 83, 85, 68, 89, 72, 78, 80, 96, 82, 89, 84, 90, 94, 93, 98, 93, 94, 108, 115, 142, 141, 147, 149, 147, 152, 141, 143, 153, 155, 137, 158, 169, 243, 382, 718, 1431, 2552, 4308, 6157, 7629, 8345, 8032, 7309, 5875, 4712, 3616, 2676, 2048, 1656, 1532, 1378, 1183, 958, 733, 534, 377, 199, 130, 58, 43, 23, 19, 25, 17, 21, 25, 21, 17, 19, 10, 18, 13, 10, 17, 13, 13, 12, 16, 14, 24, 26, 30, 32, 41, 68, 48, 78, 72, 65, 82, 57, 58, 51, 40, 57, 35, 43, 42, 15, 24, 24, 20, 18, 17, 18, 11, 11, 18, 17, 21, 10, 9, 11, 15, 17, 17, 13, 11, 17, 17, 16, 16, 11, 22, 24, 26, 19, 15, 17, 14, 9, 9, 8, 7, 10, 8, 4, 6, 5, 1, 5, 3, 6, 2, 2, 8, 6, 6, 8, 6, 10, 17, 15, 12, 8, 10, 15, 8, 8, 12, 4, 3, 2, 4, 2, 1, 2, 4, 2, 6, 4, 6, 1, 2, 1, 2, 5, 4, 2, 1, 3, 4, 3, 1, 1, 3, 7, 2, 0, 1, 1, 3, 4, 2, 2, 4, 1, 1, 1, 5, 1, 4, 2, 1, 2, 2, 0, 2, 4, 2, 2, 1, 1, 3, 2, 1, 1, 1, 5, 0, 3, 2, 1, 1, 1, 2, 2, 1, 2, 0, 1, 2, 3, 2, 1, 4, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_kupfer = [11, 11, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 4, 9, 10, 18, 18, 31, 38, 54, 61, 38, 62, 83, 50, 69, 57, 68, 59, 70, 85, 63, 77, 78, 71, 71, 78, 86, 104, 83, 92, 106, 95, 90, 92, 109, 88, 90, 89, 105, 96, 105, 98, 110, 110, 142, 123, 161, 154, 145, 163, 155, 127, 147, 135, 140, 155, 165, 164, 183, 222, 315, 644, 1204, 2324, 3836, 6019, 8029, 9184, 9358, 8737, 7525, 5951, 4496, 3343, 2254, 1852, 1603, 1604, 1484, 1352, 1125, 956, 663, 414, 332, 147, 93, 49, 55, 22, 29, 12, 24, 19, 15, 17, 15, 17, 12, 16, 14, 21, 22, 21, 20, 18, 20, 24, 23, 23, 20, 31, 37, 49, 50, 62, 78, 74, 71, 78, 76, 69, 63, 69, 45, 35, 49, 42, 37, 23, 39, 25, 22, 17, 16, 17, 18, 21, 23, 21, 23, 13, 9, 8, 16, 6, 22, 12, 16, 16, 17, 21, 25, 15, 15, 24, 21, 20, 26, 28, 16, 21, 18, 17, 16, 12, 13, 10, 8, 13, 12, 14, 13, 17, 16, 16, 14, 8, 7, 4, 9, 5, 4, 4, 3, 2, 5, 7, 3, 0, 4, 8, 2, 3, 0, 1, 3, 3, 9, 8, 5, 5, 4, 8, 0, 5, 1, 2, 0, 5, 2, 1, 2, 0, 3, 1, 1, 0, 3, 2, 2, 1, 2, 2, 4, 2, 2, 3, 1, 1, 0, 1, 3, 2, 2, 3, 1, 0, 1, 3, 3, 1, 0, 0, 2, 2, 0, 2, 1, 3, 0, 2, 1, 3, 2, 1, 4, 0, 1, 4, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_zink = [19, 19, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 4, 7, 7, 24, 30, 31, 52, 38, 55, 60, 69, 68, 48, 74, 72, 56, 81, 71, 43, 62, 65, 70, 74, 75, 86, 76, 70, 91, 72, 89, 87, 84, 98, 94, 89, 118, 94, 95, 109, 101, 117, 101, 98, 117, 101, 104, 121, 121, 121, 125, 133, 150, 164, 163, 150, 139, 148, 148, 145, 159, 161, 155, 178, 202, 209, 278, 456, 866, 1580, 2861, 4890, 7080, 9067, 9742, 9869, 9076, 7818, 6049, 4426, 3087, 2157, 1655, 1565, 1614, 1598, 1485, 1328, 1054, 837, 587, 381, 259, 163, 95, 74, 45, 30, 24, 33, 28, 33, 26, 23, 19, 26, 19, 19, 16, 21, 25, 19, 24, 18, 16, 14, 20, 22, 24, 27, 21, 36, 43, 52, 52, 63, 91, 101, 81, 84, 95, 93, 65, 65, 67, 49, 42, 42, 35, 34, 35, 33, 44, 26, 22, 18, 19, 16, 19, 23, 18, 23, 23, 26, 18, 16, 19, 21, 13, 13, 18, 16, 20, 20, 23, 14, 28, 20, 21, 31, 22, 24, 34, 32, 25, 30, 23, 22, 12, 11, 9, 6, 7, 6, 7, 7, 3, 1, 1, 2, 1, 1, 4, 1, 4, 3, 5, 5, 6, 3, 7, 5, 4, 4, 8, 1, 4, 3, 2, 3, 3, 3, 4, 4, 4, 2, 2, 4, 4, 2, 3, 2, 3, 2, 1, 2, 3, 2, 4, 0, 2, 1, 2, 2, 0, 1, 3, 1, 0, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 2, 2, 1, 0, 2, 0, 0, 0, 2, 0, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_titan = [1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 4, 4, 7, 16, 20, 26, 25, 38, 36, 20, 27, 32, 30, 29, 23, 24, 30, 32, 45, 93, 191, 395, 737, 1101, 1264, 1384, 1289, 1122, 926, 678, 513, 347, 226, 144, 69, 55, 20, 9, 2, 4, 1, 1, 2, 2, 3, 2, 2, 6, 1, 5, 1, 3, 2, 3, 3, 4, 2, 7, 3, 3, 1, 0, 5, 3, 3, 2, 1, 2, 5, 1, 1, 0, 0, 2, 1, 0, 2, 0, 2, 0, 0, 3, 2, 4, 4, 4, 1, 4, 2, 4, 1, 3, 2, 0, 1, 1, 1, 1, 0, 0, 3, 1, 4, 1, 2, 5, 2, 2, 5, 0, 2, 1, 4, 1, 1, 1, 4, 1, 4, 2, 4, 2, 3, 4, 4, 5, 3, 1, 2, 3, 3, 2, 4, 2, 1, 5, 4, 1, 5, 7, 3, 3, 2, 0, 4, 3, 1, 3, 3, 8, 7, 4, 6, 6, 7, 9, 4, 5, 5, 3, 9, 5, 8, 10, 9, 8, 17, 11, 19, 18, 24, 18, 22, 21, 17, 11, 7, 6, 4, 4, 7, 2, 3, 5, 5, 2, 8, 7, 9, 5, 11, 5, 3, 8, 5, 3, 6, 2, 6, 4, 4, 1, 3, 2, 4, 2, 7, 2, 6, 3, 2, 2, 6, 2, 3, 3, 3, 4, 4, 3, 5, 2, 5, 3, 6, 4, 4, 1, 2, 3, 0, 2, 2, 2, 1, 2, 1, 2, 4, 2, 2, 2, 1, 5, 1, 4, 5, 3, 1, 1, 3, 3, 0, 3, 0, 1, 2, 1, 1, 4, 1, 1, 0, 1, 0, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_silber = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 3, 6, 3, 8, 7, 8, 10, 27, 17, 31, 23, 22, 18, 12, 14, 14, 8, 6, 5, 8, 6, 3, 4, 6, 3, 5, 9, 5, 4, 6, 5, 6, 6, 3, 1, 8, 6, 9, 5, 5, 8, 6, 4, 5, 8, 9, 18, 5, 13, 14, 7, 6, 7, 6, 11, 15, 9, 11, 9, 6, 8, 4, 11, 12, 13, 5, 9, 7, 9, 6, 5, 8, 6, 6, 6, 9, 6, 6, 7, 9, 11, 14, 16, 24, 17, 6, 13, 15, 6, 9, 9, 5, 9, 6, 6, 7, 7, 10, 9, 5, 12, 7, 11, 20, 10, 16, 16, 13, 9, 6, 11, 10, 3, 8, 7, 10, 5, 9, 8, 6, 10, 10, 10, 8, 2, 6, 7, 7, 4, 9, 12, 4, 12, 8, 6, 9, 10, 7, 8, 9, 11, 13, 10, 6, 15, 12, 17, 5, 11, 8, 13, 4, 15, 7, 10, 14, 12, 13, 12, 10, 15, 17, 14, 17, 19, 17, 16, 30, 34, 39, 56, 48, 55, 42, 31, 25, 19, 19, 11, 11, 11, 15, 10, 12, 17, 14, 11, 7, 12, 13, 13, 13, 19, 18, 15, 19, 20, 12, 15, 8, 8, 6, 6, 6, 10, 8, 6, 8, 13, 12, 15, 12, 11, 7, 20, 34, 63, 102, 148, 221, 282, 306, 321, 290, 249, 156, 120, 104, 38, 24, 11, 7, 2, 4, 1, 3, 6, 3, 2, 3, 1, 3, 7, 3, 7, 10, 4, 11, 17, 36, 41, 37, 37, 42, 47, 31, 27, 19, 9, 12, 8, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

daten_zirkonium = [8, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 7, 23, 14, 17, 20, 20, 22, 34, 38, 42, 33, 36, 31, 34, 24, 33, 31, 30, 31, 28, 33, 36, 33, 30, 26, 31, 31, 25, 36, 24, 37, 29, 22, 31, 36, 38, 29, 49, 29, 31, 31, 43, 33, 45, 31, 46, 43, 54, 54, 38, 50, 48, 44, 40, 52, 50, 56, 64, 75, 53, 46, 54, 47, 36, 40, 45, 54, 40, 51, 37, 38, 45, 43, 47, 45, 50, 44, 34, 46, 48, 76, 77, 100, 120, 110, 87, 112, 109, 76, 76, 55, 54, 40, 37, 43, 45, 32, 41, 40, 54, 56, 81, 84, 102, 105, 82, 117, 90, 101, 76, 70, 67, 43, 51, 37, 38, 49, 35, 39, 43, 46, 42, 46, 40, 51, 47, 51, 70, 63, 62, 53, 66, 79, 60, 71, 70, 71, 64, 58, 68, 64, 77, 75, 80, 129, 132, 239, 386, 826, 1438, 2193, 2896, 3482, 3852, 3694, 3226, 2500, 1925, 1252, 779, 431, 220, 104, 79, 74, 61, 64, 51, 82, 116, 184, 299, 405, 483, 565, 516, 511, 440, 358, 277, 202, 124, 50, 40, 23, 17, 7, 8, 6, 9, 7, 2, 2, 8, 6, 0, 7, 2, 4, 1, 5, 5, 2, 3, 5, 4, 1, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 8, 0, 4, 3, 4, 3, 2, 2, 4, 1, 4, 1, 1, 3, 2, 6, 4, 4, 5, 2, 10, 12, 8, 6, 15, 12, 7, 3, 10, 3, 10, 7, 9, 11, 8, 4, 3, 4, 6, 2, 3, 5, 2, 2, 3, 5, 2, 7, 3, 10, 3, 1, 5, 4, 1, 2, 1, 1, 3, 2, 1, 2, 0, 2, 1, 1, 2, 1, 5, 1, 2, 1, 2, 2, 3, 3, 2, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 4, 1, 2, 4, 0, 4, 2, 1, 1, 1, 1, 1, 2, 2, 0, 4, 0, 3, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]



daten_unbekannt = [23, 15, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 8, 13, 11, 15, 19, 37, 30, 52, 53, 50, 53, 65, 60, 58, 74, 76, 78, 75, 66, 86, 97, 85, 72, 86, 87, 85, 89, 80, 89, 98, 104, 106, 99, 99, 109, 92, 124, 117, 120, 116, 126, 118, 131, 143, 159, 182, 182, 177, 161, 166, 159, 164, 161, 190, 167, 177, 177, 204, 257, 361, 688, 1566, 2995, 5443, 8581, 11826, 13563, 13749, 12614, 10647, 7865, 5832, 3955, 2739, 2132, 2165, 2157, 2175, 1890, 1492, 1139, 813, 526, 270, 155, 85, 64, 35, 34, 31, 28, 23, 23, 19, 13, 19, 21, 16, 25, 27, 24, 12, 22, 19, 19, 23, 19, 24, 34, 25, 45, 52, 67, 88, 108, 85, 95, 101, 83, 107, 84, 81, 68, 55, 70, 55, 50, 44, 45, 25, 28, 35, 18, 16, 33, 17, 32, 35, 25, 25, 23, 18, 14, 25, 12, 19, 18, 22, 16, 16, 25, 25, 26, 23, 26, 21, 43, 32, 27, 31, 30, 18, 13, 16, 24, 21, 11, 25, 14, 16, 17, 14, 13, 23, 14, 12, 14, 12, 8, 10, 5, 10, 8, 4, 7, 12, 5, 5, 6, 6, 1, 6, 4, 8, 7, 4, 3, 3, 9, 6, 7, 3, 6, 6, 5, 3, 4, 4, 6, 2, 1, 2, 6, 3, 4, 4, 0, 4, 1, 3, 1, 6, 1, 3, 3, 3, 4, 1, 4, 5, 5, 3, 0, 3, 2, 3, 1, 1, 0, 2, 1, 0, 1, 1, 1, 4, 1, 2, 2, 2, 1, 2, 2, 2, 1, 0, 3, 2, 2, 0, 1, 3, 1, 0, 0, 1, 3, 0, 1, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

Ry = 13.605693122994 # in eV


daten = [daten_titan, daten_eisen, daten_nickel, daten_kupfer, daten_zink, daten_zirkonium, daten_molybdaen, daten_silber, daten_unbekannt]
Z = [22,26,28,29,30,40,42,47,-1]


i1, v1 = find_max(daten_eisen)
i2, v2 = find_max(daten_molybdaen)
print("Eisen, Kanal: " + str(i1) + ", Wert: " + str(v1))
print("daten_molybdaen, Kanal: " + str(i2) + ", Wert: " + str(v2))

k = (17.48 - 6.40) / (i2 - i1)

d = 17.48 - k * i2

print("Transformation k: " + str( k ))
print("Transformation d: " + str( d ))


daten_x_achse = [i for i in range(511)]







fig, ax = plt.subplots()

ax.plot(daten_x_achse, daten_eisen, 'red')
ax.plot(daten_x_achse, daten_molybdaen, 'blue')

ax.legend(['Fe', 'Mo'])

ax.set_xlabel('Kanalnummer')
ax.set_ylabel('Anzahl der Ereignisse')
plt.savefig("vor_kalibrierung_fe_mo.png")
plt.close()








fig, ax = plt.subplots()

ax.plot(daten_x_achse, daten_titan, 'black')
ax.plot(daten_x_achse, daten_eisen, '#FF0000')
ax.plot(daten_x_achse, daten_nickel, '#FFA500')
ax.plot(daten_x_achse, daten_kupfer, '#FFFF00')
ax.plot(daten_x_achse, daten_zink, '#00FF00')
ax.plot(daten_x_achse, daten_zirkonium, '#00FFFF')
ax.plot(daten_x_achse, daten_molybdaen, '#0000FF')
ax.plot(daten_x_achse, daten_silber, '#800080')

ax.legend(['Ti', 'Fe', 'Ni', 'Cu', 'Zn', 'Zr', 'Mo', 'Ag'])


ax.set_xlabel('Kanalnummer')
ax.set_ylabel('Anzahl der Ereignisse')
plt.savefig("vor_kalibrierung_alle.png")
plt.close()




fig, ax = plt.subplots()

ax.plot(daten_x_achse, daten_titan, 'black', alpha=.3)
ax.plot(daten_x_achse, daten_eisen, '#FF0000', alpha=.3)
ax.plot(daten_x_achse, daten_nickel, '#FFA500', alpha=.3)
ax.plot(daten_x_achse, daten_kupfer, '#FFFF00', alpha=.3)
ax.plot(daten_x_achse, daten_zink, '#00FF00', alpha=.3)
ax.plot(daten_x_achse, daten_zirkonium, '#00FFFF', alpha=.3)
ax.plot(daten_x_achse, daten_molybdaen, '#0000FF', alpha=.3)
ax.plot(daten_x_achse, daten_silber, '#800080', alpha=.3)
ax.plot(daten_x_achse, daten_unbekannt, 'black')

ax.legend(['Ti', 'Fe', 'Ni', 'Cu', 'Zn', 'Zr', 'Mo', 'Ag', 'Unbekannt'])


ax.set_xlabel('Kanalnummer')
ax.set_ylabel('Anzahl der Ereignisse')
plt.savefig("vor_kalibrierung_alle_inkl_unbekannt.png")
plt.close()




daten_x_achse_kalibriert = np.array(daten_x_achse)*k + d




fig, ax = plt.subplots()

ax.plot(daten_x_achse_kalibriert, daten_titan, 'black')
ax.plot(daten_x_achse_kalibriert, daten_eisen, '#FF0000')
ax.plot(daten_x_achse_kalibriert, daten_nickel, '#FFA500')
ax.plot(daten_x_achse_kalibriert, daten_kupfer, '#FFFF00')
ax.plot(daten_x_achse_kalibriert, daten_zink, '#00FF00')
ax.plot(daten_x_achse_kalibriert, daten_zirkonium, '#00FFFF')
ax.plot(daten_x_achse_kalibriert, daten_molybdaen, '#0000FF')
ax.plot(daten_x_achse_kalibriert, daten_silber, '#800080')

ax.legend(['Ti', 'Fe', 'Ni', 'Cu', 'Zn', 'Zr', 'Mo', 'Ag'])


ax.set_xlabel('Energie / keV')
ax.set_ylabel('Anzahl der Ereignisse')
plt.savefig("nach_kalibrierung_alle.png")
plt.close()





fig, ax = plt.subplots()

#ax.plot(daten_x_achse_kalibriert, daten_titan, 'black')
#ax.plot(daten_x_achse_kalibriert, daten_eisen, '#FF0000')
#ax.plot(daten_x_achse_kalibriert, daten_nickel, '#FFA500')
ax.plot(daten_x_achse_kalibriert[30:180], daten_kupfer[30:180], '#FFFF00')
#ax.plot(daten_x_achse_kalibriert, daten_zink, '#00FF00')
#ax.plot(daten_x_achse_kalibriert, daten_zirkonium, '#00FFFF')
#ax.plot(daten_x_achse_kalibriert, daten_molybdaen, '#0000FF')
#ax.plot(daten_x_achse_kalibriert, daten_silber, '#800080')
ax.plot(daten_x_achse_kalibriert[30:180], daten_unbekannt[30:180], '#000000')

#ax.legend(['Ti', 'Fe', 'Ni', 'Cu', 'Zn', 'Zr', 'Mo', 'Ag'])
ax.legend(['Cu', 'unbekannt'])


ax.set_xlabel('Energie / keV')
ax.set_ylabel('Anzahl der Ereignisse')
plt.savefig("nach_kalibrierung_kupfer_unbekannt.png")
plt.close()




for messreihe in daten:
    i, v = find_max(messreihe)
    print(str(i) + " \t&\t " + str(round(k*i +d,2)) + " \\\\")
    


sigma = []
for n,messreihe in enumerate(daten):
    i, v = find_max(messreihe)
    abschirmkonst = Z[n] - sqrt(4000*(k*i +d)/(3*Ry))
    print(str(Z[n]) + " \t&\t " + str(round(k*i +d,2)) + " \t&\t " + str( round(abschirmkonst,3)) + " \\\\")
    sigma.append(abschirmkonst)



fig, ax = plt.subplots()

ax.plot(Z[0:-1], sigma[0:-1], 'black', linewidth=0, marker='x') # das letzte nicht miteinbeziehen
ax.plot(Z[0:-1], sigma[0:-1], 'black', linewidth=1, alpha=.3)


ax.set_xlabel('Kernladungszahl Z')
ax.set_ylabel('Abschirmkonstante sigma')
plt.savefig("abschirmkonstante.png")
plt.close()
