%% Set up PATH
% If this is a PC, add cygwin program folder to PATH, so we can run them
% using system().

if ispc
    s = getenv('PATH');
    CYGWIN='C:/cygwin/bin';
    if isempty(strfind(s,CYGWIN))
        setenv('PATH',[s ';' CYGWIN]);
    end
end

%% compile & test multiconvert...
system('g++ -o multiconvert.exe multiconvert.cc');
system('multiconvert.exe f 20');

