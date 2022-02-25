# Inter Process Communication (IPC)
Copyright (c) 2020, Carnegie Mellon University  
This software is distributed under the terms of the Simplified BSD License (see [LICENSE.TXT](LICENSE.TXT))

Current Version: **3.9.1**

This repository is a mirror of the source code released at [http://www.cs.cmu.edu/~ipc/](http://www.cs.cmu.edu/~ipc/).

## Build/Install
#### For Ubuntu/Linux Variant 
To build the program, simply run `make` at the root directory. This will build the library in the source directory.  
To install the program in another location, run `make INSTALL_DIR=/path/you/want/to/install/to`

## To Run
1. Start the central server `BASE_DIR/bin/Linux-KERNAL-VERSION/central`
2. Start programs that uses IPC components.
    * You can try building and running the test programs. Navigate to the test directory and make all.
    ```
    cd test
    make 
    cd bin/Linux-KERNAL-VERSION/ipcTest1
    ```

## Documentation
An overview of the package and API documentation can be found in [IPC_Manual.pdf](doc/IPC_Manual.pdf)


## Notes on Compatibility
- **[2020-05-22]** We were able to build the central server and C library on Ubuntu 18.04. The python binding is broken and we did not test the other programming bindings.   
- **[2022-02-25]** Reverted back from 3.10.2 due to bug that needs to be tracked down (probably related to transferring raw data).


## Original README
```
Inter-Process Communications (IPC)
----------------------------------

The IPC library is a package for doing efficient, network-based inter-process
message passing.  IPC supports both publish/subscribe and client/server
paradigms.  It also provides efficient marshalling and unmarshalling of
complex data structures.  IPC is based on the communications package of the
Task Control Architecture (TCA), with extensions to support the NASA New
Millennium Program.

For a detailed description of IPC, see the programmers guide in the doc
directory.

To compile IPC, you should just have to do "gmake install" from this directory.
For more detailed instructions on compiling IPC, see the INSTALL file in the
src directory.

The current version of IPC has been run on the following machines types:

sparc running SunOs 4.1.3
sparc running Solaris
i486, i586 running Linux
SGI Personal Iris 
i486, i586 running Windows, Windows NT, and Windows 95
Macintosh, including OSX (see README.MAC)

The system should run on any machine that supports sockets and has a C
compiler.  For information in porting IPC to a new architecture, contact
Reid Simmons (reids@cs.cmu.edu).

There are several sets of "makefiles" in these directories.  The
GNUmakefiles are for use with the GNU project make (gmake).  These are
the most comprehensive makefiles.  The "Makefiles" are the most generic.
Other files can are specialized to a specific architecture, but these
often get out of date.  Try the GNUmakefiles first, then the Makefiles
and finally any other random files.

An older version of the instructions for compiling IPC is available in
README.old.  This files also contains instructions for running some of
the example test programs.  As of this time, not all the test programs
have been tested with the current version.

Richard
___\---

Copyright (c) 2008, Carnegie Mellon University
    This software is distributed under the terms of the 
    Simplified BSD License (see ipc/LICENSE.TXT)

HISTORY

$log$

```