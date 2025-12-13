# pip install beautifulsoup4
from bs4 import BeautifulSoup
import html

html_blob = """<p>#!/bin/bash
# <del>-
# See the NOTICE file distributed with this work for additional
# information regarding copyright ownership.
#
# This is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2.1 of
# the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this software; if not, write to the Free
# Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA, or see the FSF site: <span class="wikiexternallink"><a class="wikimodel-freestanding" href="http://www.fsf.org."><span class="wikigeneratedlinkcontent">http://www.fsf.org.</span></a></span>
#&nbsp;</del>-</p><p># 
# Optional ENV vars
# -
# &nbsp;&nbsp;XWIKI_OPTS - parameters passed to the Java VM when running XWiki e.g. to increase the memory allocated to the
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JVM to 1GB, use set XWIKI_OPTS=-Xmx1024m
# &nbsp;&nbsp;JETTY_OPTS - optional parameters passed to Jetty's start.jar. For example to list the configuration that will
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;execute, try setting it to "<del>list-config". See
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="wikiexternallink"><a class="wikimodel-freestanding" href="http://www.eclipse.org/jetty/documentation/current/start-jar.html"><span class="wikigeneratedlinkcontent">http://www.eclipse.org/jetty/documentation/current/start-jar.html</span></a></span> for more options.
# &nbsp;&nbsp;JETTY_PORT - the port on which to start Jetty.
# &nbsp;&nbsp;JETTY_STOP_PORT - the port on which Jetty listens for a Stop command.
#&nbsp;</del></p><p>usage() &#123;
&nbsp;&nbsp;echo "Usage: start_xwiki.sh &lt;optional parameters&gt;"
&nbsp;&nbsp;echo "-p, <del>port: The Jetty HTTP port to use. Overrides any value from JETTY_PORT. Defaults to 8080."
&nbsp;&nbsp;echo "-sp,&nbsp;</del>stopport: The Jetty stop port to use. Overrides any value from JETTY_STOP_PORT. Defaults to 8079."
&nbsp;&nbsp;echo "-ld, <del>lockdir: The directory where the executing process id is stored to verify that that only one instance"
&nbsp;&nbsp;echo " &nbsp;&nbsp;&nbsp;is started. Defaults to /var/tmp."
&nbsp;&nbsp;echo "-j,&nbsp;</del>jmx: Allows monitoring/managing Jetty through JMX."
&nbsp;&nbsp;echo "-ni, <del>noninteractive: Don't ask questions to the user. Useful when called in an automated script."
&nbsp;&nbsp;echo ""
&nbsp;&nbsp;echo "Example: start_xwiki.sh -p 8080 -sp 8079"
}</del></p><p># Ensure that the commands below are always started in the directory where this script is located.
# To do this we compute the location of the current script.
PRG="$0"
while [ -h "$PRG" ]; do
&nbsp;&nbsp;ls=`ls -ld "$PRG"`
&nbsp;&nbsp;link=`expr "$ls" : '.*-&gt; \(.*\)$'`
&nbsp;&nbsp;if expr "$link" : '/.*' &gt; /dev/null; then
&nbsp;&nbsp;&nbsp;&nbsp;PRG="$link"
&nbsp;&nbsp;else
&nbsp;&nbsp;&nbsp;&nbsp;PRG=`dirname "$PRG"`/"$link"
&nbsp;&nbsp;fi
done
PRGDIR=`dirname "$PRG"`
cd "$PRGDIR"</p><p># If no XWIKI_OPTS env variable has been defined use default values.
if [ -z "$XWIKI_OPTS" ] ; then
&nbsp;&nbsp;XWIKI_OPTS="-Xmx1024m"
fi</p><p># The port on which to start Jetty can be defined in an environment variable called JETTY_PORT
if [ -z "$JETTY_PORT" ]; then
&nbsp;&nbsp;JETTY_PORT=8080
fi</p><p># The port on which Jetty listens for a Stop command can be defined in an environment variable called JETTY_STOP_PORT
if [ -z "$JETTY_STOP_PORT" ]; then
&nbsp;&nbsp;JETTY_STOP_PORT=8079
fi</p><p># The location where to store the process id
XWIKI_LOCK_DIR="/var/tmp"</p><p># Parse script parameters
while <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20%24%23%20%3E%200%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> $# &gt; 0 </span></a></span>; do
&nbsp;&nbsp;key="$1"
&nbsp;&nbsp;shift
&nbsp;&nbsp;case $key in
&nbsp;&nbsp;&nbsp;&nbsp;-p|<del>port)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JETTY_PORT="$1"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;-sp|</del>stopport)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JETTY_STOP_PORT="$1"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;-ld|<del>lockdir)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;XWIKI_LOCK_DIR="$1"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;-j|</del>jmx)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JETTY_OPTS="$JETTY_OPTS <del>module=jmx"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;-ni|</del>noninteractive)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;XWIKI_NONINTERACTIVE=true
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;-h|<del>help)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usage
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;&nbsp;&nbsp;*)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# unknown option
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;usage
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;;
&nbsp;&nbsp;esac
done</del></p><p># Check if a lock file already exists for the specified port &nbsp;which means an XWiki instance is already running
XWIKI_LOCK_FILE="$&#123;XWIKI_LOCK_DIR}/xwiki-$&#123;JETTY_PORT}.lck"</p><p>if [ -e $XWIKI_LOCK_FILE ]; then
&nbsp;&nbsp;# Note that there could be rare cases when the computer was rebooted without Jetty stopped and when it restarted
&nbsp;&nbsp;# another process used the same process id...
&nbsp;&nbsp;if ps -p `cat $XWIKI_LOCK_FILE` &gt; /dev/null; then
&nbsp;&nbsp;&nbsp;&nbsp;echo An XWiki instance is already running on port $&#123;JETTY_PORT}. Aborting...
&nbsp;&nbsp;&nbsp;&nbsp;echo Consider calling stop_xwiki.sh to stop it.
&nbsp;&nbsp;&nbsp;&nbsp;exit 1
&nbsp;&nbsp;else
&nbsp;&nbsp;&nbsp;&nbsp;echo An XWiki lock file exists at $&#123;XWIKI_LOCK_FILE} but no XWiki is executing. Removing lock file...
&nbsp;&nbsp;&nbsp;&nbsp;rm -f $XWIKI_LOCK_FILE
&nbsp;&nbsp;fi
fi</p><p># Location where XWiki stores generated data and where database files are.
XWIKI_DATA_DIR=/var/lib/xwiki/data
XWIKI_OPTS="$XWIKI_OPTS -Dxwiki.data.dir=$XWIKI_DATA_DIR"</p><p># Catch any Out Of Memory to make easier to analyze it
XWIKI_OPTS="$XWIKI_OPTS -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=$XWIKI_DATA_DIR"</p><p># Ensure the data directory exists so that XWiki can use it for storing permanent data.
mkdir -p $XWIKI_DATA_DIR 2&gt;/dev/null</p><p># Ensure the logs directory exists as otherwise Jetty reports an error
mkdir -p $XWIKI_DATA_DIR/logs 2&gt;/dev/null</p><p># Set up the Jetty Base directory (used for custom Jetty configuration) to be the current directory where this file is.
# Also make sure the log directory exists since Jetty won't create it.
JETTY_BASE=.
mkdir -p $JETTY_BASE/logs 2&gt;/dev/null</p><p># Specify Jetty's home directory to be the directory named jetty inside the jetty base directory.
# Thus JETTY_HOME/data and JETTY_HOME/webapps are inside the jetty base directory.
JETTY_HOME=jetty
XWIKI_OPTS="$XWIKI_OPTS -Djetty.home=$JETTY_HOME -Djetty.base=$JETTY_BASE"</p><p># Specify the encoding to use
XWIKI_OPTS="$XWIKI_OPTS -Dfile.encoding=UTF8"</p><p># Specify port on which HTTP requests will be handled
JETTY_OPTS="$JETTY_OPTS jetty.http.port=$JETTY_PORT"
# In order to print a nice friendly message to the user when Jetty has finished loading the XWiki webapp, we pass
# the port we use as a System Property
XWIKI_OPTS="$XWIKI_OPTS -Djetty.http.port=$JETTY_PORT"</p><p># Specify port and key to stop a running Jetty instance
JETTY_OPTS="$JETTY_OPTS STOP.KEY=xwiki STOP.PORT=$JETTY_STOP_PORT"</p><p># Returns the Java version.
# 8 for 1.8.0_nn, 9 for 9-ea etc, and "no_java" for undetected
java_version() &#123;
&nbsp;&nbsp;local result
&nbsp;&nbsp;local java_cmd
&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20-n%20%24%28type%20-p%20java%29%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> -n $(type -p java) </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;java_cmd=java
&nbsp;&nbsp;elif <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20%28-n%20%22%24JAVA_HOME%22%29%20%26%26%20%28-x%20%22%24JAVA_HOME%2Fbin%2Fjava%22%29%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> (-n "$JAVA_HOME") &amp;&amp; (-x "$JAVA_HOME/bin/java") </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;java_cmd="$JAVA_HOME/bin/java"
&nbsp;&nbsp;fi
&nbsp;&nbsp;local IFS=$'\n'
&nbsp;&nbsp;# remove \r for Cygwin
&nbsp;&nbsp;local lines=$("$java_cmd" -Xms32M -Xmx32M -version 2&gt;&amp;1 | tr '\r' '\n')
&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20-z%20%24java_cmd%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> -z $java_cmd </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;result=no_java
&nbsp;&nbsp;else
&nbsp;&nbsp;&nbsp;&nbsp;for line in $lines; do
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20%28-z%20%24result%29%20%26%26%20%28%24line%20%3D%20*%22version%20%22%22*%29%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> (-z $result) &amp;&amp; ($line = *"version ""*) </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local ver=$(echo $line | sed -e 's/.*version "\(.*\)"\(.*\)/\1/; 1q')
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# on macOS, sed doesn't support '?'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/%20%24ver%20%3D%20%221/%22*%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent">"* </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result=$(echo $ver | sed -e 's/1\.\([0-9]*\)\(.*\)/\1/; 1q')
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result=$(echo $ver | sed -e 's/\([0-9]*\)\(.*\)/\1/; 1q')
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fi
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fi
&nbsp;&nbsp;&nbsp;&nbsp;done
&nbsp;&nbsp;fi
&nbsp;&nbsp;echo "$result"
}</p><p># Check version of Java (when in non-interactive mode)
JAVA_VERSION="$(java_version)"
if [ ! "$XWIKI_NONINTERACTIVE" = true ] ; then
&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20%22%24JAVA_VERSION%22%20-eq%20%22no_java%22%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> "$JAVA_VERSION" -eq "no_java" </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;echo "No Java found. You need Java installed for XWiki to work."
&nbsp;&nbsp;&nbsp;&nbsp;exit 0
&nbsp;&nbsp;fi
&nbsp;&nbsp;if [ "$JAVA_VERSION" -lt 11 ]; then
&nbsp;&nbsp;&nbsp;&nbsp;echo This version of XWiki requires Java 11 or greater.
&nbsp;&nbsp;&nbsp;&nbsp;exit 0
&nbsp;&nbsp;fi
&nbsp;&nbsp;if [ "$JAVA_VERSION" -gt 17 ]; then
&nbsp;&nbsp;&nbsp;&nbsp;read -p "You're using Java $JAVA_VERSION which XWiki doesn't fully support yet. Continue (y/N)? " -n 1 -r
&nbsp;&nbsp;&nbsp;&nbsp;if <span class="wikicreatelink"><a href="/xwiki/bin/create/Main/%20%21%20%24REPLY%20%3D%20%5E%5BYy%5D%24%20/WebHome?parent=Main.SolrSearch"><span class="wikigeneratedlinkcontent"> ! $REPLY = ^[Yy]$ </span></a></span>; then
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit 0
&nbsp;&nbsp;&nbsp;&nbsp;fi
&nbsp;&nbsp;fi
fi</p><p># TODO: Remove once <span class="wikiexternallink"><a class="wikimodel-freestanding" href="https://jira.xwiki.org/browse/XCOMMONS-2852"><span class="wikigeneratedlinkcontent">https://jira.xwiki.org/browse/XCOMMONS-2852</span></a></span> is fixed. In summary we need this to allow the XWiki
# code or 3rd party code to use reflection to access private variables (setAccessible() calls).
# See <span class="wikiexternallink"><a class="wikimodel-freestanding" href="https://tinyurl.com/tdhkn6mp"><span class="wikigeneratedlinkcontent">https://tinyurl.com/tdhkn6mp</span></a></span>
if [ "$JAVA_VERSION" -gt 11 ]; then
&nbsp;&nbsp;XWIKI_OPENS_LANG="<del>add-opens java.base/java.lang=ALL-UNNAMED"
&nbsp;&nbsp;XWIKI_OPENS_IO="</del>add-opens java.base/java.io=ALL-UNNAMED"
&nbsp;&nbsp;XWIKI_OPENS_UTIL="<del>add-opens java.base/java.util=ALL-UNNAMED"
&nbsp;&nbsp;XWIKI_OPENS_CONCURRENT="</del>add-opens java.base/java.util.concurrent=ALL-UNNAMED"
&nbsp;&nbsp;XWIKI_OPTS="$XWIKI_OPENS_LANG $XWIKI_OPENS_IO $XWIKI_OPENS_UTIL $XWIKI_OPENS_CONCURRENT $XWIKI_OPTS"
fi</p><p># We save the shell PID here because we do an exec below and exec will replace the shell with the executed command
# and thus the java process PID will actually be the shell PID.
XWIKI_PID=$$
echo $XWIKI_PID &gt; $XWIKI_LOCK_FILE</p><p>(
&nbsp;&nbsp;# Wait till the java process doesn't exist anymore (which will happen if the user presses crtl-c or
&nbsp;&nbsp;# if stop_xwiki.sh is called.
&nbsp;&nbsp;while :; do
&nbsp;&nbsp;&nbsp;&nbsp;# Break the loop when kill returns non 0 results, i.e. when the java process doesn't exist anymore
&nbsp;&nbsp;&nbsp;&nbsp;kill -0 $XWIKI_PID 2&gt;/dev/null || break
&nbsp;&nbsp;&nbsp;&nbsp;sleep 1
&nbsp;&nbsp;done
&nbsp;&nbsp;# Remove XWiki lock file
&nbsp;&nbsp;rm -f $XWIKI_LOCK_FILE
) &amp;</p><p># This replaces the shell with the java process without starting a new process. This must be the last line
# of this script as anything after won't be executed.
exec java $XWIKI_OPTS -jar $&#123;JETTY_HOME}/start.jar $JETTY_OPTS</p>
"""

# parse HTML and get visible text
soup = BeautifulSoup(html_blob, "html.parser")
text = soup.get_text(separator="\n")      # keep some separation between list items
xml = html.unescape(text).strip()        # convert &lt; &gt; etc to real chars

# try to extract the XML document body (between <?xml ... and </hibernate-configuration>)
import re
m = re.search(r'(<\?xml.*?</hibernate-configuration>)', xml, flags=re.DOTALL)
xml_content = m.group(1) if m else xml

print(xml_content)   # the recovered XML
# optionally write to file
with open("start_xwiki.sh", "w", encoding="utf-8") as f:
    f.write(xml_content)