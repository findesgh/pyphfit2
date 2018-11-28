module phfit2_wrapper
  use iso_c_binding
  implicit none

  interface
     subroutine phfit2(nz, ne, is, e, s)
       integer :: nz, ne, is
       real :: e, s
     end subroutine phfit2
  end interface

contains

  subroutine wrapper(nz, ne, is, e, s) bind(c, name='c_phfit2')
    integer(c_int), intent(in), value :: nz, ne, is
    real(c_float), intent(in), value :: e
    real(c_float), intent(out) :: s

    call phfit2(nz, ne, is, e, s)
  end subroutine wrapper

  subroutine arr_wrapper(nz, ne, is, e, le, s) bind(c, name='c_phfit2_arr')
    integer(c_int), intent(in), value :: nz, ne, is, le
    real(c_float), intent(in) :: e(le)
    real(c_float), intent(out) :: s(le)
    integer :: i

    do i=1, le
       call phfit2(nz, ne, is, e(i), s(i))
    end do
  end subroutine arr_wrapper
end module phfit2_wrapper
