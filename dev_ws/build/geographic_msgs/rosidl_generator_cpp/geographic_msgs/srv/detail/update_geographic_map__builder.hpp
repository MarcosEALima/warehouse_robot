// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from geographic_msgs:srv/UpdateGeographicMap.idl
// generated code does not contain a copyright notice

#ifndef GEOGRAPHIC_MSGS__SRV__DETAIL__UPDATE_GEOGRAPHIC_MAP__BUILDER_HPP_
#define GEOGRAPHIC_MSGS__SRV__DETAIL__UPDATE_GEOGRAPHIC_MAP__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "geographic_msgs/srv/detail/update_geographic_map__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace geographic_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdateGeographicMap_Request_updates
{
public:
  Init_UpdateGeographicMap_Request_updates()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::geographic_msgs::srv::UpdateGeographicMap_Request updates(::geographic_msgs::srv::UpdateGeographicMap_Request::_updates_type arg)
  {
    msg_.updates = std::move(arg);
    return std::move(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::geographic_msgs::srv::UpdateGeographicMap_Request>()
{
  return geographic_msgs::srv::builder::Init_UpdateGeographicMap_Request_updates();
}

}  // namespace geographic_msgs


namespace geographic_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdateGeographicMap_Response_status
{
public:
  explicit Init_UpdateGeographicMap_Response_status(::geographic_msgs::srv::UpdateGeographicMap_Response & msg)
  : msg_(msg)
  {}
  ::geographic_msgs::srv::UpdateGeographicMap_Response status(::geographic_msgs::srv::UpdateGeographicMap_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Response msg_;
};

class Init_UpdateGeographicMap_Response_success
{
public:
  Init_UpdateGeographicMap_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UpdateGeographicMap_Response_status success(::geographic_msgs::srv::UpdateGeographicMap_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_UpdateGeographicMap_Response_status(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::geographic_msgs::srv::UpdateGeographicMap_Response>()
{
  return geographic_msgs::srv::builder::Init_UpdateGeographicMap_Response_success();
}

}  // namespace geographic_msgs


namespace geographic_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdateGeographicMap_Event_response
{
public:
  explicit Init_UpdateGeographicMap_Event_response(::geographic_msgs::srv::UpdateGeographicMap_Event & msg)
  : msg_(msg)
  {}
  ::geographic_msgs::srv::UpdateGeographicMap_Event response(::geographic_msgs::srv::UpdateGeographicMap_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Event msg_;
};

class Init_UpdateGeographicMap_Event_request
{
public:
  explicit Init_UpdateGeographicMap_Event_request(::geographic_msgs::srv::UpdateGeographicMap_Event & msg)
  : msg_(msg)
  {}
  Init_UpdateGeographicMap_Event_response request(::geographic_msgs::srv::UpdateGeographicMap_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_UpdateGeographicMap_Event_response(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Event msg_;
};

class Init_UpdateGeographicMap_Event_info
{
public:
  Init_UpdateGeographicMap_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UpdateGeographicMap_Event_request info(::geographic_msgs::srv::UpdateGeographicMap_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_UpdateGeographicMap_Event_request(msg_);
  }

private:
  ::geographic_msgs::srv::UpdateGeographicMap_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::geographic_msgs::srv::UpdateGeographicMap_Event>()
{
  return geographic_msgs::srv::builder::Init_UpdateGeographicMap_Event_info();
}

}  // namespace geographic_msgs

#endif  // GEOGRAPHIC_MSGS__SRV__DETAIL__UPDATE_GEOGRAPHIC_MAP__BUILDER_HPP_
