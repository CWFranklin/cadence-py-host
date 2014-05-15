Cadence Host
==========

A Python script developed to report server status and statistics back to the Cadence API.
------------------------------------------------------

Built using Nano over SSH on an Ubuntu VM running on Azure. Because.

Contributing
------------

Contributors are very welcome! If you have code fixes, please [submit a pull request][newpull] here on GitHub.

If you want to join the development team, please contact [brandonscott][bs] on GitHub.

All authors and contributors are listed in the **AUTHORS** file.

Please read the wiki page about [contributing][contrib] before submitting pull requests.

License
-------

Copyright &copy; 2014 by [Brandon Scott][bs] and [Chris Franklin][cwf].

This project is licensed under the GNU General Public license, please see the file **LICENSE** for more information.
 
All other trademarks are property of their respective owners.

Dependencies
------------

The Cadence Host is built to run on Python3 and was developed using Pyhton 3.4. (https://www.python.org/download/releases/3.0).

The Python3 dependencies are:
 * PsUtil
 * PyCrypto
 * PyOpenSSL
 * Requests
 * UrlLib3

Building
--------

Ensure Python3 is installed before running the install bash file.
Run 'python3 main.py'.

Debugging / Logging
-------------------


Related Repos
--------

Projects associated with this repository:

 * [Cadence (API)][capi]
 * [Cadence C# Host][cshost]
 * [Cadence Service][csrv]
 * [Pulse (Android App)][pulse]

 
[bs]: https://github.com/brandonscott
[capi]: https://github.com/brandonscott/cadence
[contrib]: ../../wiki/Contributing
[cshost]: https://github.com/brandonscott/cadence-host
[csrv]: https://github.com/brandonscott/cadence-service
[cwf]: https://github.com/cwfranklin
[pulse]: https://github.com/brandonscott/pulse