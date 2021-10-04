import numpy as np 

# sys=open("systemcall.txt","r")
# sys_index=[ele.rstrip("\n") for ele in sys.readlines()]
data_index=dict()
data_index["uscc"]=0#unique systemcall count
data_index["syscall"]=dict()
def check_system_calls(filename):
	data_set=list()
	time_set=list()
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
		t,s=line.rstrip("\n").split()
		data_set.append(s)
		if s not in usc:
			usc.append(s)
		time_set.append(t)
	return (data_set,time_set,usc)


	
def write_into_file(filename,num_data):
	with open(filename,'w') as f:
		for vec in num_data:
			# print(vec)
			ele=','.join([str(item) for item in vec])
			# print(ele)
			f.write(ele+'\n')
		
		
def index_list(data_set,usc):
	# usc=set(data_set)#unique system call
	global data_index
	# i=0
	for x in usc:
		if(x not in data_index["syscall"].keys()):
			data_index["syscall"][x]=data_index["uscc"]
			data_index["uscc"]+=1
		# i+=1
	return (data_index)
	
def split_set(data_set,time_set,slength):
	set_sequence=list()
	t=list()
	usc=list()
	
	# slength=10#sequence length
	for i in range(0,len(data_set),slength):
		subset=data_set[i:i+slength]
		try:
			t.append([time_set[i],time_set[i+slength-1]])
		except:
			t.append([time_set[i],time_set[-1]])
		set_sequence.append(subset)
	return (set_sequence,t)
	
def calculate_frequency(set_sequence,data_index):
	num_data=list()#numerical data_index
	for batches in set_sequence:
		l=[0]*data_index["uscc"]
		for systemcall in batches:
			l[data_index["syscall"][systemcall]]+=1
		num_data.append(l)
	return(num_data)
def helper(readfrom,writeinto,slength=50):
	
	data_set,time_set,usc=check_system_calls(readfrom)
	data_index=index_list(data_set,usc)
	# print(usc,"\n")
	# print(data_index,"\n")
	#slength=50
	set_sequence,dt=split_set(data_set,time_set,slength)
	# for i in range(len(set_sequence)):
		# print(set_sequence[i],dt[i],"\n")
	num_data=calculate_frequency(set_sequence,data_index)
	# for ele in num_data:
		# print(ele)
	# print("\n")
	matrix=np.matrix(num_data)
	# print(matrix)
	# print(num_data)
	write_into_file(writeinto,num_data)

if(__name__=="__main__"):
	
	slength=50
	data_index=dict()
	data_index["uscc"]=0#unique systemcall count
	data_index["syscall"]=dict()
	# helper("mapcalls_trimmed.txt","num_mapcalls.txt",slength)
	# helper("slapcalls_trimmed1.txt","num_slapcalls.txt",slength)
	data_set1,time_set1,usc1=check_system_calls("mapcalls_trimmed.txt")
	data_set2,time_set2,usc2=check_system_calls("slapcalls_trimmed1.txt")
	data_index=index_list(data_set1,usc1)
	data_index=index_list(data_set2,usc2)
	# print(usc,"\n")
	print(data_index,"\n")
	#slength=50
	set_sequence1,dt1=split_set(data_set1,time_set1,slength)
	set_sequence2,dt2=split_set(data_set2,time_set2,slength)
	# for i in range(len(set_sequence)):
		# print(set_sequence[i],dt[i],"\n")
	num_data1=calculate_frequency(set_sequence1,data_index)
	num_data2=calculate_frequency(set_sequence2,data_index)
	# for ele in num_data:
		# print(ele)
	# print("\n")
	# matrix=np.matrix(num_data)
	# print(matrix)
	# print(num_data)
	write_into_file("output1.txt",num_data1)
	write_into_file("output2.txt",num_data2)