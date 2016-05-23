USE [SeekingAlpha]
GO

/****** Object:  Table [dbo].[SeekingAlpha_Articles]    Script Date: 24/05/2016 10:23:11 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[SeekingAlpha_Articles](
	[ArticleID] [bigint] IDENTITY(1,1) NOT NULL,
	[Title] [nvarchar](max) NOT NULL,
	[Date] [date] NOT NULL,
	[Time] [time](7) NOT NULL,
	[TickersAbout] [nvarchar](max) NOT NULL,
	[TickersIncludes] [nvarchar](max) NULL,
	[Name] [nvarchar](max) NULL,
	[NameLink] [nvarchar](max) NULL,
	[Bio] [nvarchar](max) NULL,
	[Summary] [nvarchar](max) NULL,
	[ImageDummy] [int] NULL,
	[BodyContent] [nvarchar](max) NULL,
	[Disclosure] [nvarchar](max) NULL,
	[Position] [nvarchar](max) NULL,
	[CreatedAt] [datetime] NULL,
	[UpdatedAt] [datetime] NULL,
	[BodyAll] [varchar](max) NULL,
	[ArticleNumber] [bigint] NULL,
	[ArticleUrl] [varchar](max) NULL,
UNIQUE NONCLUSTERED 
(
	[ArticleNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

GO

SET ANSI_PADDING OFF
GO


