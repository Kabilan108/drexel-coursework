function [ out ] = seq_findgene( dna )
    % Locate and transcribe the longest ORF in a DNA sequence

    % This function will take a string containing a single strand of DNA and returns
    % the amino acid sequence of the longest gene it finds within the DNA sequence.
    % A 'gene' is defined as a reading frame that starts with the AUG codon and ends
    % with a stop codon (UAA, UAG, or UGA).

    % Store the dna sequence and its complement
    dna = upper(dna);
    dna_comp = seq_transcribe(dna).noncoding;

    %% Translate each strand into amino acids
    % One protein will be translated for each possible reading frame (3 per strand)
    orfs = {};
    for i = 1:3
        orfs = [orfs, seq_transcribe(dna(i:end)).protein];
        orfs = [orfs, seq_transcribe(dna_comp(i:end)).protein];
    end

    %% Identify all genes in the orfs

    % Use regular expression to look for the start and stop codons
    I = ~cellfun('isempty', regexp(orfs, 'M\w*[*]'));

    % Get the valid genes
    valid_genes = orfs( I );

    % If no genes were found, return an empty string
    if isempty(valid_genes)
        out = '';
    else
        % Find the longest gene
        [~,I] = max(cellfun('length', valid_genes));
        out = valid_genes{I};
    end
end
