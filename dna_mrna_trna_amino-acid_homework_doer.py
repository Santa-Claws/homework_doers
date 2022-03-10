from typing import List


def letter_exchanger(letter_list: List[str]) -> List[str]:
    new_letter_list = []
    for i in letter_list:
        if i == 'a':
            new_letter_list.append('u')
        elif i == 'c':
            new_letter_list.append('g')
        elif i == 'g':
            new_letter_list.append('c')
        elif i == 't':
            new_letter_list.append('a')
        elif i == 'u':
            new_letter_list.append('a')
        elif i == 'a':
            new_letter_list.append('t')
    return new_letter_list


def user_of_letter_exchanger(l=[]):
    if l:
        letter_exchanger_output = letter_exchanger(l)
    else:
        q_input = input('whats the code')
        letter_exchanger_output = letter_exchanger(list(q_input))
    return letter_exchanger_output


def amino_acid_converter(trna_list):
    amino_acid = []
    amino_acid_dict = {'aaa': 'phe', 'aac': 'leu', 'aag': 'phe', 'aau': 'leu', 'aca': 'cys', 'acc': 'trp', 'acg': 'cys',
                       'acu': 'scp', 'aga': 'ser', 'agc': 'ser', 'agg': 'ser', 'agu': 'ser', 'aua': 'tyr', 'auc': 'spc',
                       'aug': 'tyr', 'auu': 'spc', 'caa': 'val', 'cac': 'val', 'cag': 'val', 'cau': 'val', 'cca': 'gly',
                       'ccc': 'gly', 'ccg': 'gly', 'ccu': 'gly', 'cga': 'Ala', 'cgc': 'ala', 'cgg': 'ala', 'cgu': 'ala',
                       'cua': 'asp', 'cuc': 'glu', 'cug': 'asp', 'cuu': 'glu', 'gaa': 'leu', 'gac': 'leu', 'gag': 'leu',
                       'gau': 'leu', 'gca': 'arg', 'gcc': 'arg', 'gcg': 'arg', 'gcu': 'arg', 'gga': 'pro', 'ggc': 'pro',
                       'ggg': 'pro', 'ggu': 'pro', 'gua': 'his', 'guc': 'glu', 'gug': 'his', 'guu': 'glu', 'uaa': 'iso',
                       'uac': 'met', 'uag': 'iso', 'uau': 'iso', 'uca': 'ser', 'ucc': 'arg', 'ucg': 'ser', 'ucu': 'arg',
                       'uga': 'thr', 'ugc': 'thr', 'ugg': 'thr', 'ugu': 'thr', 'uua': 'asn', 'uuc': 'lys', 'uug': 'asn',
                       'uuu': 'lys'}
    if len(trna_list) % 3 != 0:
        print('ERROR\n :trna list not in threes')
        exit(1)
    for i in range(0, len(trna_list), 3):
        key = trna_list[i:i+3]
        key_string = ''.join(key)
        amino_acid.append(amino_acid_dict[key_string])
    return amino_acid


print('this is a dna and mrna and trna converter for gits use')
n_input = input('what do you want to convert')

if n_input == 'mrna':
    abcftuykjftyfdtyjdtgdrtdrth = user_of_letter_exchanger()
    print(abcftuykjftyfdtyjdtgdrtdrth)
elif n_input == 'trna':
    mrna_letter_list = user_of_letter_exchanger([])
    new_trna_letter_list = user_of_letter_exchanger(mrna_letter_list)
    print(new_trna_letter_list)
    print('(below is the amino acid)')
    amino_acid_list = amino_acid_converter(new_trna_letter_list)
    print(amino_acid_list)
else:
    print('ERROR')
