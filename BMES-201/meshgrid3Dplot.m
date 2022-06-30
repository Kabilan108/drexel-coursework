x = [0:.1:5];
y = [0:.1:5];
[x,y] = meshgrid(x,y);
z = x .* sin( x + 2*y );
plot3(x(:),y(:),z(:))
figure % creates new figure instead of overwritim=ng the first
surf(x,y,z)