%Jess Baggett 
%takes the password from login.mlapp and encrypts it
function d = encrypt(password)
%need to put password in a file since md5 only takes file inputs
    f=fopen('password.txt','w');
    %add password to file
    fprintf(f, password);
    %encrypt the password
    d=md5('password.txt');
    fclose('all');
    %delete password file once finished
    delete('password.txt');
end