#!/usr/bin/python
#coding=utf-8

import sys
import time

def cost_cpu(cost_percent, duration):
	begin = time.time()
	last = begin
	i = 0

	if cost_percent > 1 or cost_percent <= 0:
		print("Error:  cost percent should <= 1 and > 0")
		print_usage()
		return

	while True:
		if time.time() - last > 0.01:
			time.sleep( 0.01 * (1 - cost_percent) / cost_percent )
			last = time.time()

		i = i + 1
		j = i*i - i*5 + 1 
		i = j % 10000 + 1

		if time.time() - begin > duration:
			break

def cost_mem(rate, maximum):
	cache = []
	size = int(rate*1024*1024)
	stop_len = maximum*1024/rate
	
	while True:
		cache.append('x'*size)
		time.sleep(1)
		if len(cache) > stop_len :
			break


def print_usage():
	print('''
	cmcost tool usage :
			
		1 : python cmcost.py -c cost_percent duration
		
				e.g python cmcost.py -c 0.8 30        # 消耗单 cpu 80% 资源，持续 30 秒
		
		2 : python cmcost -m rate maximum 

				e,g python cmcost.py -m 0.1 10        # 内存以 0.1 m/s 的速率增长，最大不超过 10 G
			''')
	


if __name__ == '__main__':
	print(len(sys.argv))
	print(sys.argv)
	if len(sys.argv) == 4:
		if sys.argv[1] == '-c':
			cost_cpu(sys.argv[2], sys.argv[3])
		elif sys.argv[1] == '-m':
			cost_mem(float(sys.argv[2]), int(sys.argv[3]))

		sys.exit()

	print_usage()
