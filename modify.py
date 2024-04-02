import re

def parse_gaf_to_tsv(input_file, output_file):
    # Regular expressions to find FBgn numbers and GO terms
    fbgn_pattern = re.compile(r'FBgn\d+')
    go_pattern = re.compile(r'GO:\d+')

    # Dictionary to store FBgn numbers and associated GO terms
    gene_go_dict = {}

    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('!'):
                continue  # Skipping header lines
            fbgn_match = fbgn_pattern.search(line)
            go_matches = go_pattern.findall(line)
            if fbgn_match and go_matches:
                fbgn = fbgn_match.group(0)
                gene_go_dict.setdefault(fbgn, set()).update(go_matches)

    # Writing to TSV file
    with open(output_file, 'w') as file:
        for fbgn, go_terms in gene_go_dict.items():
            file.write(f'{fbgn}\t{";".join(sorted(go_terms))}\n')

# Example usage
parse_gaf_to_tsv('fb.gaf', 'fb.tsv')
