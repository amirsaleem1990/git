import os
for i in ["git@github.com:amirsaleem1990/The-analytics-edge.git",
"git@github.com:amirsaleem1990/Linux.git",
"git@github.com:amirsaleem1990/short-codes.git",
"git@github.com:amirsaleem1990/important.git",
"git@github.com:amirsaleem1990/Notes.git",
"git@github.com:amirsaleem1990/Assembly-language-learning.git",
"git@github.com:amirsaleem1990/linux_youtube_downloader.git",
"git@github.com:amirsaleem1990/working.git",
"git@github.com:amirsaleem1990/Data_Cleaning.git",
"git@github.com:amirsaleem1990/R_simple_codes.git",
"git@github.com:amirsaleem1990/Wikipedia_scraping.git"]:
	os.system("git clone {}".format(i))