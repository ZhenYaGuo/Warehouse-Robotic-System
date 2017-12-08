// Generated by gencpp from file ric_board/StatusMsg.msg
// DO NOT EDIT!


#ifndef RIC_BOARD_MESSAGE_STATUSMSG_H
#define RIC_BOARD_MESSAGE_STATUSMSG_H


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
struct StatusMsg_
{
  typedef StatusMsg_<ContainerAllocator> Type;

  StatusMsg_()
    : status()  {
    }
  StatusMsg_(const ContainerAllocator& _alloc)
    : status(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int8_t, typename ContainerAllocator::template rebind<int8_t>::other >  _status_type;
  _status_type status;




  typedef boost::shared_ptr< ::ric_board::StatusMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ric_board::StatusMsg_<ContainerAllocator> const> ConstPtr;

}; // struct StatusMsg_

typedef ::ric_board::StatusMsg_<std::allocator<void> > StatusMsg;

typedef boost::shared_ptr< ::ric_board::StatusMsg > StatusMsgPtr;
typedef boost::shared_ptr< ::ric_board::StatusMsg const> StatusMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ric_board::StatusMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ric_board::StatusMsg_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::ric_board::StatusMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ric_board::StatusMsg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::StatusMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ric_board::StatusMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::StatusMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ric_board::StatusMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ric_board::StatusMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "21d91a12bf821d316d02563643915b12";
  }

  static const char* value(const ::ric_board::StatusMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x21d91a12bf821d31ULL;
  static const uint64_t static_value2 = 0x6d02563643915b12ULL;
};

template<class ContainerAllocator>
struct DataType< ::ric_board::StatusMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ric_board/StatusMsg";
  }

  static const char* value(const ::ric_board::StatusMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ric_board::StatusMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int8[] status\n\
";
  }

  static const char* value(const ::ric_board::StatusMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ric_board::StatusMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StatusMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ric_board::StatusMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ric_board::StatusMsg_<ContainerAllocator>& v)
  {
    s << indent << "status[]" << std::endl;
    for (size_t i = 0; i < v.status.size(); ++i)
    {
      s << indent << "  status[" << i << "]: ";
      Printer<int8_t>::stream(s, indent + "  ", v.status[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // RIC_BOARD_MESSAGE_STATUSMSG_H
