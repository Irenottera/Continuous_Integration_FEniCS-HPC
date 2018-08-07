#2D 1 process

mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_1.bin  > log_convergence_2D_numprocs_1_lvl_1
mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_2.bin  > log_convergence_2D_numprocs_1_lvl_2
mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_3.bin  > log_convergence_2D_numprocs_1_lvl_3
mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_4.bin  > log_convergence_2D_numprocs_1_lvl_4
mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_5.bin  > log_convergence_2D_numprocs_1_lvl_5

#2D 5 processes
mpirun -n 5 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_1.bin  > log_convergence_2D_numprocs_5_lvl_1
mpirun -n 5 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_2.bin  > log_convergence_2D_numprocs_5_lvl_2
mpirun -n 5 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_3.bin  > log_convergence_2D_numprocs_5_lvl_3
mpirun -n 5 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_4.bin  > log_convergence_2D_numprocs_5_lvl_4
mpirun -n 5 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/square_level_5.bin  > log_convergence_2D_numprocs_5_lvl_5


#3D different num processes
mpirun -n 1 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/cube_level_1.bin  > log_convergence_3D_numprocs_1_lvl_1
mpirun -n 2 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/cube_level_2.bin  > log_convergence_3D_numprocs_2_lvl_2
mpirun -n 4 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/cube_level_3.bin  > log_convergence_3D_numprocs_4_lvl_3
mpirun -n 8 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/cube_level_4.bin  > log_convergence_3D_numprocs_8_lvl_4
mpirun -n 7 singularity exec -B $FENIXDIR:/home --pwd /home/poisson_convergence ../../build-fenics.simg ./demo meshes/cube_level_5.bin  > log_convergence_3D_numprocs_7_lvl_5

