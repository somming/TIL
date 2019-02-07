from linked_list import *

if __name__ == "__main__":
	slist = Linked_list()
	print("데이터 갯수 : {}".format(slist.size()))
	show_list(slist)
	print()

	slist.append(3)
	slist.append(1)
	slist.append(5)
	slist.append(2)
	slist.append(10)
	slist.append(7)
	slist.append(2)

	print("데이터 갯수 : {}".format(slist.size()))
	show_list(slist)
	print()

	data1, pos1 = slist.search_target(2)
	if data1:
		print('searched data : {} at pos<{}>'.format(data1,pos1))
	else:
		print('there is no such data')

	data2, pos2 = slist.search_target(2,pos1+1)
	if data2:
		print('searched data : {} at pos<{}>'.format(data2,pos2))
	else:
		print('there is no such data')


	if slist.remove(2):
		print("데이터 갯수 : {}".format(slist.size()))
		show_list(slist)
		print()
	else:
		print("target Not found")

	if slist.remove(2):
		print("데이터 갯수 : {}".format(slist.size()))
		show_list(slist)
		print()
	else:
		print("target Not found")