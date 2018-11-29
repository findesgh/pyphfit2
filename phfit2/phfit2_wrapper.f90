module phfit2_wrappers
  ! Provides f90 wrappers for phfit2 and does C binding for them.
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
    ! Fortran 90 wrapper for phfit2.
    !
    ! Parameters
    ! ----------
    ! nz : c_int, intent(in)
    !     Atomic number from 1 to 30.
    ! ne : c_int, intent(in)
    !     Number of electrons bound to the nucleus from 1 to nz.
    ! is : c_int, intent(in)
    !    Shell number from 1 to 7 where:
    !               1 - 1s
    !               2 - 2s
    !               3 - 2p
    !               4 - 3s
    !               5 - 3p
    !               6 - 3d
    !               7 - 4s
    ! e : c_float, intent(in)
    !     Photon energy [eV].
    ! s : c_float, intent(out)
    !     Cross section [Mb].
    integer(c_int), intent(in), value :: nz, ne, is
    real(c_float), intent(in), value :: e
    real(c_float), intent(out) :: s

    call phfit2(nz, ne, is, e, s)
  end subroutine wrapper

  subroutine arr_wrapper(nz, ne, is, e, le, s) bind(c, name='c_phfit2_arr')
    ! Fortran 90 wrapper for phfit2 that loops over photon energies.
    !
    ! Parameters
    ! ----------
    ! nz : c_int, intent(in)
    !     Atomic number from 1 to 30.
    ! ne : c_int, intent(in)
    !     Number of electrons bound to the nucleus from 1 to nz.
    ! is : c_int, intent(in)
    !    Shell number from 1 to 7 where:
    !               1 - 1s
    !               2 - 2s
    !               3 - 2p
    !               4 - 3s
    !               5 - 3p
    !               6 - 3d
    !               7 - 4s
    ! le : c_int, intent(in)
    !     Length of energy array.
    ! e : c_float(le), intent(in)
    !     Photon energy [eV].
    ! s : c_float(le), intent(out)
    !     Cross section [Mb].
    integer(c_int), intent(in), value :: nz, ne, is, le
    real(c_float), intent(in) :: e(le)
    real(c_float), intent(out) :: s(le)
    integer :: i

    do i=1, le
       call phfit2(nz, ne, is, e(i), s(i))
    end do
  end subroutine arr_wrapper
end module phfit2_wrappers
