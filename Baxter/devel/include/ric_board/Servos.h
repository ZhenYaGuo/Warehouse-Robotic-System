// Generated by gencpp from file ric_board/Servos.msg
// DO NOT EDIT!


#ifndef RIC_BOARD_MESSAGE_SERVOS_H
#define RIC_BOARD_MESSAGE_SERVOS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <ric_board/Named_Data.h>

namespace ric_board
{
template <class ContainerAllocator>
struct Servos_
{
  typedef Servos_<ContainerAllocator> Type;

  Servos_()
    : servos()  {
    }
  Servos_(const ContainerAllocator& _alloc)
    : servos()  {
  (void)_alloc;
      servos.assign( ::ric_board::Named_Data_<ContainerAllocator> (_alloc));
  }



   typedef boost::array< ::ric_board::Named_Data_<ContainerAllocator> , 2>  _servos_type;
  _servos_type servos;




  typedef boost::shared_ptr< ::ric_board::Servos_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_board::Servos_<ContainerAllocator> const> ConstPtr;

}; // struct Servos_

typedef ::ric_board::Servos_<std::allocator<void> > Servos;

typedef boost::shared_ptr< ::ric_board::Servos > ServosPtr;
typedef boost::shared_ptr< ::ric_board::Servos const> ServosConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_board::Servos_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_board::Servos_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ric_board

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'ric_board': ['/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_board/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::Servos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::Servos_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Servos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Servos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Servos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Servos_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_board::Servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "08598a0aa2667aecb6d49af080bd4a40";
  }

  static const char* value(const ::ric_board::Servos_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x08598a0aa2667aecULL;
  static const uint64_t static_value2 = 0xb6d49af080bd4a40ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_board::Servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_board/Servos";
  }

  static const char* value(const ::ric_board::Servos_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_board::Servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Named_Data[2] servos\n\
\n\
================================================================================\n\
MSG: ric_board/Named_Data\n\
float32 data\n\
string name\n\
\n\
\n\
";
  }

  static const char* value(const ::ric_board::Servos_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_board::Servos_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.servos);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Servos_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_board::Servos_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_board::Servos_<ContainerAllocator>& v)
  {
    s << indent << "servos[]" << std::endl;
    for (size_t i = 0; i < v.servos.size(); ++i)
    {
      s << indent << "  servos[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ric_board::Named_Data_<ContainerAllocator> >::stream(s, indent + "    ", v.servos[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_BOARD_MESSAGE_SERVOS_H
