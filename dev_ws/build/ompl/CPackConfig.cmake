# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


set(CPACK_BUILD_SOURCE_DIRS "/home/administrador/Desktop/dev_ws/src/ompl;/home/administrador/Desktop/dev_ws/build/ompl")
set(CPACK_CMAKE_GENERATOR "Unix Makefiles")
set(CPACK_COMPONENTS_ALL "ompl;python")
set(CPACK_COMPONENTS_ALL_SET_BY_USER "TRUE")
set(CPACK_COMPONENT_OMPL_DISPLAY_NAME "OMPL library, headers, and demos")
set(CPACK_COMPONENT_OMPL_REQUIRED "ON")
set(CPACK_COMPONENT_PYTHON_DEPENDS "ompl")
set(CPACK_COMPONENT_PYTHON_DISPLAY_NAME "Python bindings")
set(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "amd64")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python3.10, libboost-serialization-dev, libboost-filesystem-dev, libboost-system-dev, libboost-program-options-dev, libboost-test-dev, libode-dev, libtriangle-dev")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_FILE "/usr/share/cmake-3.22/Templates/CPack.GenericDescription.txt")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_SUMMARY "ompl built using CMake")
set(CPACK_GENERATOR "DEB;TGZ")
set(CPACK_INSTALL_CMAKE_PROJECTS "/home/administrador/Desktop/dev_ws/build/ompl;ompl;ALL;/")
set(CPACK_INSTALL_PREFIX "/home/administrador/Desktop/dev_ws/install/ompl")
set(CPACK_MODULE_PATH ";/cmake/Modules;/home/administrador/Desktop/dev_ws/src/ompl/CMakeModules")
set(CPACK_NSIS_DISPLAY_NAME "ompl 1.6.0")
set(CPACK_NSIS_INSTALLER_ICON_CODE "")
set(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
set(CPACK_NSIS_PACKAGE_NAME "ompl 1.6.0")
set(CPACK_NSIS_UNINSTALL_NAME "Uninstall")
set(CPACK_OUTPUT_CONFIG_FILE "/home/administrador/Desktop/dev_ws/build/ompl/CPackConfig.cmake")
set(CPACK_PACKAGE_CONTACT "Mark Moll <mmoll@rice.edu>")
set(CPACK_PACKAGE_DEFAULT_LOCATION "/")
set(CPACK_PACKAGE_DESCRIPTION_FILE "/usr/share/cmake-3.22/Templates/CPack.GenericDescription.txt")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "The Open Motion Planning Library (OMPL)")
set(CPACK_PACKAGE_FILE_NAME "ompl_1.6.0_amd64-Ubuntu22.04")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "ompl 1.6.0")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "ompl 1.6.0")
set(CPACK_PACKAGE_NAME "ompl")
set(CPACK_PACKAGE_RELOCATABLE "true")
set(CPACK_PACKAGE_VENDOR "Rice University")
set(CPACK_PACKAGE_VERSION "1.6.0")
set(CPACK_PACKAGE_VERSION_MAJOR "1")
set(CPACK_PACKAGE_VERSION_MINOR "6")
set(CPACK_PACKAGE_VERSION_PATCH "0")
set(CPACK_RESOURCE_FILE_LICENSE "/usr/share/cmake-3.22/Templates/CPack.GenericLicense.txt")
set(CPACK_RESOURCE_FILE_README "/usr/share/cmake-3.22/Templates/CPack.GenericDescription.txt")
set(CPACK_RESOURCE_FILE_WELCOME "/usr/share/cmake-3.22/Templates/CPack.GenericWelcome.txt")
set(CPACK_SET_DESTDIR "OFF")
set(CPACK_SOURCE_GENERATOR "TGZ;ZIP")
set(CPACK_SOURCE_IGNORE_FILES ".git;/.vscode;/build/;.pyc$;.pyo$;__pycache__;.so$;.dylib$;.orig$;.log$;.DS_Store;/html/;/bindings/;TODO;.registered$;binding_generator.py$")
set(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/home/administrador/Desktop/dev_ws/build/ompl/CPackSourceConfig.cmake")
set(CPACK_SYSTEM_NAME "Linux")
set(CPACK_THREADS "1")
set(CPACK_TOPLEVEL_TAG "Linux")
set(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "/home/administrador/Desktop/dev_ws/build/ompl/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()