// Generated by gencpp from file ric_robot/ric_command.msg
// DO NOT EDIT!


#ifndef RIC_ROBOT_MESSAGE_RIC_COMMAND_H
#define RIC_ROBOT_MESSAGE_RIC_COMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ric_robot
{
template <class ContainerAllocator>
struct ric_command_
{
  typedef ric_command_<ContainerAllocator> Type;

  ric_command_()
    : left_wheel(0)
    , right_wheel(0)  {
    }
  ric_command_(const ContainerAllocator& _alloc)
    : left_wheel(0)
    , right_wheel(0)  {
  (void)_alloc;
    }



   typedef int32_t _left_wheel_type;
  _left_wheel_type left_wheel;

   typedef int32_t _right_wheel_type;
  _right_wheel_type right_wheel;




  typedef boost::shared_ptr< ::ric_robot::ric_command_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_robot::ric_command_<ContainerAllocator> const> ConstPtr;

}; // struct ric_command_

typedef ::ric_robot::ric_command_<std::allocator<void> > ric_command;

typedef boost::shared_ptr< ::ric_robot::ric_command > ric_commandPtr;
typedef boost::shared_ptr< ::ric_robot::ric_command const> ric_commandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_robot::ric_command_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_robot::ric_command_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ric_robot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'ric_robot': ['/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_robot/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ric_robot::ric_command_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_robot::ric_command_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_robot::ric_command_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_robot::ric_command_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_robot::ric_command_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_robot::ric_command_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_robot::ric_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3cad0bda4aa523fe6ab3c0809a84e390";
  }

  static const char* value(const ::ric_robot::ric_command_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3cad0bda4aa523feULL;
  static const uint64_t static_value2 = 0x6ab3c0809a84e390ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_robot::ric_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_robot/ric_command";
  }

  static const char* value(const ::ric_robot::ric_command_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_robot::ric_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 left_wheel\n\
int32 right_wheel\n\
\n\
\n\
";
  }

  static const char* value(const ::ric_robot::ric_command_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_robot::ric_command_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.left_wheel);
      stream.next(m.right_wheel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ric_command_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_robot::ric_command_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_robot::ric_command_<ContainerAllocator>& v)
  {
    s << indent << "left_wheel: ";
    Printer<int32_t>::stream(s, indent + "  ", v.left_wheel);
    s << indent << "right_wheel: ";
    Printer<int32_t>::stream(s, indent + "  ", v.right_wheel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_ROBOT_MESSAGE_RIC_COMMAND_H
