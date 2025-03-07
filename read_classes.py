# -*- coding: UTF-8 -*-
"""
 This program is used to read the classes data in Excel-xlsx
    Copyright (C) 2025  ShengYan Cheng

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# PROJECT_NAME Python_projects
# PRODUCT_NAME PyCharm
# NAME read_classes
# AUTHOR Pfolg
# TIME 2025/3/6 14:19

import random

import pandas as pd


class ReadTable:
    def __init__(self, xlsx, timetable):
        self.colors = [
            # 红色系
            "#FF2400", "#8B0000", "#FF6F61", "#800000",
            # 橙色系
            "#FFA500", "#FF8C00", "#FF7F50", "#FF6347",
            # 黄色系
            "#FFD700", "#FFF44F", "#FFDB58", "#CC7722",
            # 绿色系
            "#228B22", "#32CD32", "#98FF98", "#008080",
            # 蓝色系
            "#000080", "#87CEEB", "#1E90FF", "#4682B4",
            # 紫色系
            "#4B0082", "#8A2BE2", "#DA70D6", "#9400D3",
            # 粉色系
            "#FF1493", "#FF69B4", "#FFB6C1", "#FF007F",
            # 棕色系
            "#D2691E", "#6F4E37", "#8B4513",
            # 白色
            "#ffffff"
        ]
        self.timetable = {}
        with open(timetable, "r", encoding="utf-8") as f:
            txt = f.readlines()
        for line in txt:
            if "#" in line:
                continue
            elif line:
                a, b = line.split("/")
                self.timetable[a] = b

        self.table = pd.read_excel(xlsx, header=None, )
        # print(self.table)
        # print(len(self.table.columns))
        # print(self.table.iloc[:, 0])

    # 添加颜色
    def addColor(self):
        data = self.getData()
        new_data = []
        color_data = {}
        for i in data:
            if i.get("text") and i.get("text") in list(color_data.keys()):
                continue
            elif i.get("text"):
                length = len(self.colors)
                c = self.colors[random.randint(0, length - 1)]
                self.colors.remove(c)
                color_data[i.get("text")] = c

        for i in data:
            i["background_color"] = color_data.get(i.get("text"))
            new_data.append(i)
        return new_data

    # 处理数据
    def getData(self):
        data = []
        for i in range(len(self.table.columns)):
            x = self.table.iloc[:, i]
            y = {}
            for j in range(len(x)):
                if j == 0:
                    y["text"] = x[0]
                if j == 1:
                    y["description"] = x[1]
                if j == 2:
                    y["week"] = (x[2].replace("：", "-").replace(":", "-").replace("周", "-")).split("-")[2:4]
                    a, b = y.get("week")
                    y["repeat"] = True
                    y["repeat_number"] = eval(b) - eval(a) + 1
                    y["repeat_space"] = 7
                if j == 3:
                    y["description"] = y.get("description") + "；" + x[3]
                if j == 4:
                    a, b = x[4].split("-")
                    y["time_start"] = self.timetable.get(a).split("-")[0]
                    y["time_end"] = (self.timetable.get(b).split("-")[1]).strip()
                if j == 5:
                    y["weekday"] = x[5]
                if j == 6:
                    y["description"] = y.get("description") + "；" + x[6]
                if j == len(x) - 1:
                    data.append(y)
        return data


if __name__ == '__main__':
    # 结果测试
    # print(ReadTable("assets/sample.xlsx", "assets/timeline.txt").addColor()
    pass
