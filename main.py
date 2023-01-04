from Bio import SeqIO

# import pdb; pdb.set_trace()
start_Codon = "ATG"
stop_Codons = ["TAA", "TAG", "TGA"]


def get_orf_region(sequence):
    sequence = sequence.upper()
    print("The sequence is: " + sequence + ".")

    start_codon_sequence = find_start_codon(sequence)

    if start_codon_sequence == "None":
        print("There is not a start codon in this sequence: " + sequence + ".\n")
        return

    ORF_Region, rest_sequence = find_stop_codons(start_codon_sequence)


    if ORF_Region == "None":
        print("None of the three stop codons were found, so ORF region does not exist.\n")
        return
    print("Continue for the rest_sequence.")
    get_orf_region(rest_sequence)

def find_start_codon(sequence):
    for k in range(0, len(sequence), 1):
        # checking for the start codon in the sequence
        if start_Codon in sequence[k:k + 3]:
            start_codon_sequence = sequence[k:]
            print("Start codon %s found, the start_codon_sequence is: %s."
                  % (start_codon_sequence[:3], triplets(start_codon_sequence)))
            return start_codon_sequence
    return "None"


def find_stop_codons(start_codon_sequence):
    for k in range(0, len(start_codon_sequence), 3):
        # checking for any of the stop codons in the sequence
        if any(s in start_codon_sequence[k:k + 3] for s in stop_Codons):
            ORF_Region = start_codon_sequence[:k + 3]
            rest_sequence = start_codon_sequence[k + 3:]
            print("Stop codon %s found, the ORF_Region is: %s.\n" % (ORF_Region[-3:], triplets(ORF_Region)))
            return ORF_Region, rest_sequence
    return "None", "None"

def triplets(string):
    return ' '.join(string[i:i + 3] for i in range(0, len(string), 3))


def read_seq_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', '').split()


def read_fasta_file(filepath):
    list_fasta = list()
    for seq_record in SeqIO.parse(filepath, "fasta"):
        list_fasta.append(str(seq_record.seq))
    return list_fasta


def main():
    options = ["give your own sequence", "seq", "fasta"]
    user_option = ''
    input_message = "Pick an option with number 1-3:\n"

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item}\n'

    input_message += "Your choice: "

    while user_option not in map(str, range(1, len(options) + 1)):
        user_option = input(input_message)

    user_input = options[int(user_option) - 1]
    print("You selected: " + user_input)

    if user_input == "give your own sequence":
        # pdb.set_trace()
        sequence = input("\n\nEnter your own sequence: ")
        get_orf_region(sequence)

    elif user_input == "seq":
        # pdb.set_trace()
        filepath = input("\n\nEnter your seq filepath: ")
        list_of_sequences = read_seq_file(filepath)
        for sequence in list_of_sequences:
            get_orf_region(sequence)

    elif user_input == "fasta":
        filepath = input("\n\nEnter your fasta filepath: ")
        list_of_sequences = read_fasta_file(filepath)
        for sequence in list_of_sequences:
             get_orf_region(sequence)


if __name__ == "__main__":
    main()

