#Student Name: YİĞİT SARIOĞLU
#Student Number: 2022400354
#Compile Status: Compiling
#Program Status: Working
#Notes: Anything you want to say about your code that will be helpful in the grading process.


#Imports the necessary modules for parsing command line arguments
import argparse

#Imports the necessary modules for parallel processing with MPI.
from mpi4py import MPI


# Create an ArgumentParser object and add three required arguments: input_file, merge_method, and test_file. 
# These arguments will be used later in the program to specify the input data, the method for merging the data, and the file to test the results on.
parser = argparse.ArgumentParser()
parser.add_argument("--input_file", type=str, required=True)
parser.add_argument("--merge_method", type=str, required=True)
parser.add_argument("--test_file", type=str, required=True)
    
# get it
args = parser.parse_args()
# Read the input file from the command line arguments
input_file = args.input_file

# Read the test file from the command line arguments
test_file = args.test_file

# Read the merge method from the command line arguments
merge_method = args.merge_method


# Initialize the MPI environment
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.rank

# Get the total number of processes
num_procs = comm.size

# bigram_data and unigram_data are dictionaries containing the bigram and unigram counts for each worker process
bigram_data = {}
unigram_data = {}


# bigram_counts and unigram_counts are dictionaries containing the bigram and unigram counts for each worker process
bigram_counts ={}
unigram_counts = {}


# Dictionary to store the conditional probabilities of the bigrams
probs = {}





# The master process is responsible for reading and distributing the input data evenly
# to the worker processes.
if rank == 0:
    # Read the input file and split it into sentences
    with open(input_file, "r") as f:
        sentences = f.read().split("\n")


    # Distribute the sentences evenly to the worker processes
    sentence_lists = []
    for i in range(num_procs):
        sentence_lists.append([])

    for i in range(len(sentences)):
        sentence_lists[i % (num_procs-1)].append(sentences[i])

    for i in range(num_procs-1):
        comm.send(sentence_lists[i], dest = i+1)


    
else:
    # The worker processes receive the sentences from the master process
    sentences = comm.recv(source=0)

    # The worker processes prints number of received sentences
    print("Process {} has received {} sentences".format(rank, len(sentences)))
  
    

    if merge_method=="MASTER" :
            
         for sentence in sentences:
            # Split the sentence into words
            words = sentence.split(" ")
            

            # Count the frequencies of the bigrams and unigrams in the sentence
            for i in range(len(words)-1 ):
                bigram = (words[i], words[i+1]) 
                
                bigram_data[bigram] = bigram_data.get(bigram, 0) + 1

                unigram = words[i]
                bigram_data[unigram] = bigram_data.get(unigram, 0) + 1

            
         comm.send(bigram_data, dest=0) 


    elif merge_method == "WORKERS":    
        

        for sentence in sentences:
            # Split the sentence into words
            words = sentence.split(" ")
            

            # Count the frequencies of the bigrams and unigrams in the sentence
            for i in range(len(words)-1 ):
                bigram = (words[i], words[i+1]) 
                bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1

                unigram = words[i]
                unigram_counts[unigram] = unigram_counts.get(unigram, 0) + 1
            
        
        

        # Gather the bigram and unigram counts from the previous worker (if any)
        if rank > 1:
            prev_bigram_counts = comm.recv(source=rank-1)
            prev_unigram_counts = comm.recv(source=rank-1)

            # Merge the data from the previous worker with our own data
            for bigram, count in prev_bigram_counts.items():
                if bigram not in bigram_counts:
                   bigram_counts[bigram] = 0
                bigram_counts[bigram] += count

            for unigram, count in prev_unigram_counts.items():
                if unigram not in unigram_counts:
                    unigram_counts[unigram] = 0
                unigram_counts[unigram] += count

        # Pass our data to the next worker (if any)
        if rank < num_procs -1:

            comm.send(bigram_counts, dest=rank+1)
            comm.send(unigram_counts, dest=rank+1) 

        # If we are the last worker, the final data is in our bigram_counts and unigram_counts dictionaries
        if rank == num_procs-1:
        # Use the merged data to calculate the conditional probabilities of the bigrams in the test data
            comm.send(bigram_counts, dest=0)
            comm.send(unigram_counts, dest=0) 
            





# Master Process merges data from workers and calculates conditional probability
if merge_method=="MASTER" :
    if rank == 0:
    
    # Receive the bigram data from the worker processes
        for i in range(1, num_procs):
            received_data = comm.recv(source=i)
        
            # Merge the received data with the existing data
            for key, value in received_data.items():
                bigram_data[key] = bigram_data.get(key, 0) + value
                

        
        # Read the test file and split it into sentences
        with open(test_file, "r") as f:
            test_sentences = f.read().split("\n")

        # Compute the number of sentences
        number_of_sentences = len(test_sentences) 

        
        for test_sentence in test_sentences:
            # Split the sentence into words
            words = test_sentence.split(" ")
            
             # Count the frequencies of the first word in the bigram_data dictionary   
            freq_of_first_word =  bigram_data.get(words[0]) or 0
            
            # Count the frequencies of the both word(bigram) in the bigram_data dictionary 
            freq_of_both = bigram_data.get( (words[0], words[1]) ) or 0
           

            if freq_of_first_word > 0 :
                #Calculate the conditional probability
                probs[test_sentence] = freq_of_both / freq_of_first_word 
                
            else:
                probs[test_sentence] = 0

            # Prints conditional probability of test sentence
            print ("(MASTER METHOD) Conditional probability of {} is {}  " .format(test_sentence , probs[test_sentence]  )  )

        



# If merging method WORKERS is selected, conditional probabilities are calculated accordingly.
elif merge_method=="WORKERS" :

    if rank == 0:
        bigram_counts = comm.recv(source=num_procs-1)
        unigram_counts = comm.recv(source=num_procs-1)


         # Read the test file(test.txt) and split it into sentences
        with open(test_file, "r") as f:
            test_sentences = f.read().split("\n")

        
        for test_sentence in test_sentences:
            # Split the sentence into words
            words = test_sentence.split(" ")
            
        
            # Count the frequencies of the first word in the unigram_counts dictionary   
            freq_of_first_word =  unigram_counts.get(words[0]) or 0
            
            # Count the frequencies of the bigram  in the bigram_counts dictionary 
            freq_of_both = bigram_counts.get( (words[0], words[1]) ) or 0
           

            if freq_of_first_word > 0 :
                #Calculates the conditional probability
                probs[test_sentence] =  freq_of_both / freq_of_first_word 
            else:
                probs[test_sentence] = 0

            #Prints the conditional probability of test sentence
            print ("(WORKER METHOD) Conditional probability of {} is {}  " .format(test_sentence , probs[test_sentence]  )  )


# If the merging method is written incorrectly, this is handled.    
else :
    
    if rank == 0:
        print("Choose a valid merge method: MASTER or WORKERS") 