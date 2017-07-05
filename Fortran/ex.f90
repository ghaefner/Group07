! example file
! input a,b (integer)
! output c = a + b (integer)

subroutine ex(a,b,c)
integer,intent(in) :: a
integer,intent(in) :: b

integer,intent(out) :: c

c = a + b

end subroutine ex
