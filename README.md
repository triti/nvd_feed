# nvd_feed
Collects NIST's vulnerability feed, parses it, and sends it out to stdout.

This is intended to be used with a Sumo Logic collector as a script source. It's very basic and does pretty much no error checking. It depends on the [Requests](http://docs.python-requests.org/en/master/) library to be installed.
