#!/bin/sh
# Shell wrapper for Phing
# $Id$
#
# This script will do the following:
# - check for PHP_COMMAND env, if found, use it.
#   - if not found assume php is on the path
# - check for PHING_HOME evn, if found use it
#   - if not look for it
# - check for PHP_CLASSPATH, if found use it
#   - if not found set it using PHING_HOME/classes

if [ -z "$PHING_HOME" ]; then
  # make it available in PHP via getenv("PHING_HOME")
  export PHING_HOME=/usr/share/phing
fi

if [ -z "$PHP_COMMAND" ]; then
	export PHP_COMMAND=php
fi

if [ -z "$PHP_CLASSPATH" ]; then
	export PHP_CLASSPATH=$PHING_HOME/classes
fi

$PHP_COMMAND $PHING_HOME/bin/phing.php -logger phing.listener.AnsiColorLogger $@
