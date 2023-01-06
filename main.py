from Bio import SeqIO

start_Codon = "ATG"
stop_Codons = ["TAA", "TAG", "TGA"]


def get_orf_region(sequence, counter):
    sequence = sequence.upper()
    print("The sequence is: " + sequence + ".")
    if counter == 1:
        complementary_sequence(sequence)

    start_codon_sequence = find_start_codon(sequence)

    if start_codon_sequence == "None":
        print("There is not a start codon in this sequence: " + sequence + ".\n")
        return

    orf_region, rest_sequence = find_stop_codons(start_codon_sequence, counter)

    if orf_region == "None":
        print("None of the three stop codons were found, so orf region does not exist.\n")
        return
    elif len(rest_sequence) == 0:
        print("No rest_sequence.\n")
        return
    print("Continue for the rest_sequence.")
    counter += 1
    get_orf_region(rest_sequence, counter)


def find_start_codon(sequence):
    for k in range(0, len(sequence), 1):
        # checking for the start codon in the sequence
        if start_Codon in sequence[k:k + 3]:
            start_codon_sequence = sequence[k:]
            print("Start codon %s found, the start_codon_sequence is: %s."
                  % (start_codon_sequence[:3], triplets(start_codon_sequence)))
            return start_codon_sequence
    return "None"


def find_stop_codons(start_codon_sequence, counter):
    for k in range(0, len(start_codon_sequence), 3):
        # checking for any of the stop codons in the sequence
        if any(s in start_codon_sequence[k:k + 3] for s in stop_Codons):
            orf_region = start_codon_sequence[:k + 3]
            rest_sequence = start_codon_sequence[k + 3:]
            print("Stop codon %s found, the %s orf_region is: %s.\n" % (orf_region[-3:], counter, triplets(orf_region)))
            return orf_region, rest_sequence
    return "None", "None"


def triplets(string):
    return ' '.join(string[i:i + 3] for i in range(0, len(string), 3))


def complementary_sequence(sequence):
    sequence = sequence.replace("A", "t").replace(
        "C", "g").replace("T", "a").replace("G", "c")
    sequence = sequence.upper()
    print("The complementary sequence is: " + sequence + ".")
    print("The reversed-complementary sequence is: " + sequence[::-1] + ".")
    return sequence


def read_seq_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', '').split()


def read_fasta_file(filepath):
    list_fasta = list()
    for seq_record in SeqIO.parse(filepath, "fasta"):
        list_fasta.append(str(seq_record.seq))
    return list_fasta


def read_fastq_file(filepath):
    list_fastq = list()
    with open(filepath) as fp:
        while True:
            fp.readline()
            sequence = fp.readline()
            fp.readline()
            fp.readline()
            if len(sequence) == 0:
                break
            list_fastq.append(sequence)
    return list_fastq


def select_input():
    options = ["give your own sequence", ".seq", ".fasta", ".fastq"]
    user_option = ''
    input_message = "Pick an option with number 1-4:\n"

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item}\n'

    input_message += "Your choice: "

    while user_option not in map(str, range(1, len(options) + 1)):
        user_option = input(input_message)

    user_input = options[int(user_option) - 1]
    print("You selected: " + user_input)
    return user_input


def main():
    user_input = select_input()

    if user_input == "give your own sequence":
        sequence = input("\n\nEnter your own sequence: ")
        get_orf_region(sequence, 1)

    elif user_input == ".seq":
        filepath = input("\n\nEnter your .seq filepath: ")
        list_of_sequences = read_seq_file(filepath)
        for sequence in list_of_sequences:
            get_orf_region(sequence, 1)

    elif user_input == ".fasta":
        filepath = input("\n\nEnter your .fasta filepath: ")
        list_of_sequences = read_fasta_file(filepath)
        for sequence in list_of_sequences:
            get_orf_region(sequence, 1)

    elif user_input == ".fastq":
        filepath = input("\n\nEnter your .fastq filepath: ")
        list_of_sequences = read_fastq_file(filepath)
        for sequence in list_of_sequences:
            get_orf_region(sequence, 1)


if __name__ == "__main__":
    main()
