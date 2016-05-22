



ALTER TABLE dbo.SeekingAlpha_Articles 
ADD CreatedAt datetime NULL, UpdatedAt datetime NULL;

ALTER TABLE dbo.SeekingAlpha_Articles
ADD BodyAll varchar(max);

ALTER TABLE dbo.SeekingAlpha_Articles
ADD ArticleNumber bigint NULL

ALTER TABLE dbo.SeekingAlpha_Articles
ADD ArticleUrl varchar(max) NULL


SELECT TOP 100 * FROM dbo.SeekingAlpha_Articles

TRUNCATE TABLE dbo.SeekingAlpha_Articles

ALTER TABLE dbo.SeekingAlpha_Articles ADD UNIQUE (ArticleNumber)