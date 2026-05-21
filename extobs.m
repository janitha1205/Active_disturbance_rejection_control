function [x1_ob1,x2_ob1,z1]=extobs(x1,x1_ob,x2_ob,u,z,dt)
  lem_1=10.0;
  lem_2=120.0;
  lem_3=4000.0;
  dx1_ob=x2_ob+lem_1*(x1-x1_ob);
  dx2_ob=u+lem_2*(x1-x1_ob)+z;
  dz=lem_3*(x1-x1_ob);
  x1_ob1=dx1_ob*dt+x1_ob;
  x2_ob1=dx2_ob*dt+x2_ob;
  z1=dz*dt+z;
endfunction
