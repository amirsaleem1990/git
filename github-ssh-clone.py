import os
base = "git@github.com:amirsaleem1990/"
for i in [
"The-analytics-edge.git",
"Linux.git",
"short-codes.git",
"important.git",
"Notes.git",
"Assembly-language-learning.git",
"linux_youtube_downloader.git",
"working.git",
"Data_Cleaning.git",
"R_simple_codes.git",
"Wikipedia_scraping.git"
]:
	os.system("git clone {}{}".format(base, i))
