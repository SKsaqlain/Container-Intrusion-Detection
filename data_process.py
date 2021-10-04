import numpy as np 

# sys=open("systemcall.txt","r")
# sys_index=[ele.rstrip("\n") for ele in sys.readlines()]
def check_system_calls(filename):
	data_set=list()
	usc=list()#unique system  call
	file=open(filename,'r')
	for line in file:
		#print(len(line))
		if(len(line)<=1):
			continue
		#line=line.rstrip("\n")
		# if line not in d.keys():
			# d[line]+=1
		# else:
			# usc.append(line)
			# d[line]=0
		data_set.append(line.rstrip("\n"))
	return (data_set)


	
def write_into_file(filename,num_data):
	with open(filename,'w') as f:
		for vec in num_data:
			# print(vec)
			ele=','.join([str(item) for item in vec])
			# print(ele)
			f.write(ele+'\n')
		
		
def index_list(data_set):
	usc=set(data_set)#unique system call
	data_index=dict()
	data_index["uscc"]=len(usc)#unique systemcall count
	data_index["syscall"]=dict()
	i=0
	for x in usc:
		data_index["syscall"][x]=i
		i+=1
	return (usc,data_index)
	
def split_set(data_set,slength):
	set_sequence=list()
	# slength=10#sequence length
	for i in range(0,len(data_set),slength):
		subset=data_set[i:i+slength]
		set_sequence.append(subset)
	return set_sequence
	
def calculate_frequency(set_sequence,data_index):
	num_data=list()#numerical data_index
	for batches in set_sequence:
		l=[0]*data_index["uscc"]
		for systemcall in batches:
			l[data_index["syscall"][systemcall]]+=1
		num_data.append(l)
	return(num_data)

if(__name__=="__main__"):
	
	data_set=check_system_calls("trimmed_1.txt")
	usc,data_index=index_list(data_set)
	# print(usc,"\n")
	# print(data_index,"\n")
	slength=10
	set_sequence=split_set(data_set,slength)
	# for ele in set_sequence:
		# print(ele,"\n")
	num_data=calculate_frequency(set_sequence,data_index)
	# for ele in num_data:
		# print(ele)
	# print("\n")
	matrix=np.matrix(num_data)
	print(matrix)
	# print(num_data)
	write_into_file("num_data1.txt",num_data)