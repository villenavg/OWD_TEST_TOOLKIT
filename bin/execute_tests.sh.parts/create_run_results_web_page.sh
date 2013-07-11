#!/bin/bash
#
# Script to create the html summary file etc...
#
# NOTE: This is intended to be run via the 'run_all_tests.sh' script
# and only works on the CI server (or if "$INSTALL_LOG" is set).
#
if [ ! "$ON_CI_SERVER" ]
then
	printf "(No results web page generated: we're not on the ci server.)"
	exit
fi

#
# Setup dependencies.
#
. $0.parts/setup_dependencies.sh

#
# Build table of any 'extra' setup details that are required.
#
. $0.parts/create_extra_setup_detail_rows.sh

#
# Build table of test case executions summaries.
#
. $0.parts/create_summary_types.sh

#
# Build the final details web page by substituting the variables into the template.
#
# (NOTE: for now, every variable that needs to be substituted has to be listed here.)
#
page_title="${JOB_NAME}-${BUILD_NUMBER}"

[ "$UNEX_FAILS" = "0" ] && BUILD_RESULT="pass" || BUILD_RESULT="fail"

if [ "$ASSERTS_PASSED" -lt "$ASSERTS_TOTAL" ]
then
	PERCENT_PASSED=$(($ASSERTS_PASSED * 100))
	PERCENT_PASSED=$(($PERCENT_PASSED / $ASSERTS_TOTAL))
else
    PERCENT_PASSED="100"
fi
PERCENT_PASSED="$PERCENT_PASSED%"

f_sub_variables_into_webpage    page_title          \
                                JOB_NAME            \
                                BUILD_NUMBER        \
                                RUN_TIME            \
                                blocked             \
                                chance2             \
                                EXTRA_SETUP_DETAILS \
                                SUMMARIES           \
                                END_TIME            \
                                UNEX_PASSES         \
                                UNEX_FAILS          \
                                EX_FAILS            \
                                EX_PASSES           \
                                ASSERTS_PASSED      \
                                ASSERTS_TOTAL       \
                                IGNORED             \
                                UNWRITTEN           \
                                BUILD_RESULT        \
                                PERCENT_PASSED
                                
. $0.parts/build_run_detail_pages.sh
    
##########################################################################
#
# CSS FILE
#
cp $0.parts/run_html.css $RESULT_DIR



##########################################################################
#
# COPY EVERYTHING INTO THE HTML_FILEDIR.
#
cd $RESULT_DIR
cp * $HTML_FILEDIR 2> /dev/null

#
# Output the web page link.
#
printf "$HTML_WEBDIR"


