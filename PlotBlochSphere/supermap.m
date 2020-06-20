function [X, Y, Z] = supermap(X, Y, Z, chi)
    RHO = 0.5 * [1 + Z X - 1i * Y; X + 1i*Y 1 - Z];
    RHO = superop(RHO, chi);
    X = 2*real(RHO(1:end/2, end/2+1:end));
    Y = 2*imag(RHO(end/2+1:end, 1:end/2));
    Z = real(RHO(1:end/2, 1:end/2) - RHO(end/2+1:end, end/2+1:end));
end