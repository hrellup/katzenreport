#!/usr/bin/env python
from PIL import Image
import math
import operator
import sys
import os
from datetime import datetime

#Threshold
TH_AUS=190
TH_EIN=60

#Baseline histogram
avg_ausgang =   [21.05, 20.74, 2.74, 38.53, 45.32, 7.63, 40.58, 33.74, 29.21, 8.95, 27.05, 20.68, 7.84, 18.05, 20.16, 20.58, 20.89, 49.84, 57.68, 56.05, 57.89, 63.58, 81.63, 114.89, 135.63, 138.89, 167.42, 185.95, 200.21, 230.84, 289.0, 330.21, 305.32, 346.63, 346.79, 331.58, 344.26, 385.16, 428.89, 424.32, 515.53, 532.26, 499.63, 558.68, 575.05, 613.47, 600.58, 679.11, 707.37, 673.95, 759.16, 811.68, 828.89, 815.84, 949.0, 989.0, 930.37, 1032.05, 1069.95, 1062.32, 991.89, 1121.53, 1180.32, 1137.74, 1278.37, 1304.21, 1281.0, 1185.89, 1304.42, 1307.37, 1197.16, 1260.42, 1253.11, 1190.74, 1109.32, 1213.37, 1230.79, 1064.58, 1108.16, 1077.47, 1025.68, 942.58, 1018.79, 1020.16, 904.21, 909.0, 873.37, 832.42, 760.0, 817.0, 836.11, 746.11, 777.84, 778.21, 783.63, 765.79, 840.79, 895.21, 783.74, 770.37, 727.11, 683.21, 575.11, 575.68, 504.16, 410.79, 403.16, 396.47, 371.47, 316.95, 324.32, 286.11, 237.37, 243.32, 232.21, 213.42, 182.68, 173.05, 154.32, 141.21, 150.79, 166.37, 148.37, 119.74, 124.95, 126.16, 121.32, 137.68, 157.32, 139.53, 134.11, 138.26, 132.21, 128.79, 136.68, 140.79, 120.42, 110.68, 108.32, 107.11, 106.26, 112.84, 116.58, 104.21, 94.95, 97.95, 109.74, 107.21, 122.95, 136.26, 136.32, 132.58, 152.89, 156.05, 161.58, 199.84, 221.42, 233.21, 227.11, 258.58, 266.37, 245.21, 268.95, 254.42, 227.0, 198.68, 175.42, 140.37, 98.58, 72.11, 50.95, 30.11, 18.21, 12.58, 11.11, 8.42, 8.05, 5.89, 5.16, 3.63, 3.26, 2.84, 3.16, 2.47, 2.68, 3.0, 2.68, 2.63, 3.74, 3.32, 4.53, 4.74, 4.63, 4.63, 4.42, 4.53, 3.95, 5.21, 3.84, 3.58, 3.21, 3.21, 3.42, 2.74, 2.58, 2.47, 1.79, 1.42, 1.47, 1.42, 1.32, 1.26, 1.42, 1.11, 1.26, 1.0, 0.74, 0.89, 0.79, 1.37, 1.05, 0.95, 0.89, 1.0, 0.74, 0.63, 0.42, 0.42, 0.37, 0.32, 0.47, 0.42, 0.74, 0.53, 0.79, 0.74, 0.84, 0.84, 0.47, 0.63, 0.42, 0.37, 0.53, 0.37, 0.26, 0.58, 0.63, 0.53, 0.84, 0.89, 1.58, 2.05, 3.47, 2.16, 5.79, 226.95, 309.21, 36.53, 16.79, 11.68, 9.63, 7.26, 5.89, 4.47, 3.32, 4.11, 3.37, 1.74, 2.53, 2.68, 2.63, 4.89, 15.42, 34.74, 50.0, 55.0, 54.74, 64.11, 98.26, 153.79, 186.37, 217.79, 249.37, 288.37, 320.26, 386.16, 452.32, 407.53, 384.26, 401.42, 440.47, 552.32, 688.11, 767.37, 728.0, 722.68, 742.53, 805.0, 904.47, 964.37, 952.32, 837.47, 816.32, 875.26, 1010.37, 1147.95, 1243.42, 1175.58, 1005.74, 897.58, 903.0, 1006.84, 1159.58, 1270.95, 1189.79, 1009.47, 920.84, 921.16, 951.89, 1047.0, 1199.05, 1229.79, 1128.37, 1119.26, 1156.42, 1219.68, 1326.32, 1453.32, 1339.37, 1088.95, 973.79, 951.79, 947.0, 998.53, 1034.63, 950.37, 763.68, 661.68, 623.47, 627.05, 689.79, 778.37, 832.95, 715.05, 646.47, 612.58, 620.68, 679.68, 813.84, 883.47, 742.47, 607.58, 548.58, 544.42, 553.26, 620.11, 640.68, 494.05, 361.84, 322.63, 312.95, 317.68, 356.68, 353.95, 279.74, 221.84, 180.16, 184.47, 185.21, 196.79, 208.21, 184.89, 153.89, 133.53, 135.32, 135.63, 151.74, 167.63, 157.26, 138.58, 124.37, 127.68, 119.58, 127.74, 144.11, 142.42, 117.95, 111.58, 103.32, 100.26, 103.0, 108.0, 104.47, 81.26, 74.58, 71.26, 71.0, 81.21, 91.74, 95.42, 81.68, 73.58, 72.84, 73.89, 85.58, 105.42, 115.89, 104.89, 101.05, 95.58, 99.58, 104.74, 130.11, 154.58, 157.84, 156.37, 165.53, 191.42, 240.58, 321.16, 367.89, 334.74, 289.95, 235.95, 212.53, 178.37, 149.79, 119.53, 79.26, 46.58, 29.53, 19.74, 13.37, 11.26, 12.0, 8.32, 7.11, 5.26, 4.16, 5.42, 3.53, 3.74, 2.68, 2.0, 2.0, 2.95, 2.84, 4.47, 4.84, 4.95, 3.47, 4.32, 4.95, 5.05, 6.58, 5.05, 4.58, 3.68, 2.16, 3.32, 2.26, 3.47, 2.42, 2.47, 1.89, 1.53, 1.58, 2.16, 1.42, 1.26, 1.74, 1.05, 2.0, 1.42, 0.63, 1.0, 1.74, 1.11, 1.11, 0.47, 1.16, 0.68, 1.11, 0.79, 0.47, 0.47, 1.0, 0.63, 0.79, 0.53, 1.05, 1.0, 0.74, 1.53, 1.74, 2.0, 1.84, 1.74, 2.16, 2.26, 1.53, 1.58, 2.53, 2.63, 2.95, 4.68, 7.95, 16.95, 34.95, 49.74, 57.63, 57.63, 389.89, 4.74, 9.0, 3.84, 4.37, 3.68, 2.53, 1.68, 1.11, 1.74, 1.11, 2.68, 6.53, 15.53, 30.05, 47.84, 70.05, 86.68, 132.68, 165.21, 196.42, 265.11, 302.26, 378.95, 412.74, 524.95, 595.95, 600.53, 691.53, 685.05, 787.58, 779.63, 909.58, 916.84, 867.79, 964.95, 930.05, 1009.53, 968.16, 1108.37, 1113.42, 1032.37, 1084.79, 1018.84, 1074.05, 981.58, 1094.11, 1055.21, 948.47, 987.84, 924.0, 1005.95, 939.26, 1050.95, 1051.37, 967.11, 1039.58, 987.05, 1074.11, 1019.58, 1120.16, 1157.37, 1074.32, 1172.21, 1119.42, 1198.16, 1104.47, 1197.42, 1167.0, 1024.26, 1033.74, 939.84, 981.63, 838.95, 874.47, 831.63, 716.84, 727.63, 657.47, 677.95, 632.26, 671.47, 670.47, 610.37, 635.74, 599.16, 638.16, 577.58, 623.37, 610.0, 520.37, 533.32, 477.58, 491.05, 440.05, 472.0, 458.42, 388.53, 393.53, 351.37, 367.68, 327.32, 340.63, 304.16, 258.16, 244.26, 218.63, 210.89, 191.21, 189.0, 172.32, 159.84, 157.26, 143.53, 146.42, 128.32, 136.84, 133.16, 120.84, 124.21, 110.32, 105.47, 97.89, 103.26, 96.53, 92.16, 94.32, 90.11, 89.37, 83.63, 81.47, 80.11, 74.0, 82.42, 72.79, 77.89, 67.26, 68.79, 66.42, 65.63, 69.05, 64.16, 68.63, 66.63, 70.58, 73.05, 76.32, 83.79, 80.68, 97.37, 85.58, 95.05, 93.32, 100.32, 107.11, 106.84, 125.74, 126.47, 139.0, 146.42, 172.21, 208.11, 207.0, 253.26, 237.16, 262.63, 241.0, 239.47, 226.05, 183.74, 170.37, 138.05, 115.74, 93.42, 69.37, 55.74, 34.95, 27.84, 19.79, 14.84, 11.47, 9.74, 6.79, 6.16, 5.84, 4.11, 4.26, 4.26, 4.32, 4.37, 5.89, 7.16, 5.63, 6.63, 6.47, 5.63, 6.63, 5.68, 6.16, 5.68, 4.63, 4.05, 3.16, 3.47, 2.95, 2.84, 3.21, 2.32, 2.68, 2.05, 2.32, 1.79, 2.11, 1.32, 2.16, 1.68, 2.26, 1.58, 2.74, 1.53, 2.89, 4.26, 1.47, 5.16, 1.89, 5.21, 2.16, 6.53, 7.05, 1.47, 6.95, 2.16, 7.26, 2.32, 7.26, 2.89, 8.32, 8.95, 2.42, 9.79, 3.0, 11.53, 2.0, 16.37, 20.79, 2.47, 23.32, 1.79, 26.11, 2.0, 20.89, 15.74, 1.0, 10.84, 0.79, 13.58]
avg_eingang =  [31.81, 7.14, 1.1, 16.57, 22.86, 4.43, 28.0, 34.57, 33.48, 14.24, 29.29, 28.33, 17.24, 28.52, 35.62, 46.57, 44.95, 79.62, 121.86, 133.62, 183.71, 198.05, 218.48, 218.67, 202.33, 198.95, 208.43, 212.14, 215.0, 220.81, 229.0, 200.86, 191.48, 211.14, 220.14, 223.29, 249.71, 262.24, 265.86, 256.86, 257.76, 264.33, 258.43, 274.24, 279.76, 276.14, 264.95, 279.9, 286.62, 271.62, 291.19, 313.33, 304.86, 300.43, 314.14, 309.57, 304.05, 333.14, 351.62, 335.95, 326.81, 353.1, 355.24, 351.29, 381.33, 422.95, 421.38, 409.19, 431.81, 425.57, 409.48, 446.57, 472.95, 451.62, 417.38, 432.81, 434.19, 413.33, 442.24, 448.95, 443.33, 415.76, 448.43, 455.76, 446.33, 480.38, 506.62, 520.9, 517.81, 576.14, 624.05, 621.0, 709.57, 776.52, 807.29, 834.48, 962.67, 1027.9, 938.1, 959.38, 952.81, 878.57, 782.9, 777.57, 788.67, 758.38, 848.9, 924.48, 959.38, 943.29, 976.48, 939.14, 797.38, 730.38, 612.0, 493.57, 448.86, 506.9, 566.95, 599.0, 713.52, 792.48, 821.76, 842.76, 982.86, 1076.57, 1022.62, 1081.81, 1047.43, 938.14, 823.38, 819.95, 783.95, 671.14, 657.0, 605.86, 497.86, 430.14, 391.14, 347.48, 280.81, 253.71, 217.57, 182.57, 161.1, 166.52, 172.43, 167.95, 192.86, 219.48, 265.38, 293.81, 363.29, 434.1, 451.81, 535.62, 594.9, 631.86, 597.81, 646.0, 627.14, 559.19, 542.52, 517.52, 470.57, 385.1, 344.76, 286.71, 221.19, 181.67, 151.0, 130.43, 106.33, 99.0, 97.33, 79.48, 75.62, 76.48, 75.57, 69.67, 74.19, 73.38, 66.57, 70.0, 74.95, 78.43, 67.48, 72.19, 70.05, 64.67, 65.52, 70.9, 66.0, 58.62, 56.81, 47.76, 43.86, 41.86, 42.71, 39.57, 33.24, 30.9, 24.67, 20.38, 17.05, 18.71, 15.43, 12.33, 11.38, 11.86, 10.29, 11.0, 10.95, 9.9, 8.24, 7.9, 8.57, 7.71, 9.43, 10.1, 10.29, 10.14, 8.62, 7.9, 5.81, 6.19, 4.48, 5.24, 5.19, 4.86, 5.95, 5.52, 5.43, 5.43, 5.76, 5.14, 3.81, 3.81, 3.48, 2.19, 2.33, 1.9, 1.52, 1.14, 0.76, 0.52, 0.52, 1.05, 2.62, 3.81, 0.95, 4.86, 4.0, 2.0, 4.38, 216.86, 311.1, 27.67, 19.19, 15.24, 9.67, 6.57, 5.05, 4.38, 3.71, 3.48, 3.24, 3.48, 4.48, 6.29, 10.9, 17.05, 24.24, 36.43, 57.0, 92.95, 128.29, 153.62, 191.9, 213.95, 212.1, 187.38, 190.0, 198.67, 211.9, 234.62, 235.62, 217.52, 196.48, 195.9, 211.38, 244.95, 279.81, 307.29, 288.1, 269.67, 263.57, 264.52, 282.05, 317.1, 329.1, 299.52, 280.29, 273.95, 285.71, 305.76, 339.29, 348.24, 324.0, 282.9, 279.81, 292.95, 330.52, 393.67, 401.52, 363.76, 337.05, 330.38, 339.38, 376.24, 434.05, 477.19, 462.05, 431.52, 434.05, 442.43, 485.48, 542.76, 577.95, 516.52, 459.52, 442.33, 434.14, 453.0, 482.95, 485.19, 428.9, 398.1, 390.19, 401.62, 451.43, 540.33, 580.95, 562.57, 555.76, 560.24, 589.76, 634.9, 726.19, 780.67, 694.33, 574.0, 527.29, 520.76, 541.9, 607.57, 673.05, 639.62, 576.95, 554.14, 575.43, 611.9, 696.33, 759.14, 798.33, 861.43, 901.48, 868.43, 816.19, 836.14, 873.71, 831.33, 841.29, 868.19, 917.24, 1077.48, 1367.76, 1668.1, 1708.05, 1530.24, 1254.62, 973.0, 852.52, 859.86, 929.81, 901.95, 805.62, 743.86, 654.29, 553.9, 457.86, 397.0, 305.67, 218.81, 173.62, 149.48, 124.52, 118.81, 112.1, 110.0, 99.33, 82.76, 82.1, 83.48, 88.95, 110.62, 134.71, 145.81, 145.9, 150.81, 168.57, 192.1, 251.0, 347.52, 400.86, 418.24, 419.0, 447.57, 495.95, 592.0, 716.9, 740.71, 680.43, 589.24, 550.1, 497.05, 434.29, 373.43, 300.86, 217.76, 153.43, 124.24, 101.67, 101.19, 102.9, 95.81, 80.38, 65.62, 59.9, 59.05, 59.29, 70.95, 73.19, 63.29, 55.1, 49.24, 50.05, 53.67, 64.52, 80.81, 85.48, 71.19, 67.0, 63.71, 59.81, 68.05, 65.14, 58.81, 41.81, 37.43, 33.38, 34.29, 34.38, 39.1, 36.38, 28.33, 22.19, 20.62, 18.81, 16.71, 18.67, 17.81, 14.81, 11.48, 10.95, 10.81, 12.48, 13.9, 13.81, 12.1, 9.9, 8.1, 7.95, 7.48, 7.57, 7.67, 6.52, 6.95, 6.1, 7.81, 8.0, 6.95, 7.38, 7.1, 7.76, 10.0, 9.95, 8.14, 5.62, 4.24, 2.48, 2.19, 2.0, 2.43, 3.9, 6.38, 12.38, 26.1, 50.43, 49.29, 33.86, 45.24, 382.29, 2.57, 8.81, 2.19, 9.19, 4.81, 1.43, 3.71, 1.33, 2.24, 2.05, 1.95, 2.81, 5.43, 10.62, 17.33, 31.52, 48.0, 67.9, 89.43, 103.71, 132.43, 147.71, 167.52, 180.33, 189.19, 198.29, 200.48, 206.71, 202.14, 210.67, 218.48, 228.14, 229.29, 240.67, 257.67, 255.67, 278.43, 275.52, 287.33, 303.76, 306.62, 314.57, 300.19, 318.1, 320.0, 333.05, 335.67, 325.9, 346.19, 339.76, 360.86, 356.95, 374.19, 381.57, 379.0, 396.0, 392.9, 402.38, 405.38, 441.29, 452.1, 460.86, 491.14, 485.33, 521.38, 514.48, 557.67, 568.81, 562.19, 570.81, 543.9, 567.62, 540.95, 555.71, 548.19, 511.52, 520.86, 498.29, 518.24, 496.29, 530.76, 545.29, 515.57, 553.43, 532.81, 555.48, 544.1, 568.0, 572.95, 546.81, 559.33, 545.33, 575.9, 565.33, 640.9, 653.19, 661.1, 718.9, 721.1, 765.86, 755.14, 822.43, 824.1, 772.29, 805.48, 773.05, 816.62, 804.67, 903.76, 951.9, 934.52, 995.19, 963.57, 1028.0, 999.24, 1048.33, 1048.71, 1017.1, 1016.24, 904.67, 861.24, 765.9, 756.9, 719.52, 691.81, 709.76, 673.29, 723.81, 690.24, 706.33, 620.19, 576.52, 477.0, 361.52, 323.24, 262.19, 220.81, 182.38, 162.67, 144.81, 120.0, 118.52, 102.29, 100.9, 101.71, 101.05, 111.48, 113.24, 130.95, 142.1, 159.95, 177.14, 194.71, 230.33, 230.38, 266.9, 285.24, 315.71, 343.86, 393.9, 438.81, 458.0, 517.1, 519.71, 567.29, 544.33, 573.57, 557.62, 487.9, 451.05, 379.1, 347.62, 289.33, 258.62, 217.14, 164.14, 144.1, 115.14, 100.38, 84.29, 82.48, 77.67, 68.62, 70.9, 62.19, 56.76, 53.43, 51.48, 58.48, 56.9, 61.86, 58.14, 65.62, 63.24, 66.67, 67.9, 63.95, 65.24, 59.52, 62.1, 55.14, 61.33, 55.14, 46.05, 45.95, 38.76, 37.05, 33.1, 30.9, 31.14, 26.38, 25.19, 19.38, 23.38, 16.43, 23.76, 17.38, 22.33, 15.1, 24.29, 23.48, 15.43, 21.52, 14.14, 19.33, 12.24, 15.19, 15.9, 11.24, 13.14, 9.14, 11.24, 8.81, 12.24, 8.9, 15.14, 16.57, 8.81, 15.43, 5.62, 16.95, 3.62, 20.57, 21.19, 3.62, 17.57, 1.38, 13.19, 0.86, 7.86, 4.0, 0.62, 3.14, 0.9, 20.1]
avg_eingang_crop =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.43, 0.67, 0.52, 0.9, 1.05, 1.52, 1.81, 2.33, 2.71, 3.38, 4.48, 4.76, 7.38, 9.86, 12.86, 20.38, 24.86, 28.29, 32.05, 32.67, 35.71, 40.33, 46.62, 47.05, 46.1, 56.33, 56.29, 61.38, 72.95, 85.19, 92.95, 89.0, 89.95, 94.95, 92.71, 101.14, 113.38, 119.62, 112.05, 127.95, 130.48, 124.05, 138.9, 161.38, 165.71, 170.24, 179.14, 179.76, 178.38, 199.52, 223.43, 219.24, 212.1, 234.76, 239.9, 241.62, 268.76, 306.33, 308.81, 298.57, 311.1, 300.57, 286.38, 308.71, 320.76, 294.24, 261.19, 262.71, 247.57, 235.95, 258.24, 257.95, 255.52, 238.38, 261.38, 262.0, 259.43, 285.1, 297.95, 296.43, 282.19, 303.76, 308.81, 288.0, 315.9, 327.1, 313.62, 299.05, 328.38, 335.14, 303.29, 313.0, 338.81, 324.81, 292.19, 296.86, 294.52, 282.52, 291.81, 285.62, 256.9, 209.81, 203.1, 173.24, 140.48, 140.48, 149.29, 145.43, 139.19, 138.9, 142.24, 139.05, 140.29, 147.57, 136.95, 120.38, 110.62, 103.14, 94.05, 92.95, 96.95, 89.14, 80.29, 77.24, 75.33, 68.0, 70.43, 67.48, 54.67, 50.9, 43.81, 43.76, 42.57, 46.0, 45.38, 37.52, 40.0, 42.33, 45.1, 44.29, 55.48, 60.29, 68.24, 71.38, 91.52, 107.24, 112.95, 135.05, 139.57, 139.48, 134.43, 146.24, 147.71, 138.52, 142.71, 138.1, 126.19, 108.0, 103.33, 86.57, 64.76, 51.24, 36.86, 26.52, 21.81, 19.05, 20.48, 17.62, 16.0, 18.0, 19.14, 18.29, 21.57, 23.71, 21.52, 25.33, 25.33, 23.24, 16.9, 16.57, 12.81, 10.76, 7.86, 7.95, 5.29, 2.48, 2.38, 1.24, 0.81, 0.19, 0.19, 0.1, 0.0, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14, 0.62, 1.14, 1.76, 2.19, 2.05, 2.43, 3.48, 4.86, 8.1, 11.1, 17.14, 24.43, 31.76, 33.81, 36.38, 36.57, 42.62, 50.33, 54.29, 54.29, 58.05, 63.9, 74.62, 97.1, 112.95, 112.9, 105.57, 99.95, 103.52, 113.0, 125.24, 143.81, 141.62, 122.43, 119.14, 128.14, 134.29, 158.1, 176.19, 183.19, 160.43, 146.48, 150.76, 165.71, 196.14, 251.48, 253.0, 219.62, 201.62, 206.05, 220.0, 248.86, 301.48, 335.52, 317.86, 293.1, 295.19, 293.33, 314.24, 347.71, 366.95, 305.38, 258.14, 249.19, 236.95, 255.0, 276.57, 289.05, 243.86, 212.57, 210.86, 212.81, 240.9, 289.86, 317.9, 291.14, 270.67, 264.62, 274.62, 296.95, 372.43, 413.57, 375.29, 319.1, 297.57, 300.1, 314.38, 356.24, 399.43, 363.33, 298.86, 273.14, 276.38, 274.57, 277.19, 264.67, 198.62, 134.62, 111.14, 104.86, 98.05, 108.05, 120.52, 110.14, 98.33, 88.57, 90.33, 93.9, 111.19, 127.38, 134.29, 118.38, 105.86, 98.24, 97.19, 97.86, 100.24, 91.19, 77.33, 67.19, 61.05, 54.0, 57.29, 57.67, 60.52, 49.67, 42.33, 40.19, 34.38, 37.81, 37.67, 43.0, 38.81, 33.14, 33.14, 32.29, 36.86, 48.67, 59.71, 60.33, 57.1, 60.95, 64.33, 72.1, 88.9, 118.76, 125.48, 120.76, 116.38, 116.48, 126.62, 154.67, 181.9, 180.24, 156.86, 137.1, 122.0, 99.57, 75.9, 60.95, 40.57, 27.71, 24.86, 19.52, 17.05, 17.38, 18.81, 18.9, 18.1, 14.81, 12.38, 15.19, 15.52, 19.76, 19.05, 14.76, 13.67, 11.67, 13.1, 14.0, 17.57, 21.71, 21.71, 14.1, 11.43, 10.57, 6.33, 5.81, 4.86, 3.19, 0.95, 0.57, 0.19, 0.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.0, 0.19, 0.24, 0.48, 1.0, 1.38, 2.24, 2.71, 4.1, 5.1, 7.71, 10.24, 12.71, 17.1, 20.19, 24.33, 29.43, 34.9, 39.81, 41.86, 50.43, 53.43, 62.86, 68.43, 82.43, 92.05, 95.19, 110.52, 109.95, 120.67, 121.81, 128.95, 138.05, 135.05, 146.86, 138.0, 155.33, 152.48, 167.48, 166.76, 155.9, 167.62, 165.0, 184.19, 180.24, 197.33, 208.52, 203.9, 219.62, 219.24, 230.48, 237.29, 259.9, 274.29, 274.14, 303.14, 294.67, 321.76, 311.05, 341.29, 338.71, 331.71, 335.19, 311.05, 321.9, 299.05, 306.24, 283.19, 255.52, 252.1, 242.86, 242.81, 234.1, 249.67, 261.33, 249.9, 271.86, 263.76, 280.14, 278.57, 309.14, 317.1, 314.48, 327.48, 315.14, 336.43, 323.76, 369.71, 363.9, 351.14, 358.14, 335.62, 325.48, 293.57, 287.19, 253.29, 207.95, 186.0, 155.29, 139.81, 122.81, 114.48, 102.95, 94.95, 93.0, 83.9, 89.33, 81.38, 81.48, 85.76, 83.1, 89.67, 87.95, 95.14, 93.76, 98.33, 94.43, 91.43, 87.19, 74.14, 72.24, 71.29, 63.95, 62.29, 55.0, 52.71, 53.19, 51.29, 51.24, 48.67, 45.0, 46.1, 44.81, 43.38, 42.14, 38.05, 41.05, 41.14, 40.29, 47.1, 48.67, 58.14, 61.29, 66.48, 75.05, 80.33, 96.67, 96.1, 111.14, 114.57, 120.86, 126.29, 134.48, 143.24, 144.38, 152.81, 139.05, 134.05, 122.86, 103.29, 90.52, 71.62, 60.1, 36.24, 31.1, 22.9, 18.05, 17.57, 17.33, 19.0, 16.57, 16.05, 16.19, 14.62, 14.33, 13.81, 18.43, 13.48, 12.1, 9.62, 10.86, 10.62, 9.81, 12.19, 11.76, 14.67, 13.71, 15.05, 16.48, 12.33, 11.57, 9.86, 9.48, 6.33, 5.52, 3.76, 2.48, 1.48, 0.62, 0.33, 0.19, 0.05, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
avg_ausgang_crop =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11, 0.26, 0.05, 0.42, 0.68, 0.42, 0.42, 0.47, 0.21, 0.21, 0.16, 0.26, 0.26, 0.16, 0.53, 0.74, 1.68, 2.68, 4.47, 7.63, 11.58, 17.26, 27.58, 47.11, 61.63, 70.21, 85.42, 90.79, 89.63, 88.84, 106.95, 115.11, 119.95, 139.21, 139.26, 131.0, 138.79, 144.58, 154.21, 146.58, 168.16, 175.53, 172.37, 189.47, 206.47, 207.84, 207.26, 236.42, 254.16, 238.0, 260.47, 268.53, 262.74, 248.53, 286.79, 299.68, 301.26, 354.47, 387.58, 405.11, 399.58, 463.79, 487.53, 463.21, 507.11, 510.42, 472.37, 441.21, 477.53, 468.42, 393.63, 415.26, 397.79, 367.11, 329.95, 350.63, 350.42, 312.89, 312.84, 293.53, 274.26, 245.84, 267.32, 282.42, 263.68, 290.74, 293.63, 294.84, 288.95, 311.05, 334.37, 303.47, 314.0, 292.21, 268.32, 239.74, 229.63, 202.05, 161.26, 151.32, 147.21, 140.79, 121.16, 123.21, 112.53, 99.0, 99.58, 98.37, 89.47, 76.26, 70.37, 60.58, 54.53, 61.89, 70.0, 58.84, 44.32, 45.95, 43.95, 41.16, 49.47, 57.63, 49.11, 46.68, 43.47, 39.32, 38.58, 38.95, 42.95, 35.84, 32.26, 30.26, 30.47, 31.74, 38.63, 45.63, 41.11, 38.89, 37.47, 45.32, 49.74, 60.37, 70.53, 61.11, 57.63, 59.63, 54.74, 54.26, 63.05, 62.05, 57.26, 52.74, 55.53, 64.11, 66.53, 78.47, 74.95, 64.21, 52.16, 49.42, 42.21, 30.32, 27.42, 20.84, 13.32, 9.37, 6.0, 4.74, 3.21, 2.26, 1.89, 1.74, 1.16, 0.68, 0.63, 0.84, 0.53, 0.53, 1.0, 0.95, 1.11, 1.95, 1.47, 2.0, 1.74, 2.05, 1.32, 1.47, 1.16, 0.53, 0.68, 0.26, 0.47, 0.16, 0.0, 0.16, 0.21, 0.16, 0.21, 0.26, 0.05, 0.16, 0.05, 0.16, 0.16, 0.05, 0.11, 0.26, 0.0, 0.05, 0.11, 0.16, 0.16, 0.11, 0.11, 0.16, 0.11, 0.21, 0.21, 0.21, 0.11, 0.21, 0.11, 0.11, 0.16, 0.21, 0.16, 0.32, 0.26, 0.32, 0.32, 0.16, 0.26, 0.11, 0.26, 0.26, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16, 0.42, 0.53, 0.32, 0.47, 0.47, 0.26, 0.32, 0.26, 0.63, 1.16, 4.32, 11.58, 18.84, 31.74, 44.0, 52.26, 78.16, 97.95, 105.84, 111.74, 115.68, 127.89, 151.37, 178.63, 190.11, 169.74, 163.84, 168.84, 181.26, 206.74, 220.37, 235.37, 209.16, 213.53, 233.05, 268.11, 298.74, 310.84, 286.58, 236.63, 219.84, 219.58, 255.68, 311.95, 349.63, 332.37, 300.84, 300.89, 324.42, 353.47, 408.47, 482.89, 490.11, 461.53, 451.95, 449.32, 476.42, 527.89, 571.32, 500.47, 395.37, 340.11, 329.26, 319.47, 341.95, 345.84, 317.95, 258.58, 226.42, 211.26, 218.63, 240.58, 274.47, 297.42, 259.58, 240.63, 231.32, 230.37, 251.47, 300.47, 327.21, 282.47, 242.26, 208.32, 208.42, 204.63, 234.42, 246.47, 195.53, 143.68, 126.37, 116.32, 111.63, 121.58, 129.79, 109.16, 89.0, 73.58, 71.0, 68.05, 71.63, 77.74, 68.89, 53.79, 45.89, 47.79, 46.68, 52.95, 64.74, 61.95, 48.11, 41.32, 42.26, 40.95, 44.95, 56.16, 54.63, 46.68, 42.74, 39.11, 35.58, 36.89, 38.84, 39.63, 31.42, 28.68, 29.47, 28.42, 34.05, 41.68, 40.58, 34.84, 31.79, 33.89, 36.26, 45.95, 58.26, 61.37, 54.95, 52.89, 50.58, 50.05, 51.05, 57.42, 61.58, 60.37, 56.21, 56.95, 60.37, 73.68, 94.79, 91.0, 66.89, 55.32, 46.21, 39.68, 35.74, 29.21, 26.47, 18.05, 11.89, 7.95, 6.58, 5.11, 4.89, 4.84, 3.68, 3.0, 2.26, 1.74, 1.89, 1.26, 1.47, 0.79, 1.16, 0.79, 1.26, 1.47, 2.32, 2.21, 2.37, 1.84, 1.42, 1.89, 1.11, 1.32, 1.32, 0.79, 0.21, 0.21, 0.21, 0.32, 0.32, 0.11, 0.26, 0.16, 0.05, 0.47, 0.32, 0.11, 0.05, 0.21, 0.16, 0.32, 0.37, 0.16, 0.16, 0.26, 0.11, 0.26, 0.11, 0.47, 0.21, 0.47, 0.21, 0.11, 0.21, 0.42, 0.21, 0.21, 0.21, 0.16, 0.32, 0.0, 0.21, 0.37, 0.47, 0.68, 0.74, 1.05, 0.84, 0.58, 0.26, 0.53, 0.26, 0.16, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11, 0.05, 0.21, 0.26, 0.16, 0.32, 0.63, 1.32, 1.68, 5.32, 9.84, 17.0, 28.74, 39.16, 55.47, 65.47, 92.89, 113.53, 126.84, 150.53, 156.11, 166.89, 170.84, 200.74, 199.11, 194.74, 217.89, 214.74, 236.21, 231.16, 267.58, 277.79, 254.11, 277.63, 266.63, 283.37, 268.79, 304.53, 299.16, 281.58, 310.05, 293.42, 335.11, 317.37, 371.79, 379.47, 362.47, 390.63, 374.68, 414.05, 386.68, 429.37, 451.58, 408.95, 445.63, 425.37, 453.26, 413.95, 451.16, 439.84, 382.21, 380.53, 342.95, 357.68, 292.95, 311.95, 291.74, 255.89, 252.68, 239.74, 236.84, 227.11, 241.11, 242.47, 218.16, 237.21, 220.37, 235.95, 210.53, 223.74, 220.84, 183.84, 196.95, 173.58, 179.89, 162.63, 170.79, 160.16, 140.95, 136.11, 120.74, 124.21, 110.32, 113.95, 103.84, 89.21, 82.21, 73.68, 68.11, 65.37, 61.95, 56.37, 54.32, 53.95, 48.63, 48.16, 44.47, 49.74, 51.74, 46.42, 49.0, 47.26, 46.79, 44.95, 48.0, 45.26, 46.68, 48.53, 45.89, 45.79, 44.26, 42.79, 41.68, 35.79, 40.32, 35.0, 35.58, 30.68, 32.53, 31.26, 30.74, 34.68, 30.89, 34.0, 35.68, 36.58, 40.21, 42.32, 48.37, 45.32, 56.47, 48.84, 54.47, 53.37, 53.79, 56.79, 52.58, 63.42, 59.63, 59.47, 59.68, 65.11, 73.47, 66.89, 71.0, 58.05, 53.32, 46.32, 39.68, 33.05, 26.79, 25.53, 17.68, 14.68, 11.32, 7.47, 6.37, 5.0, 4.32, 3.42, 3.26, 2.74, 2.58, 3.11, 2.74, 3.21, 2.26, 2.53, 2.89, 2.53, 2.53, 3.37, 4.21, 3.21, 3.32, 2.89, 2.21, 2.68, 1.74, 2.05, 1.89, 1.53, 0.95, 0.74, 0.47, 0.58, 0.32, 0.53, 0.37, 0.74, 0.26, 0.37, 0.32, 0.95, 0.37, 0.37, 0.37, 0.53, 0.58, 0.58, 0.32, 0.42, 0.37, 0.32, 0.21, 0.21, 0.32, 0.37, 0.26, 0.42, 0.16, 0.21, 0.42, 0.42, 0.74, 0.26, 1.05, 0.32, 0.63, 0.84, 0.42, 0.42, 0.11, 0.32, 0.26, 0.47, 0.42, 0.42, 0.37, 0.37, 0.42, 0.42, 0.21, 0.11, 0.16, 0.26, 1.05]


def img_cmp(img):
    img = Image.open(img)
    h2 = img.histogram()
    rmsa = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, avg_ausgang, h2))/len(h2))
    rmse = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, avg_eingang, h2))/len(h2))
    return (round(rmsa), round(rmse))
    
def img_cmp_crop(img):
    img = Image.open(img).crop((157,16,280,215))
    h2 = img.histogram()
    rmsa = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, avg_ausgang_crop, h2))/len(h2))
    rmse = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, avg_eingang_crop, h2))/len(h2))
    return (round(rmsa), round(rmse))

def avg(path):
    histo_list = []

    for filename in os.listdir(path):
        img = Image.open(path+filename)
        histo_list.append(img.histogram())
        #print img_cmp(path+filename)
    hist_len = len(histo_list) *1.0
    avg_list = [round(sum(x)/hist_len,2) for x in zip(*histo_list)]
    return avg_list

def avg_crop(path):
    histo_list = []

    for filename in os.listdir(path):
        img = Image.open(path+filename).crop((157,16,280,215))
        img = Image.open(path+filename).crop((157,16,280,215))
        histo_list.append(img.histogram())
        #print img_cmp(path+filename)
    hist_len = len(histo_list) *1.0
    avg_list = [round(sum(x)/hist_len,2) for x in zip(*histo_list)]
    return avg_list
    
def classify(img):

    ausgang, eingang = img_cmp_crop(img)
    erg = "N"
    
    if eingang <= TH_EIN:
        erg = "E"
    elif ausgang <= TH_AUS:
        erg = "L"

    return ausgang, eingang, erg
    
def curl_post(date, ewert, awert, erg, img_path):
    cmd="""curl -i -X POST -H "Content-Type: multipart/form-data" -F "datum={0}" -F "eingangswert={2}" -F "ausgangswert={1}" -F "computer={3}" -F "event=@{4}" http://raspberry:9000/events/new/""".format(date,ewert,awert,erg,img_path)
    print(cmd)

def createdate(string):
    datetime_object = datetime.strptime(string.split("-")[0], '%Y%m%d%H%M%S')
    return  datetime_object.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    
    eingang = '/media/usbstick/motion/'
    
    for filename in os.listdir(eingang):
	if filename.endswith("jpg"):
          value = classify(eingang+filename)
          curl_post(createdate(filename),value[0],value[1],value[2],eingang+filename)
        
