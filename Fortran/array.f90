subroutine array(N,a,i,b)
integer,intent(in) :: N
integer,intent(in) :: a(N)

integer,intent(out) :: b
!---------------
integer c(N)

c = a+1

b = c(i)


end subroutine array
