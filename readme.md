Readme: UK Government Organograms
==========

Crawls the UK Government Linked Data API for organogram and pay data.

Saves to csv, alternatively to SQLite (for scraperwiki portability)

Sources of data
-------
* see UI at http://data.gov.uk/organogram/ - bottom right 'Sources' button explains what calls
	are being made to build the organogram
* scraper works on API at http://reference.data.gov.uk/

Scope of data
-------
* four levels down
* junior posts (with not further details) as well as SCS reporting posts
* can specify the departments to get and the timepoint for each department (there are currently 3 timepoints)
* for each non-junior job, gets the info, the reporting posts, and the statistics
* for junior jobs, gets the label/position, profession, report-to, job title, in-unit bits

Policy context/things to watch for
---------
* According to Open Data White Paper (July 2012, http://data.gov.uk/sites/default/files/Open_data_White_Paper.pdf),
	API principles should be delivered as part of the Developer Engagement Strategy
* According to Gov ICT Strategy SIP (http://www.cabinetoffice.gov.uk/content/government-ict-strategy-strategic-implementation-plan#17app)
	a review should have been done in March 2011, Common API Standard should be in place in July 12, and an API list should be published
	in September 2012

Scraperwiki version
---------
The Scraperwiki version is at https://scraperwiki.com/scrapers/uk_government_organograms/

Mirrored manually, so not always up to date.