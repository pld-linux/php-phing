#!/bin/sh
# Shell wrapper for Phing
# $Id$
#
# This script will do the following:
# - check for PHP_CLASSPATH, if found use it
#   - if not found set it using PHING_HOME/classes

if [ -z "$PHP_CLASSPATH" ]; then
	export PHP_CLASSPATH=/usr/share/php
fi

exec /usr/bin/php /usr/share/php/phing.php -logger phing.listener.DefaultLogger ${1:+"$@"}
