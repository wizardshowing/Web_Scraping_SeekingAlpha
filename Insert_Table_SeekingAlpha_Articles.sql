BEGIN
IF NOT EXISTS (SELECT * FROM dbo.SeekingAlpha_Articles
WHERE Title = 'Apple: Buffett Wants Its Stock To Drop' AND Name='Feria Investor')
BEGIN
INSERT dbo.SeekingALpha_Articles (Title, Date, Time, TickersAbout, TickersIncludes,
	Name, NameLink, Bio, Summary, ImageDummy, BodyContent, Disclosure, Position, CreatedAt, UpdatedAt) 
	VALUES ('test', '2000-01-01','11:11:11','test', 'test', 'test', 'test', 'test', 'test', 1, 'test', 'test', 'test', null, null)
END
END

SELECT *
FROM dbo.SeekingAlpha_Articles
WHERE Title = '3M: Emerging Markets Is The Focus'
ORDER BY ArticleID


