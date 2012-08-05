Readme: UK Government Organograms
==========

Crawls the UK Government Linked Data API for organogram and pay data.

Saves to csv, alternatively to SQLite (for scraperwiki portability)

Sources of data

Scope of data
-------
* four levels down
* junior posts (with not further details) as well as SCS reporting posts
* can specify the departments to get and the timepoint for each department (there are currently 3 timepoints)
* for each non-junior job, gets the info, the reporting posts, and the statistics
* for junior jobs, gets the label/position, profession, report-to, job title, in-unit bits

Scraperwiki version
---------
The Scraperwiki version is at https://scraperwiki.com/scrapers/uk_government_organograms/
Mirrored manually, so not always up to date.