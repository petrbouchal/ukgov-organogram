Readme: UK Government Organograms
==========

Crawls the UK Government Linked Data API for organogram and pay data.

Saves to csv, alternatively to SQLite (for scraperwiki portability)

Sources of data
-------
* see UI at http://data.gov.uk/organogram/ - bottom right 'Sources' button explains what calls
	are being made to build the organogram
* scraper uses API at http://reference.data.gov.uk/

Scope of data
-------
* four levels down
* junior posts (with no further details other than pay, grade, FTE count) as well as SCS reporting posts
* can specify the departments to get and the timepoint for each department (there are currently 3 timepoints available)
* for each non-junior job, gets the basic position info, the reporting posts, and the statistics
* for junior jobs, gets the label/position, profession, report-to, job title, information on what unit that job belongs to

Mechanics
--------
1. gets top job (Perm Sec) - URL constructed per department
2. gets information on top job
3. gets statistical data on top job
4. gets list of non-junior posts reporting to top job 
5. gets list of junior posts reporting directly to top job
6. gets basic data on posts listed in 5
7. repeats 2-6 for each non-junior post reporting to top post, as gathered in 4
8. repeat for next level down

Policy context/things to watch for
---------
* According to Open Data White Paper (July 2012, http://data.gov.uk/sites/default/files/Open_data_White_Paper.pdf),
	API principles should be delivered as part of the Developer Engagement Strategy
* According to Gov ICT Strategy SIP (http://www.cabinetoffice.gov.uk/content/government-ict-strategy-strategic-implementation-plan#17app)
	a review should have been done in March 2011; Common API Standard should be in place in July 2012, and an API list should be published
	in September 2012

Scraperwiki version
---------
The Scraperwiki version is at https://scraperwiki.com/scrapers/uk_government_organograms/

The code is mirrored manually form here to ScraperWiki, so the SW version is not always up to date.
The stable link to the CSV output of the result of the last run at ScraperWiki is [TODO: fill this in]