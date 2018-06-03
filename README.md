# Youtube_Thumbnail_Downloader

Download, then resize, then crop Youtube Video Thumbnails, by simply providing URL list of the videos in a txt file, named 'ID.txt'.
You have to place URL of videos in each new line without any spaces.

This will download 1280 * 720 image, then resize it to the cofiguration specified (900 * 600 by default),
then crop 500*500 middle portion of image



NOTE:	If possible url should be like 'https://www.youtube.com/watch?v=wArETCVkS4g'
		It should not be like 'https://www.youtube.com/watch?v=wArETCVkS4g&eohoeht?eueu',
		in this case and others, only part before '&' is useful

-------------------------------------------------------------------------------

How to manully download thumbnail of video using video ID.(Only if you are intrested in the script's working)

Replace "VIDEOID" with your selected video's ID number!

*For YouTube's Auto-Generated Thumbnails*

Thumbnail 1 [120x90] http://img.youtube.com/vi/VIDEOID/1.jpg

Thumbnail 2 [120x90] http://img.youtube.com/vi/VIDEOID/2.jpg

Thumbnail 3 [120x90] http://img.youtube.com/vi/VIDEOID/3.jpg

*For Custom thumbnails*

Small thumbnail [320x180] https://img.youtube.com/vi/VIDEOID/mqdefault.jpg

Medium thumbnail [480x360] http://img.youtube.com/vi/VIDEOID/0.jpg

Large thumbnail [1280x720 or 1920x1080] https://img.youtube.com/vi/VIDEOID/maxresdefault.jpg


