// Generated by gencpp from file ric_board/Motor.msg
// DO NOT EDIT!


#ifndef RIC_BOARD_MESSAGE_MOTOR_H
#define RIC_BOARD_MESSAGE_MOTOR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ric_board
{
template <class ContainerAllocator>
struct Motor_
{
  typedef Motor_<ContainerAllocator> Type;

  Motor_()
    : position(0.0)
    , velocity(0.0)  {
    }
  Motor_(const ContainerAllocator& _alloc)
    : position(0.0)
    , velocity(0.0)  {
  (void)_alloc;
    }



   typedef float _position_type;
  _position_type position;

   typedef float _velocity_type;
  _velocity_type velocity;




  typedef boost::shared_ptr< ::ric_board::Motor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_board::Motor_<ContainerAllocator> const> ConstPtr;

}; // struct Motor_

typedef ::ric_board::Motor_<std::allocator<void> > Motor;

typedef boost::shared_ptr< ::ric_board::Motor > MotorPtr;
typedef boost::shared_ptr< ::ric_board::Motor const> MotorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_board::Motor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_board::Motor_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ric_board

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'ric_board': ['/home/cc/ee106a/fa17/class/ee106a-aax/ros_workspaces/project/src/ric/ric_board/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::Motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::Motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Motor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Motor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_board::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2cf6c2ef6d4814960f7bd2c448525593";
  }

  static const char* value(const ::ric_board::Motor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2cf6c2ef6d481496ULL;
  static const uint64_t static_value2 = 0x0f7bd2c448525593ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_board::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_board/Motor";
  }

  static const char* value(const ::ric_board::Motor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_board::Motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 position\n\
float32 velocity\n\
";
  }

  static const char* value(const ::ric_board::Motor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_board::Motor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.position);
      stream.next(m.velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Motor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_board::Motor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_board::Motor_<ContainerAllocator>& v)
  {
    s << indent << "position: ";
    Printer<float>::stream(s, indent + "  ", v.position);
    s << indent << "velocity: ";
    Printer<float>::stream(s, indent + "  ", v.velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_BOARD_MESSAGE_MOTOR_H
