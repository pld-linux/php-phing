#!/bin/sh
# Shell wrapper for Phing
#
# This script will do the following:
# - check for PHP_CLASSPATH, if found use it
#   - if not found set it using PHING_HOME/classes

if [ -z "$PHP_CLASSPATH" ]; then
	export PHP_CLASSPATH=/usr/share/php
fi

if [ -z "$PHP_COMMAND" ]; then
	export PHP_COMMAND=/usr/bin/php
fi

export PHING_HOME=/usr/share/php/phing

exec $PHP_COMMAND /usr/share/php/phing.php -logger phing.listener.DefaultLogger ${1:+"$@"}
