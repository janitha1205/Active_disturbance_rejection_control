dt=0.001;
t=0;
t1=[];
y=[];
yd=[];
x1=0;
x2=0;
u=0;
x1_ob=0;
x2_ob=0;
while(t<30)
x1_ref=20.3*sin(t);
x2_ref=20.3*cos(t);
z=0.3*sin(7*t)+0.7*cos(2*t);

[x1_ob,x2_ob,z_1]=extobs(x1,x1_ob,x2_ob,u,z,dt);
u=controller(x1_ref,x2_ref,x1_ob,x2_ob,z_1);
[x1,x2]=sysdyn(x1_ob,x2_ob,u,z,dt);



y=[y,z_1];
yd=[yd,z];
t1=[t1,t];
t+=dt;
endwhile
plot(t1,y,'r',t1,yd,'b');
