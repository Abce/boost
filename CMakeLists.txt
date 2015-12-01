set(BOOST_SRC 	libs/system/src/error_code.cpp
				libs/thread/src/future.cpp
				libs/thread/src/tss_null.cpp
				libs/thread/src/pthread/once.cpp
				libs/thread/src/pthread/once_atomic.cpp
				libs/thread/src/pthread/thread.cpp
				)
add_library(boost STATIC ${BOOST_SRC})
target_include_directories(boost PRIVATE ./)