# CMake generated Testfile for 
# Source directory: /home/administrador/Desktop/dev_ws/src/BehaviorTree.CPP/tests
# Build directory: /home/administrador/Desktop/dev_ws/build/behaviortree_cpp/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(behaviortree_cpp_test "/usr/bin/python3.10" "-u" "/opt/ros/iron/share/ament_cmake_test/cmake/run_test.py" "/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/test_results/behaviortree_cpp/behaviortree_cpp_test.gtest.xml" "--package-name" "behaviortree_cpp" "--output-file" "/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/ament_cmake_gtest/behaviortree_cpp_test.txt" "--command" "/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/tests/behaviortree_cpp_test" "--gtest_output=xml:/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/test_results/behaviortree_cpp/behaviortree_cpp_test.gtest.xml")
set_tests_properties(behaviortree_cpp_test PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/tests/behaviortree_cpp_test" TIMEOUT "60" WORKING_DIRECTORY "/home/administrador/Desktop/dev_ws/build/behaviortree_cpp/tests" _BACKTRACE_TRIPLES "/opt/ros/iron/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/iron/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;86;ament_add_test;/opt/ros/iron/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/administrador/Desktop/dev_ws/src/BehaviorTree.CPP/tests/CMakeLists.txt;41;ament_add_gtest;/home/administrador/Desktop/dev_ws/src/BehaviorTree.CPP/tests/CMakeLists.txt;0;")
subdirs("../gtest")
