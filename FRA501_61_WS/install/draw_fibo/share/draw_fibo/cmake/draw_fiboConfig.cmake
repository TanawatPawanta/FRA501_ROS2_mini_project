# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_draw_fibo_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED draw_fibo_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(draw_fibo_FOUND FALSE)
  elseif(NOT draw_fibo_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(draw_fibo_FOUND FALSE)
  endif()
  return()
endif()
set(_draw_fibo_CONFIG_INCLUDED TRUE)

# output package information
if(NOT draw_fibo_FIND_QUIETLY)
  message(STATUS "Found draw_fibo: 0.0.0 (${draw_fibo_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'draw_fibo' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${draw_fibo_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(draw_fibo_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${draw_fibo_DIR}/${_extra}")
endforeach()
