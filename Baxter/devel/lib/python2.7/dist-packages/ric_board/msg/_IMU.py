# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ric_board/IMU.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class IMU(genpy.Message):
  _md5sum = "e8a98900b806343478f736605d2b07cf"
  _type = "ric_board/IMU"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Quaternion orientation
float32[3] linear_acceleration
float32[3] angular_velocity
float32[3] magnetometer
float32 temperature
float32 pitch
float32 yaw
float32 roll




================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['orientation','linear_acceleration','angular_velocity','magnetometer','temperature','pitch','yaw','roll']
  _slot_types = ['geometry_msgs/Quaternion','float32[3]','float32[3]','float32[3]','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       orientation,linear_acceleration,angular_velocity,magnetometer,temperature,pitch,yaw,roll

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IMU, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      if self.linear_acceleration is None:
        self.linear_acceleration = [0.,0.,0.]
      if self.angular_velocity is None:
        self.angular_velocity = [0.,0.,0.]
      if self.magnetometer is None:
        self.magnetometer = [0.,0.,0.]
      if self.temperature is None:
        self.temperature = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.roll is None:
        self.roll = 0.
    else:
      self.orientation = geometry_msgs.msg.Quaternion()
      self.linear_acceleration = [0.,0.,0.]
      self.angular_velocity = [0.,0.,0.]
      self.magnetometer = [0.,0.,0.]
      self.temperature = 0.
      self.pitch = 0.
      self.yaw = 0.
      self.roll = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w))
      buff.write(_struct_3f.pack(*self.linear_acceleration))
      buff.write(_struct_3f.pack(*self.angular_velocity))
      buff.write(_struct_3f.pack(*self.magnetometer))
      _x = self
      buff.write(_struct_4f.pack(_x.temperature, _x.pitch, _x.yaw, _x.roll))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w,) = _struct_4d.unpack(str[start:end])
      start = end
      end += 12
      self.linear_acceleration = _struct_3f.unpack(str[start:end])
      start = end
      end += 12
      self.angular_velocity = _struct_3f.unpack(str[start:end])
      start = end
      end += 12
      self.magnetometer = _struct_3f.unpack(str[start:end])
      _x = self
      start = end
      end += 16
      (_x.temperature, _x.pitch, _x.yaw, _x.roll,) = _struct_4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w))
      buff.write(self.linear_acceleration.tostring())
      buff.write(self.angular_velocity.tostring())
      buff.write(self.magnetometer.tostring())
      _x = self
      buff.write(_struct_4f.pack(_x.temperature, _x.pitch, _x.yaw, _x.roll))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w,) = _struct_4d.unpack(str[start:end])
      start = end
      end += 12
      self.linear_acceleration = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.angular_velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.magnetometer = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      _x = self
      start = end
      end += 16
      (_x.temperature, _x.pitch, _x.yaw, _x.roll,) = _struct_4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4f = struct.Struct("<4f")
_struct_4d = struct.Struct("<4d")
_struct_3f = struct.Struct("<3f")
