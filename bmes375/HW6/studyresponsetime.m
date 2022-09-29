function studyresponsetime( dyfunction )


Y0 = zeros(9,1);%need to change for orpathway and xorpathway
Y0([2, 5, 7]) = 10;

checks = linspace(0.1, 5, 20);
responsetimes = zeros(size(checks));

for i = 1:length(checks)
    Y0([1, 4]) = checks(i);
    [T, Y] = ode23s(dyfunction, [0, 10], Y0); 
    pos = find(Y(:,9)>=8.0, 1, 'first'); %need to change for orpathway and xorpathway
    if isempty(pos); responsetimes(i) = nan;
		else             responsetimes(i) = T(pos); end
end

clf
plot(checks, responsetimes, 'b-')
xlabel('Input Concentration')
ylabel('Response Time')
ylim([0 10]);
hold on
plot([1, 1], ylim, 'k--')
plot([0, 5], [1, 1], 'k--')
hold off

