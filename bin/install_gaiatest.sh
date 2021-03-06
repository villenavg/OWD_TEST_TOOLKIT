#!/bin/bash
#
# Handles all dependencies etc... related to installing gaiatest.
#

. $HOME/.OWD_TEST_TOOLKIT_LOCATION

export MYPATH=$(dirname $0)
export CURRPATH=$(pwd)

export BRANCH=${1:-"v1-train"}
LOGFILE=${LOGFILE:-/tmp/gaiatest_setup.log}

printf "\n\n<b>Installing gaiatest (for $BRANCH) and Marionette ...</b>" | tee -a $LOGFILE
printf "\n<b>====================================================</b>\n" | tee -a $LOGFILE

#
# Now re-install everything.
#
printf "\n* Installing the latest gaiatest from github: " | tee -a $LOGFILE
#git clone https://github.com/mozilla/gaia-ui-tests.git >> $LOGFILE 2>&1

if [ ! -d "$GAIATEST_PATH" ]
then
    printf "(need to clone all of 'gaia' - this will take about 10-15 minutes ...)\n\n" | tee -a $LOGFILE
    cd $HOME
	git clone https://github.com/mozilla-b2g/gaia.git --depth 1 >> $LOGFILE 2>&1
	
    printf "\n<b>Switching to branch \"$BRANCH\" of gaiatest ...</b>\n\n" | tee -a $LOGFILE
	cd $HOME/gaia
	git checkout $BRANCH  2> >( tee -a $LOGFILE)
	

	# Temporary hack...
	$OWD_TEST_TOOLKIT_BIN/tmp_hack.sh
else
    printf "(refreshing 'gaia' - this will take just a minute or so ...)\n\n" | tee -a $LOGFILE
    cd $HOME/gaia
    sudo git checkout $BRANCH  2> >( tee -a $LOGFILE)
    sudo git pull
    git fetch origin >> $LOGFILE 2>&1
fi

#
# Install gaiatest.
#
cd $GAIATEST_PATH/..

#
# Install gaiatest and dependencies.
#
printf "\n<b>Installing gaiatest for branch \"$(git branch | grep '*')\" ... </b>\n\n" | tee -a $LOGFILE
sudo python setup.py develop > $LOGFILE.tmp 2>&1


#
# Sometimes a bad network connection causes an error in this installation.
# If this happens, wait 1 minute then try again.
#
x=$(grep -i error $LOGFILE.tmp)
if [ "$x" ]
then
	printf "\n<b>ERRORS detected while setting up gaiatest dependencies! Trying once more in 1 minute ...<b>\n\n" | tee -a $LOGFILE
	sleep 60
	sudo python setup.py develop > $LOGFILE.tmp

	x=$(grep -i error $LOGFILE.tmp)
    cat $LOGFILE.tmp >>$LOGFILE
    rm $LOGFILE.tmp
	if [ "$x" ]
	then
		#
		# This one failed too - exit with an error code, so the test run knows the situation.
		#
		echo "<b>ERROR: Failed 2nd attempt to install gaiatest properly! See $LOGFILE for details.</b>" | tee -a $LOGFILE
		exit 1
	else
		#
		# The 2nd attempt succeeded.
		#
		echo "<b>2nd attempt succeeded!</b>" | tee -a $LOGFILE
	fi
else
    cat $LOGFILE.tmp >> $LOGFILE
    rm $LOGFILE.tmp
fi
