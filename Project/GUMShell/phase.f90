
!==============================================================================================
! expectation value of  <b|a+(p)a+(q)a(s)a(r)|a> (= phase = -1 or 0 or +1) and what the final state b is
!==============================================================================================
! input: states : p,q,r,s
! input: particle number : N
! input: slater determinant (like 1,2,3,4 (normal ordered)) : a
! output: final slater determinant (like 1,2,6,7 (normal ordered)) : b
! output: resulting phase (like 1,4,2,5 to 1,2,4,5 then phase = (-1)**(1) ) : phase
!----------------------------------------------------------------------------------------------
subroutine bandp(p,q,r,s,N,a,b,phase)
integer,intent(in) :: p
integer,intent(in) :: q
integer,intent(in) :: r
integer,intent(in) :: s
integer,intent(in) :: N

integer,intent(inout) :: a(N)
!f2py intent(in, out) :: a(N)

integer,intent(out) :: b(N)
!f2py intent(out) :: b(N)
integer,intent(out) :: phase
!----------------------------------
integer i1,i2
integer point
integer c(N)

point = 0
c = a

loop1: do i = 1,N-1
 loop2: do j = i+1,N
  if ( r == a(i) .and. s == a(j) ) then
   point = 1
   a(i) = p
   a(j) = q
   exit loop1
  end if
 end do loop2
end do loop1

loop3: do i = 1,N-1
  loop4: do j = i+1,N
   if ( a(i) == a(j) ) then
    point = 0
   exit loop3
   end if
  end do loop4
end do loop3

if (point == 0) then
 phase = 0
 b = c
else if (point == 1) then
 call sort(N,a,phase)
 b = a
end if

end subroutine bandp
!----------------------------------------------------------------------------------------------





!==============================================================================================
! Normal ordering and phase
!==============================================================================================
! input: particle number : N
! input: slater determinant (e.g. 1,4,2,5) : a
! output: resulting phase (e.g. 1,4,2,5 to 1,2,4,5 then phase = (-1)**(1) ) : phase
!----------------------------------------------------------------------------------------------
subroutine sort(N,a,phase)
integer,intent(in) :: N        ! particle's number

integer,intent(inout) :: a(N)     ! slater determinant

integer,intent(out) :: phase      ! phase ( <b|a+(p)a+(q)a(s)a(r)|a> )
!----------------------------------
integer i,j
integer number
integer p

number = 0
do i = 1,N-1
  do j = i+1,N
   if ( a(j) < a(i) ) then
     number = number + 1         ! counting how many times permutation is needed
     p = a(i)
     a(i) = a(j)
     a(j) = p
   end if
  end do
end do

phase = (-1)**(number)
end subroutine sort
!----------------------------------------------------------------------------------------------
