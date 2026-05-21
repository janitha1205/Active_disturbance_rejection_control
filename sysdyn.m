function [x1,x2]=sysdyn(x1,x2,u,d,dt)
 g=9.81;
 L=0.12;
 x1_dot=x2;
 x2_dot=u-(g/L)*sin(x1)+d;
 x2+=x2_dot*dt;
 x1+=x1_dot*dt;
endfunction
