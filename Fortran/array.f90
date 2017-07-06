subroutine array(N,a,b)
integer,intent(in) :: N
integer,intent(in) :: a(N)

integer,intent(out) :: b(N)
!---------------
b = a+1

end subroutine array
