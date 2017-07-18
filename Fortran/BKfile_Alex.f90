program BKfile
implicit none
integer,parameter :: M=964
integer z(M),N(M),A(M)
real(8) RMS(M)
real(8) LDR

integer i


open(18,file='rms13.dat', status='old')

open(21, file='BK_Alex.dat', status='replace')

do i = 1,M
 read(18,*) Z(i),N(i),A(i),RMS(i)

 if ( i >= 2 .and. Z(i) == Z(i-1) .and. N(i) - N(i-1) == 2 ) then
  write(21,120) Z(i),N(i),A(i),(RMS(i)**2.d0-RMS(i-1)**2.d0)/(LDR(A(i)) - LDR(A(i-1)))
 else if ( i >= 2 .and. Z(i) == Z(i-2) .and. N(i) - N(i-2) == 2 ) then
  write(21,120) Z(i),N(i),A(i),(RMS(i)**2.d0-RMS(i-2)**2.d0)/(LDR(A(i)) - LDR(A(i-2)))
 end if


end do

120 format(i4,1x,i4,1x,i4,1x,f9.4)

end program BKfile




real(8) function LDR(A)
integer A
LDR = 3.d0/5.d0*(1.2d0*A**(1.d0/3.d0))**2.d0
end function LDR
