function [winratio]=hwbayes_montyhall_template(strategy,trials)
% by Author (write your name).
% See http://en.wikipedia.org/wiki/Monty_Hall_problem for a description of the
% problem.
% In this function, you need to simulate the game for "trials" many times
% and return the ratio of the times the player wins under the given strategy.
% "strategy" is one of 0,1,2 with the following meaning:
% 0: never switch door
% 1: always switch door
% 2: switch door at random (switch or stay with equal probability)
% "trials" is the number of times you execute the game.
% The pseudocode is given below, you need to write corresponding Matlab code.


%{
foreach iteration
  randomly determine which door has the car.
  player picks a door randomly.
  among the two doors the player did not pick,
   randomly discard one that doesn't have the car.
  apply the strategy
  if player wins, increase a winning counter
calculate the winratio from the winning counter.
%}

