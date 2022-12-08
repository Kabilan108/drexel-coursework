%created by hailee mayer
%the purpose of this function is the get the request from the log
%submission and stores the data in the proper fields of the SQL database
%(symdb). The script should confirm to the user if the entry of the data is
%successful or if there is an error. 



%=======new table=====
CREATE TABLE symptoms (
    id         INTEGER      PRIMARY KEY,
    username     VARCHAR (50),
    year       INTEGER,
    month      INTEGER,
    day        INTEGER,
    abpain     INTEGER,
    recpain    INTEGER,
    backpain   INTEGER,
    bodyache   INTEGER,
    headache   INTEGER,
    stooltype  INTEGER,
    stoolcolor INTEGER,
    stoolpain  INTEGER,
    bai1       INTEGER,
    bai2       INTEGER,
    bai3       INTEGER,
    bai4       INTEGER,
    bai5       INTEGER,
    bai6       INTEGER,
    bai7       INTEGER,
    bai8       INTEGER,
    bai9       INTEGER,
    bai10      INTEGER,
    bai11      INTEGER,
    bai12      INTEGER,
    bai13      INTEGER,
    bai14      INTEGER,
    bai15      INTEGER,
    bai16      INTEGER,
    bai17      INTEGER,
    bai18      INTEGER,
    bai19      INTEGER,
    bai20      INTEGER,
    bai21      INTEGER,
    otherpain  VARCHAR (50),
    othersymp  VARCHAR (50),
    notes      VARCHAR (50) 
);
