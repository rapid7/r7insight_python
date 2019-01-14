Rapid7 Insight Logger
=====================

This is a plugin library to enable logging to Rapid7 Insight from the Python Logger.
Additionally this plugin allows the user to get an overview of methods being executed,
their execution time, as well as CPU and Memory statistics.
More info at https://www.rapid7.com/solutions/it-operations/. Note that this plugin is
**asynchronous**.

Setup
-----

To use this library, you must first create an account on Rapid7 Insight.
This will only take a few moments.

Install
-------

To install this library, use the following command:

``pip install r7insight_python``

Usage
-----

.. code-block:: python

    #!/usr/bin/env python

    import logging
    from r7insight import R7InsightHandler


    log = logging.getLogger('r7insight')
    log.setLevel(logging.INFO)
    test = R7InsightHandler(TOKEN, REGION)

    log.addHandler(test)

    log.warn("Warning message")
    log.info("Info message")

    sleep(10)


Usage with metric functionality
-------------------------------

.. code-block:: python

    import time
    import logging
    from r7insight import R7InsightHandler, metrics


    TEST = metrics.Metric(TOKEN, REGION)

    @TEST.metric()
    def function_one(t):
        """A dummy function that takes some time."""
        time.sleep(t)

    if __name__ == '__main__':
            function_one(1)


Metric.Time()
-------------

This decorator function is used to log the execution time of given function. In the above example ``@TEST.time()`` will wrap ``function_one`` and send log message containing the name and execution time of this function.



Configure
---------

The parameter ``TOKEN`` needs to be filled in to point to a
file in your Insight account.

The parameter ``REGION`` needs to be filled with the region your log is located in. i.e: 'eu', 'us'

In your R7Insight account, create a logfile, selecting ``Token TCP`` as
the source\_type. This will print a Token UUID. This
is the value to use for ``TOKEN``.

The appender will attempt to send your log data over TLS over port 443,
otherwise it will send over port 80.

You are now ready to start logging

Contact Support
===============

Please email our support team at support@rapid7.com if you need any help.
