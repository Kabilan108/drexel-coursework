function [] = diagram(app)
% by Henry Nguyen 120722
% This function creates the association tree diagram between cancers and genes

% Connect to database
dbfile = [bmes.tempdir '/disgenet_2020.sqlite'];
db = bmes_db(dbfile,'database');

% Create and execute SQL query to get the cancers associated with inputted
% gene
txt = sprintf('Select Disease from compare_table where geneName = "%s"', upper(app.GeneName.Value));
x = db.query(txt);

% Process the query output by removing unnecessary characters and splitting
% each cancer disease by comma
y = struct2array(x);
d = strsplit(y, '","');
c = regexprep(d, {'[' ,']' , '"'} , {''});

% Create empty digraph to input nodes and edges into
G = digraph();

% Get the number of cancers, C
[R,C] = size(c);

% Loop through each of the cancers and connect them to related genes 
for i = 1:C
    % Create and execute SQL query that selects the geneNames associated
    % with a specific cancer
    txt2 = sprintf('Select geneNames from compare_table2 where diseaseName = "%s"', c{i});
    z = db.query(txt2);

    % Process the query output by removing unnecessary characters and splitting
    % each cancer disease by comma
    p = struct2array(z);
    o = strsplit(p, '","');
    h = regexprep(o, {'[' ,']' , '"'} , {''});

    % Create the edges and nodes for the tree diagram 
    G = addedge(G,c{i},h);
end

% If gene and cancer association is found follow through with if statement
if x.Disease ~= "No Data"
    % Display cancers in table
    app.Table.Data = c';

    % Plot the tree diagrams using the nodes and edges
    plot(app.Plot,G,'Layout','force');

    % Turn plot on and label off
    app.Plot.Visible = 'on';
    app.Label.Visible = 'off';

    % Change title of plot to include the patient name and the gene that
    % they have
    app.Plot.Title.String = sprintf("%s's Cancer Association With Gene: %s", app.FirstName.Value, upper(app.GeneName.Value));
end
