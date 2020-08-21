# DhanishandSamRepo
GES JGSA;GAWNGNJAGI

#Read Me!

##Using index.php

To connect directly to the index.php page you will need to change a config from the apache server.

Edit the file:
'''
/etc/httpd/conf/httpd.conf
'''

Change the section:
'''
<IfModule dir_module>
    DirectoryIndex index.html
</IfModule>
'''
To:
'''
<IfModule dir_module>
    DirectoryIndex index.html index.php
</IfModule>
'''
This will make the server try and send you to index.html, if thats not possible you will be sent to index.php
Doing it this way allows you to quickly put up a html mask page to stop users from being sent to a broken php page.
