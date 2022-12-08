function [] = NoData(app)
% by Dao Lin 120722
% This function displays a message when the inputted gene has no relation to
% cancer

% Connect to database
dbfile = [bmes.tempdir '/disgenet_2020.sqlite'];
db = bmes_db(dbfile,'database');

% Create and execute SQLQuery to get the cancer associated with inputted
% gene
txt = sprintf('Select Disease from compare_table where geneName = "%s"', upper(app.GeneName.Value));
x = db.query(txt);

% If the inputted gene is not associated with cancer display a messeage
if x.Disease == "No Data"
    % Clear the plot
    cla(app.Plot);

    % Clear the table
    app.Table.Data = [];

    % Turn plot off and the label on
    app.Plot.Visible = 'off';
    app.Label.Visible = 'on';

    % Display the message
    app.Label.Text = sprintf('%s IS NOT ASSOCIATED WITH CANCER', upper(app.GeneName.Value));
end 