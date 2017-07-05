! vector input test
! input n,p (integer)
! output n dimensional vector (integer)

subroutine vec(n,p,v)
integer,intent(in) :: n
integer,intent(in) :: p

integer,intent(out) :: v(1:n)

integer i

do i = 1,n
v(i) = p + i - 1
end do

end subroutine vec
