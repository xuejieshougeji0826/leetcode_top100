# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/876.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/876.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/876.dir/flags.make

CMakeFiles/876.dir/876.cpp.o: CMakeFiles/876.dir/flags.make
CMakeFiles/876.dir/876.cpp.o: ../876.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/876.dir/876.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/876.dir/876.cpp.o -c /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/876.cpp

CMakeFiles/876.dir/876.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/876.dir/876.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/876.cpp > CMakeFiles/876.dir/876.cpp.i

CMakeFiles/876.dir/876.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/876.dir/876.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/876.cpp -o CMakeFiles/876.dir/876.cpp.s

# Object files for target 876
876_OBJECTS = \
"CMakeFiles/876.dir/876.cpp.o"

# External object files for target 876
876_EXTERNAL_OBJECTS =

876: CMakeFiles/876.dir/876.cpp.o
876: CMakeFiles/876.dir/build.make
876: CMakeFiles/876.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 876"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/876.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/876.dir/build: 876

.PHONY : CMakeFiles/876.dir/build

CMakeFiles/876.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/876.dir/cmake_clean.cmake
.PHONY : CMakeFiles/876.dir/clean

CMakeFiles/876.dir/depend:
	cd /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug /Users/gzc/Downloads/研二下+实习/研二下/leetcode_top100/cpp/cmake-build-debug/CMakeFiles/876.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/876.dir/depend

