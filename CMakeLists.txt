set(BOOST_SRC libs/system/src/error_code.cpp)
add_library(boost STATIC ${BOOST_SRC})
target_include_directories(boost PRIVATE ./)