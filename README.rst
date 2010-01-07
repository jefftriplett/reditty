=======
RedItty
=======

RedItty is a REST-based application that integrates with Itty and Redis.  Basically a port of ``redbottle`` (http://github.com/tnm/redbottle/) to Itty


Install and Configure
---------------------

RedItty depends on [Itty](http://github.com/toastdriven/itty "Itty"), [Redis](http://code.google.com/p/redis/ "Redis"), and the [Python interface](http://github.com/andymccurdy/redis-py/ "Python Interface") for Redis.

If you have those installed, start your Redis server. Then:

`python reditty_web.py` 

and the RedItty application will start on localhost.


Add/Remove/Show Key-Value Pairs
-------------------------------

Let's say you want to add a key-value pair with the number '2' as a key and the name 'John' as its value.
It's as easy as utilizing POST at:

> **/keyvalue/**

That saves it to the Redis data store. You can utilize delete functionality there as well. 

To show the value of any key:

> **/keyvalue/show/[key]**


Thanks to Ted Nyman for the inspiration.  I've been looking for an excuse to play with Itty and Redis for some time and this gave me an excuse to dive in.

:author: Jeff Triplett - @webology
:date: 2010-01-05


MIT License
-----------

 Copyright (c) 2010 Jeff Triplett

 Copyright (c) 2010 Ted Nyman

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
