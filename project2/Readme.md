# CMPE 300 PROJECT 2 - MPI Programming

This is a MPI programming project which coded with python.

## Quick Explanation

In this project, we explore the use of the Message Passing Interface (MPI) for parallelizing the computation of bigrams and unigrams in a collection of sentences. MPI is a standardized and widely used library for writing parallel programs in C, C++, and Fortran, but it can also be used in Python through the mpi4py package.

The task of counting bigrams and unigrams in the document can be easily parallelized by dividing the input sentences among the available processes and having each process count the n-grams in its assigned portion. The results can then be gathered and combined by the main process to obtain the final counts. The program is supposed to work in a master slave/worker architecture. There will be P processes where the rank of the master process is zero and the ranks of the worker processes are positive.

## Usage

- In the command prompt/terminal write this code:

 ` mpiexec -n 5 python3 main.py --input_file data/sample_text.txt --merge_method MASTER --test_file data/test.txt  ` 

this will show requirement 2 of the project. The worker process should print its rank and the number of sentences it has received.Then, each worker will count the bigrams and unigrams in the sentences it received. This will be done by all the worker processes in parallel. Then, the bigram and unigram counts of the workers will be merged by summing the counts of the same bigrams and unigrams. The merge operation is the master process’s responsibility and will be done at the master process. 



- In the command prompt/terminal write this code:

 ` mpiexec -n 5 python main.py --input_file data/sample_text.txt --merge_method WORKERS  --test_file data/test.txt ` 

this will show requirement 3 of the project. Here we implement the data merging operation sequentially between the workers. Instead of passing the calculated data to the master node, each process will gather the data from the previous worker, merge that data with its own data, and pass it to the next worker. The last worker will in the end pass the final data to the master node. The argument value for this requirement will be “WORKERS” so the program will be called with “--merge_method WORKERS
