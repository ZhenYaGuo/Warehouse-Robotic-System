# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build

# Include any dependencies generated for this target.
include ric/ric_robot/CMakeFiles/ric_node.dir/depend.make

# Include the progress variables for this target.
include ric/ric_robot/CMakeFiles/ric_node.dir/progress.make

# Include the compile flags for this target's objects.
include ric/ric_robot/CMakeFiles/ric_node.dir/flags.make

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o: ric/ric_robot/CMakeFiles/ric_node.dir/flags.make
ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o: /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot/src/ric_node.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o"
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/ric_node.dir/src/ric_node.cpp.o -c /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot/src/ric_node.cpp

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ric_node.dir/src/ric_node.cpp.i"
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot/src/ric_node.cpp > CMakeFiles/ric_node.dir/src/ric_node.cpp.i

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ric_node.dir/src/ric_node.cpp.s"
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot/src/ric_node.cpp -o CMakeFiles/ric_node.dir/src/ric_node.cpp.s

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.requires:
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.requires

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.provides: ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.requires
	$(MAKE) -f ric/ric_robot/CMakeFiles/ric_node.dir/build.make ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.provides.build
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.provides

ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.provides.build: ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o

# Object files for target ric_node
ric_node_OBJECTS = \
"CMakeFiles/ric_node.dir/src/ric_node.cpp.o"

# External object files for target ric_node
ric_node_EXTERNAL_OBJECTS =

/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: ric/ric_robot/CMakeFiles/ric_node.dir/build.make
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libtf.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libtf2_ros.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libactionlib.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libtf2.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_common_planning_interface_objects.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_scene_interface.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_move_group_interface.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_warehouse.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libwarehouse_ros.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_pick_place_planner.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_move_group_capabilities_base.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_rdf_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_kinematics_plugin_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_robot_model_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_constraint_sampler_manager_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_pipeline.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_trajectory_execution_manager.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_plan_execution.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_scene_monitor.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_collision_plugin_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_lazy_free_space_updater.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_point_containment_filter.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_occupancy_map_monitor.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_pointcloud_octomap_updater_core.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_semantic_world.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_exceptions.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_background_processing.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_kinematics_base.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_robot_model.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_transforms.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_robot_state.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_robot_trajectory.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_interface.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_collision_detection.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_collision_detection_fcl.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_kinematic_constraints.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_scene.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_constraint_samplers.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_planning_request_adapter.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_profiler.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_trajectory_processing.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_distance_field.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_kinematics_metrics.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmoveit_dynamics_solver.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libeigen_conversions.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libgeometric_shapes.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/liboctomap.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/liboctomath.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libkdl_parser.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/liborocos-kdl.so.1.3.0
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/liburdf.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/liburdfdom_sensor.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/liburdfdom_model_state.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/liburdfdom_model.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/liburdfdom_world.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librosconsole_bridge.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librandom_numbers.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libsrdfdom.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libimage_transport.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libmessage_filters.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libclass_loader.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/libPocoFoundation.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libdl.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libroscpp.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librosconsole.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/liblog4cxx.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libroslib.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librospack.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/librostime.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /opt/ros/indigo/lib/libcpp_common.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node: ric/ric_robot/CMakeFiles/ric_node.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node"
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ric_node.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
ric/ric_robot/CMakeFiles/ric_node.dir/build: /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/devel/lib/ric_robot/ric_node
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/build

ric/ric_robot/CMakeFiles/ric_node.dir/requires: ric/ric_robot/CMakeFiles/ric_node.dir/src/ric_node.cpp.o.requires
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/requires

ric/ric_robot/CMakeFiles/ric_node.dir/clean:
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot && $(CMAKE_COMMAND) -P CMakeFiles/ric_node.dir/cmake_clean.cmake
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/clean

ric/ric_robot/CMakeFiles/ric_node.dir/depend:
	cd /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot /home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/build/ric/ric_robot/CMakeFiles/ric_node.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ric/ric_robot/CMakeFiles/ric_node.dir/depend

