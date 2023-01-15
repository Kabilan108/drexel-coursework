function [ out ] = seq_transcribe( dna )
    % Transcribe DNA to mRNA
    %
    % This function takes a string containing the coding DNA strand (5' -> 3')
    % and returns the noncoding strand (5' -> 3'), transcribed mRNA sequence (5' -> 3')
    % and the protein sequence.
    %
    % Author: TKO

    % One option is using the built-in `geneticcode` function to map the codons
    gen_code = geneticcode(1);
    % This object can be indexed thus: gen_code.(codon) to get the amino acid

    % The other option is to create a custom map object
    codons = {
        'TTT', 'TCT', 'TAT', 'TGT', 'TTC', 'TCC', 'TAC', 'TGC', 'TTA', 'TCA', 'TAA',...
        'TGA', 'TTG', 'TCG', 'TAG', 'TGG', 'CTT', 'CCT', 'CAT', 'CGT', 'CTC', 'CCC',... 
        'CAC', 'CGC', 'CTA', 'CCA', 'CAA', 'CGA', 'CTG', 'CCG', 'CAG', 'CGG', 'ATT',... 
        'ACT', 'AAT', 'AGT', 'ATC', 'ACC', 'AAC', 'AGC', 'ATA', 'ACA', 'AAA', 'AGA',... 
        'ATG', 'ACG', 'AAG', 'AGG', 'GTT', 'GCT', 'GAT', 'GGT', 'GTC', 'GCC', 'GAC',... 
        'GGC', 'GTA', 'GCA', 'GAA', 'GGA', 'GTG', 'GCG', 'GAG', 'GGG'
    };
    proteins = {
        'F', 'S', 'Y', 'C', 'F', 'S', 'Y', 'C', 'L', 'S', '*', '*', 'L', 'S', '*', ...
        'W', 'L', 'P', 'H', 'R', 'L', 'P', 'H', 'R', 'L', 'P', 'Q', 'R', 'L', 'P', ...
        'Q', 'R', 'I', 'T', 'N', 'S', 'I', 'T', 'N', 'S', 'I', 'T', 'K', 'R', 'M', ...
        'T', 'K', 'R', 'V', 'A', 'D', 'G', 'V', 'A', 'D', 'G', 'V', 'A', 'E', 'G', ...
        'V', 'A', 'E', 'G'
    };
    gen_code = containers.Map(codons, proteins);
    % This object can be indexed thus: gen_code(codon) to get the amino acid

    %% Determine the Noncoding Strand

    % The noncoding strand is the reverse complement of the coding strand
    % We'll use another map object to map the nucleotides to their complements
    complement = containers.Map({'A', 'T', 'C', 'G'}, {'T', 'A', 'G', 'C'});

    % We'll use a for loop to iterate over the nucleotides in the coding strand
    % and add the complement to the noncoding strand
    noncoding = '';
    for i = 1:length(dna)
        % Joining the nucleotids this way will reverse the order
        noncoding = [complement(dna(i)), noncoding];
    end

    %% Get the mRNA Sequence

    % The mRNA sequence is the coding strand with T replaced with U
    mRNA = strrep(dna, 'T', 'U');

    %% Transcribe the Coding Strand to mRNA

    protein = '';
    for i = 1:3:length(dna)
        % Make sure this is a valid codon
        if i + 2 > length(dna)
            break
        end

        % Get the codon
        codon = dna(i:i+2);

        % Get the amino acid
        aa = gen_code(codon);

        % Add the amino acid to the protein sequence
        protein = [protein, aa];
    end

    % Create output struct
    out = struct('noncoding', noncoding, 'mRNA', mRNA, 'protein', protein);
end
