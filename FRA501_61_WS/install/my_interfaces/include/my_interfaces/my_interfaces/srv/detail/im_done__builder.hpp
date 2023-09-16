// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/ImDone.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__IM_DONE__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__IM_DONE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/im_done__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_ImDone_Request_imhere
{
public:
  explicit Init_ImDone_Request_imhere(::my_interfaces::srv::ImDone_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::ImDone_Request imhere(::my_interfaces::srv::ImDone_Request::_imhere_type arg)
  {
    msg_.imhere = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::ImDone_Request msg_;
};

class Init_ImDone_Request_success
{
public:
  Init_ImDone_Request_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImDone_Request_imhere success(::my_interfaces::srv::ImDone_Request::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ImDone_Request_imhere(msg_);
  }

private:
  ::my_interfaces::srv::ImDone_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::ImDone_Request>()
{
  return my_interfaces::srv::builder::Init_ImDone_Request_success();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_ImDone_Response_result
{
public:
  Init_ImDone_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::ImDone_Response result(::my_interfaces::srv::ImDone_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::ImDone_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::ImDone_Response>()
{
  return my_interfaces::srv::builder::Init_ImDone_Response_result();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__IM_DONE__BUILDER_HPP_
