# -*- coding: UTF-8 -*-
"""
 This program is used to show classes in the app
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
# NAME CurriculumUI
# AUTHOR Pfolg
# TIME 2025/3/6 17:28

from PyQt6 import uic
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView


class CurriculumUI(QWidget):
    def __init__(self, ui_file, parent=None):
        super().__init__(parent)
        ui_main = uic.loadUi(ui_file, self)
        self.tableWidget: QTableWidget = ui_main.tableWidget
        self.tableWidget.setAlternatingRowColors(True)  # 斑马线
        self.tableWidget.resizeColumnsToContents()  # 设置列宽随内容改变
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # 最后一列填满表格
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 设置编辑模式=不可编辑

    def setTable(self, data: list, column=None, header=None, ):
        if header is None:
            header = ["课程", "开始", "结束", "教学周", "信息"]
        if column is None:
            column = 5
        weekday_ch = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "日"}
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(column)
        self.tableWidget.setHorizontalHeaderLabels(header)

        for i in range(len(data)):
            c = data[i].get("background_color")
            for j in range(column):
                if j == 0:
                    __weekday__ = weekday_ch.get(data[i].get("weekday"))
                    x = QTableWidgetItem(data[i].get("text"))
                    x.setToolTip(data[i].get("description") + "；星期" + __weekday__)
                    if c:
                        x.setBackground(QBrush(QColor(c)))
                    self.tableWidget.setItem(i, j, x)
                elif j == 1:
                    x = QTableWidgetItem(data[i].get("time_start"))
                    if c:
                        x.setBackground(QBrush(QColor(c)))
                    self.tableWidget.setItem(i, j, x)
                elif j == 2:
                    x = QTableWidgetItem(data[i].get("time_end"))
                    if c:
                        x.setBackground(QBrush(QColor(c)))
                    self.tableWidget.setItem(i, j, x)
                elif j == 3:
                    a, b = data[i].get("week")
                    x = QTableWidgetItem("{}-{}".format(a, b))
                    if c:
                        x.setBackground(QBrush(QColor(c)))
                    self.tableWidget.setItem(i, j, x)
                elif j == 4:
                    __weekday__ = weekday_ch.get(data[i].get("weekday"))

                    x = QTableWidgetItem(data[i].get("description") + "；星期" + __weekday__)
                    if c:
                        x.setBackground(QBrush(QColor(c)))
                    self.tableWidget.setItem(i, j, x)
