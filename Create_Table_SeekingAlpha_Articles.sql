--The query was not working when I first tried, then I added "CREATE SCHEMA SeekingAlpha" and it's working now.
--Table design: Title, Date, Time, TickersAbout, TickersIncludes, Name, NameLink, Bio, Summary
--, ImageDummy, BodyContent, Disclosure, Position 
CREATE SCHEMA SeekingAlpha
CREATE TABLE SeekingAlpha.Articles(
	ArticleID bigint IDENTITY(1,1) NOT NULL,
	Title nvarchar(max) NOT NULL,
	Date date NOT NULL,
	Time time NOT NULL,
	TickersAbout nvarchar(max) NOT NULL,
	TickersIncludes nvarchar(max) NULL,
	Name nvarchar(max) NULL,
	NameLink nvarchar(max) NULL,
	Bio nvarchar(max) NULL,
	Summary nvarchar(max) NULL,
	ImageDummy int NULL,
	BodyContent nvarchar(max) NULL,
	Disclosure nvarchar(max) NULL,
	Position nvarchar(max) NULL

)