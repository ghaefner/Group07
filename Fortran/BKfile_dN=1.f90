program BKfile
implicit none
integer,parameter :: M=964
integer z(M),N(M),A(M)
real(8) RMS(M)
integer i


open(18,file='rms13.dat', status='old')

open(21, file='BK_dN=1.dat', status='replace')

do i = 1,M
 read(18,*) Z(i),N(i),A(i),RMS(i)

 if ( i >= 2 .and. Z(i) == Z(i-1) .and. (N(i) - N(i-1) == 1) ) then
  write(21,120) Z(i),N(i),A(i),RMS(i)-RMS(i-1)
 end if



end do

120 format(i4,1x,i4,1x,i4,1x,f9.4)

end program BKfile
