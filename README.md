# A collection of spec files

Sometimes we need a rpm and can't find it elsewhere. Here is our
collection of spec files. Provided without any warranty.

## Projects

-  forever.spec builds [node-forever](https://github.com/nodejitsu/forever/)

## How-to

The *Source0* directive is defined in a spectool compatible way. This means that all you need to build
an RPM is the following:

- spectool -g -R <specfile.spec>
- rpmbuild -ba <specfile>

If you are missing the command line tools, install the package 'rpmbuild' and 'rpmdevtools'

#### License: MIT
#### Authors: 
- [Laurent Eschenauer](http://github.com/eschnou)

