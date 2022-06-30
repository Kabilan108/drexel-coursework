x = 1:4; y = 1:4;
[x,y] = meshgrid(x,y);
I = ((x.^2) + y) == (3*x);
combs = [x(I),y(I)]