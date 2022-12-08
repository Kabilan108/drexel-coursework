function  [risk, diameter] = molesize_export(file)

[risk,diameter]=molesize(file);
outfile=[file '.out'];
f = fopen(outfile,'W');
fprintf(f, '%f\n%s\n',diameter,risk);
fclose(f);


