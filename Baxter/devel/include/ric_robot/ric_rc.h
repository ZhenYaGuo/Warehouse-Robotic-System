// Generated by gencpp from file ric_robot/ric_rc.msg
// DO NOT EDIT!


#ifndef RIC_ROBOT_MESSAGE_RIC_RC_H
#define RIC_ROBOT_MESSAGE_RIC_RC_H


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
struct ric_rc_
{
  typedef ric_rc_<ContainerAllocator> Type;

  ric_rc_()
    : RX1(0)
    , RX2(0)
    , RX3(0)
    , RX4(0)
    , RX5(0)
    , RX6(0)  {
    }
  ric_rc_(const ContainerAllocator& _alloc)
    : RX1(0)
    , RX2(0)
    , RX3(0)
    , RX4(0)
    , RX5(0)
    , RX6(0)  {
  (void)_alloc;
    }



   typedef uint16_t _RX1_type;
  _RX1_type RX1;

   typedef uint16_t _RX2_type;
  _RX2_type RX2;

   typedef uint16_t _RX3_type;
  _RX3_type RX3;

   typedef uint16_t _RX4_type;
  _RX4_type RX4;

   typedef uint16_t _RX5_type;
  _RX5_type RX5;

   typedef uint16_t _RX6_type;
  _RX6_type RX6;




  typedef boost::shared_ptr< ::ric_robot::ric_rc_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_robot::ric_rc_<ContainerAllocator> const> ConstPtr;

}; // struct ric_rc_

typedef ::ric_robot::ric_rc_<std::allocator<void> > ric_rc;

typedef boost::shared_ptr< ::ric_robot::ric_rc > ric_rcPtr;
typedef boost::shared_ptr< ::ric_robot::ric_rc const> ric_rcConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_robot::ric_rc_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_robot::ric_rc_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::ric_robot::ric_rc_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_robot::ric_rc_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_robot::ric_rc_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_robot::ric_rc_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_robot::ric_rc_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_robot::ric_rc_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_robot::ric_rc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "141c3eb3d7391c30d945399a5b34b7d1";
  }

  static const char* value(const ::ric_robot::ric_rc_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x141c3eb3d7391c30ULL;
  static const uint64_t static_value2 = 0xd945399a5b34b7d1ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_robot::ric_rc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_robot/ric_rc";
  }

  static const char* value(const ::ric_robot::ric_rc_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_robot::ric_rc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint16 RX1\n\
uint16 RX2\n\
uint16 RX3\n\
uint16 RX4\n\
uint16 RX5\n\
uint16 RX6\n\
";
  }

  static const char* value(const ::ric_robot::ric_rc_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_robot::ric_rc_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.RX1);
      stream.next(m.RX2);
      stream.next(m.RX3);
      stream.next(m.RX4);
      stream.next(m.RX5);
      stream.next(m.RX6);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ric_rc_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_robot::ric_rc_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_robot::ric_rc_<ContainerAllocator>& v)
  {
    s << indent << "RX1: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX1);
    s << indent << "RX2: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX2);
    s << indent << "RX3: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX3);
    s << indent << "RX4: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX4);
    s << indent << "RX5: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX5);
    s << indent << "RX6: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.RX6);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_ROBOT_MESSAGE_RIC_RC_H
