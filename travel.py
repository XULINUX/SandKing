#!/usr/bin/env python3 
#-*- coding:utf-8 -*-
#Date：2018-07-17
#Author: RUIXU
print("遇见你是最美丽的意外！")
import this
while True:
	salary = input("请输入你的月薪: 输入q或Q退出：")
	if salary == 'q' or salary == 'Q':
		break
	try:
		a = int(salary)
	except:
		print("请输入一个数字")
	else:
		if a >= 50000:
			print("欧洲高端游等着你")
		elif 30000 <= a < 50000:
			print("欧洲低端旅游考虑一下")
		elif 15000 <= a < 30000:
			print("东南亚旅游新马泰了解一下")
		elif 8000 <= a < 15000:
			print("国内任你游")
		elif 4000 <= a < 8000:
			print("只能选择省内游了！")
		elif 2000 <= a < 4000:
			print("只能选择郊游！")
		elif 500 <= a < 2000:
			print("只能选择花生油！")
		elif 0 < a < 500:
			print("请选择地沟油！")
		else:
			print("请选择梦游！梦里啥都有！！！")
		
	


