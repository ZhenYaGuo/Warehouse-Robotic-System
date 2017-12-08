// Generated by gencpp from file ric_board/Odom.msg
// DO NOT EDIT!


#ifndef RIC_BOARD_MESSAGE_ODOM_H
#define RIC_BOARD_MESSAGE_ODOM_H


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
struct Odom_
{
  typedef Odom_<ContainerAllocator> Type;

  Odom_()
    : x(0.0)
    , y(0.0)
    , theta(0.0)
    , x_vel(0.0)
    , y_vel(0.0)
    , theta_vel(0.0)  {
    }
  Odom_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , theta(0.0)
    , x_vel(0.0)
    , y_vel(0.0)
    , theta_vel(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _theta_type;
  _theta_type theta;

   typedef double _x_vel_type;
  _x_vel_type x_vel;

   typedef double _y_vel_type;
  _y_vel_type y_vel;

   typedef double _theta_vel_type;
  _theta_vel_type theta_vel;




  typedef boost::shared_ptr< ::ric_board::Odom_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_board::Odom_<ContainerAllocator> const> ConstPtr;

}; // struct Odom_

typedef ::ric_board::Odom_<std::allocator<void> > Odom;

typedef boost::shared_ptr< ::ric_board::Odom > OdomPtr;
typedef boost::shared_ptr< ::ric_board::Odom const> OdomConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_board::Odom_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_board::Odom_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::ric_board::Odom_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::Odom_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Odom_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::Odom_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Odom_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::Odom_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_board::Odom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e6ef1346804e297029361956b8a1e971";
  }

  static const char* value(const ::ric_board::Odom_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe6ef1346804e2970ULL;
  static const uint64_t static_value2 = 0x29361956b8a1e971ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_board::Odom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_board/Odom";
  }

  static const char* value(const ::ric_board::Odom_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_board::Odom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n\
float64 y\n\
float64 theta\n\
float64 x_vel\n\
float64 y_vel\n\
float64 theta_vel\n\
";
  }

  static const char* value(const ::ric_board::Odom_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_board::Odom_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.theta);
      stream.next(m.x_vel);
      stream.next(m.y_vel);
      stream.next(m.theta_vel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Odom_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_board::Odom_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_board::Odom_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "theta: ";
    Printer<double>::stream(s, indent + "  ", v.theta);
    s << indent << "x_vel: ";
    Printer<double>::stream(s, indent + "  ", v.x_vel);
    s << indent << "y_vel: ";
    Printer<double>::stream(s, indent + "  ", v.y_vel);
    s << indent << "theta_vel: ";
    Printer<double>::stream(s, indent + "  ", v.theta_vel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_BOARD_MESSAGE_ODOM_H
