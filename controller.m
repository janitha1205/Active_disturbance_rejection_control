function [u_c]=controller(x1_ref,x2_ref,x1_ob,x2_ob,z)
  k_p=100.0;
  k_d=10.0;
  u_c=k_p*(x1_ref-x1_ob)+k_d*(x2_ref-x2_ob)-z;

endfunction
