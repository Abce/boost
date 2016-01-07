cmake_minimum_required(VERSION 3.1)

set(BOOST_SRC 	libs/system/src/error_code.cpp
				libs/thread/src/future.cpp
				libs/thread/src/tss_null.cpp
				libs/thread/src/pthread/once.cpp
				libs/thread/src/pthread/once_atomic.cpp
				libs/thread/src/pthread/thread.cpp
				)
add_library(boost STATIC ${BOOST_SRC})
target_include_directories(boost PRIVATE ./)

set(BOOST_UNITTEST_SRC 	libs/test/src/compiler_log_formatter.cpp
						#libs/test/src/cpp_main.cpp
						libs/test/src/debug.cpp
						libs/test/src/exception_safety.cpp
						libs/test/src/execution_monitor.cpp
						libs/test/src/framework.cpp
						libs/test/src/interaction_based.cpp
						libs/test/src/logged_expectations.cpp
						libs/test/src/plain_report_formatter.cpp
						libs/test/src/progress_monitor.cpp
						libs/test/src/results_collector.cpp
						libs/test/src/results_reporter.cpp
						#libs/test/src/test_main.cpp
						libs/test/src/test_tools.cpp
						libs/test/src/unit_test_log.cpp
						libs/test/src/unit_test_main.cpp
						libs/test/src/unit_test_monitor.cpp
						libs/test/src/unit_test_parameters.cpp
						libs/test/src/unit_test_suite.cpp
						libs/test/src/xml_log_formatter.cpp
						libs/test/src/xml_report_formatter.cpp
						)
add_library(boost_unittest STATIC ${BOOST_UNITTEST_SRC})
target_include_directories(boost_unittest PRIVATE ./)