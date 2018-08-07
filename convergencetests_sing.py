import math
import numpy as np

def tokenval(fname, token):
	file_in = open(fname, 'r')
	lines = file_in.readlines()
	file_in.close()
	found = 0
	for line in lines:
		if (token in line):
			strnext = line.split(token)[1]
			val = strnext.split()[0]
			valf = float(val)
			found = 1
			break

	if (found == 0):
		print "could not find token : ", token , " in file : ", fname
	return valf



def findconstants(filelist):
	hlist = []
	errlist = []
	constants = []
	timelist = []
	nvertices = []

	for fname in  filelist:

		token = 'Assembling A took : '
		time_tot = tokenval(fname, token)
		token = 'Assembling b took : '
		time_tot = time_tot + tokenval(fname, token)
		token = 'Applying BCs took : '
		time_tot = time_tot + tokenval(fname, token)
		token = 'Solving took : '
		time_tot = time_tot + tokenval(fname, token)
		token = 'Total number of vertices :'
		vertices = tokenval(fname, token)
		token = 'hmin : '
		val_hmin = tokenval(fname, token)
		token = 'hmax : '
		val_hmax = tokenval(fname, token)
		if val_hmin <> val_hmax :
			print "non uniform mesh used for checking convergence for log : ", fname

		token = '0.49) : '
		val_err = tokenval(fname, token)

		nvertices.append(vertices)
		timelist.append(time_tot)
		hlist.append(val_hmin)
		errlist.append(val_err)
		


	for i in range(len(hlist)-1):
		constants.append(math.fabs(math.log( errlist[i+1] / errlist[i]  ) / math.log(hlist[i+1] / hlist[i] )) )


	return hlist, errlist, constants, timelist, nvertices


if __name__ == '__main__':

	#2D 1 process tests

	file = open("convergence_test_details.txt","w")

	hlist, errlist, constants_2D_1, timelist_2D_1, nvertices_2D_1 = findconstants(['log_convergence_2D_numprocs_1_lvl_1', 'log_convergence_2D_numprocs_1_lvl_2', 'log_convergence_2D_numprocs_1_lvl_3', 'log_convergence_2D_numprocs_1_lvl_4', 'log_convergence_2D_numprocs_1_lvl_5'])
	if ( np.mean(np.asarray(constants_2D_1))  > 1.99):
		print "2D 1 prcess test : PASSED"
	else:
		print "2D 1 prcess test : FAILED"

	file.write('#2D mesh 1 process case :\n')
	file.write('#mesh sizes :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, hlist))) 
	file.write('\n')
	file.write('#number of vertices :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, nvertices_2D_1)))
	file.write('\n')
	file.write('#errors     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, errlist)))
	file.write('\n')
	file.write('#ln(e-1 / e) / ln(h-1 / h)     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, constants_2D_1)))
	file.write('\n')
	file.write('#Total time to assemble and solve     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, timelist_2D_1)))
	file.write('\n')





	#2D 5 process tests

	hlist, errlist, constants_2D_5, timelist_2D_5, nvertices_2D_5 = findconstants(['log_convergence_2D_numprocs_5_lvl_1', 'log_convergence_2D_numprocs_5_lvl_2', 'log_convergence_2D_numprocs_5_lvl_3', 'log_convergence_2D_numprocs_5_lvl_4', 'log_convergence_2D_numprocs_5_lvl_5'])
	if ( np.mean(np.asarray(constants_2D_5)) > 1.99):
		print "2D 5 prcess test : PASSED"
	else:
		print "2D 5 prcess test : FAILED"

	#compute strong scaling efficiency for each level

	strong_scal = []
	strong_scal = np.divide(timelist_2D_1, timelist_2D_5)
	strong_scal = np.divide(strong_scal, 5)

	file.write('#2D mesh 5 process case :\n')
	file.write('#mesh sizes :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, hlist)))
	file.write('\n')
	file.write('#number of vertices :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, nvertices_2D_5)))
	file.write('\n')
	file.write('#errors     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, errlist)))
	file.write('\n')
	file.write('#ln(e-1 / e) / ln(h-1 / h)     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, constants_2D_5)))
	file.write('\n')
	file.write('#Total time to assemble and solve     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, timelist_2D_5)))
	file.write('\n')







	#3D different num process tests
	hlist, errlist, constants_3D_5, timelist_3D_5, nvertices_3D_5 = findconstants(['log_convergence_3D_numprocs_1_lvl_1', 'log_convergence_3D_numprocs_2_lvl_2', 'log_convergence_3D_numprocs_4_lvl_3', 'log_convergence_3D_numprocs_8_lvl_4', 'log_convergence_3D_numprocs_7_lvl_5'])
	if ( np.mean(np.asarray(constants_3D_5)) > 1.99):
		print "3D diff prcess test : PASSED"
	else:
		print "3D diff prcess test : FAILED"
	
	weak_scal = np.divide(timelist_3D_5, timelist_3D_5[0])
	
	
	#print constants_3D_5
	file.write('#3D mesh case :\n')
	file.write('#mesh sizes :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, hlist)))
	file.write('\n')
	file.write('#number of vertices :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, nvertices_3D_5)))
	file.write('\n')
	file.write('#errors     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, errlist)))
	file.write('\n')
	file.write('#ln(e-1 / e) / ln(h-1 / h)     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, constants_3D_5)))
	file.write('\n')
	file.write('#Total time to assemble and solve     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, timelist_3D_5)))
	file.write('\n')
	file.write('#Weak Scaling efficiencies     :\n')
	file.write('#----------------------\n')
	file.write('\n'.join(map(str, weak_scal)))
	file.write('\n')
        file.write('#Strong scaling efficiencies     :\n')
        file.write('#----------------------\n')
        file.write('\n'.join(map(str, strong_scal)))
        file.write('\n')


	file.close();

