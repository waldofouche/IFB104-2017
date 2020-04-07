
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9950095
#    Student name: Waldo Fouche
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################

#--------------------- TKinter window setup-----------------------------#

# Program built on Windows 10

# Create a window
window = Tk()

# Give the window a title
window.title('Wall Street Journal News Archive')

# Set the window's size
window.geometry('800x600')

# Make window background colour white
window['bg'] = '#757575'

# Disables maximum mode
window.resizable(0, 0)

# Frames
archives_frame = Frame(window, borderwidth=1, relief='solid')
archives_frame.place(relx=0.025, rely=0.42, width=376)

# Current Action Messenger
standard = 'Select a date..'
extract = 'News extraction completed succesfully.'
downloading = 'Downloading latest archive..'
displaying_webpage = 'Extracted news being displayed.'
display_error = "Error!: Webpage open Failed."
error = 'Error: News file not found!'
extract_fail = "Archive Extraction Failure."
#-------------------------------------------------------------------------#

#-------------------------- HTML setup -----------------------------------#

# HTML template, with blanks marked by asterisks
html_template = """<!DOCTYPE html>
<html lang="en">

<head>
  <title>Wall Street Journal Archive</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    /* Style the text elements */

    body {
      background-color: white;
      color: #616161;
    }

    p {
      width: 80%;
      margin-left: auto;
      margin-right: auto;
      text-align: left;
      font-family: "Times"
    }

    h1 {
      width: 80%;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      font-family: "Times";
      font-size: 3em
    }

    h2 {
      width: 80%;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      font-family: "Times";
      font-size: 2em
    }

    h3 {
      width: 80%;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      font-family: "Times";
      font-size: 1.5em
    }

    hr {
      border-style: solid;
      margin-top;
      lem;
      margin-bottom: lem
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
    }

    /* Style the side navigation */

    .sidenav {
      height: 100%;
      width: 200px;
      position: fixed;
      z-index: 1;
      top: 0;
      left: 0;
      background-color: #212121;
      overflow-x: hidden;
    }


    /* Side navigation links */

    .sidenav a {
      color: white;
      padding: 16px;
      text-decoration: none;
      display: block;
    }

    /* Change color on hover */

    .sidenav a:hover {
      background-color: #E0E0E0;
      color: black;
    }

    /* Style the content */

    .content {
      margin-left: 200px;
      padding-left: 20px;
    }
  </style>
</head>

    <body>

      <div class="sidenav">
        <!-- navigation links -->
        <p style="color: #FFFFFF;">***SUBTITLE***</p>
        <a href="#Home">Home</a>
        <a href="#***HEADLINE_1***">Article 1</a>
        <a href="#***HEADLINE_2***">Article 2</a>
        <a href="#***HEADLINE_3***">Article 3</a>
        <a href="#***HEADLINE_4***">Article 4</a>
        <a href="#***HEADLINE_5***">Article 5</a>
        <a href="#***HEADLINE_6***">Article 6</a>
        <a href="#***HEADLINE_7***">Article 7</a>
        <a href="#***HEADLINE_8***">Article 8</a>
        <a href="#***HEADLINE_9***">Article 9</a>
        <a href="#***HEADLINE_10***">Article 10</a>
      </div>

      <div class="content">

        <!-- Page Heading and Brand Image -->
        <a name="Home">
          <h1> Wall Street Journal Archive </h1>
          <h4 style="text-align: center">***SUBTITLE***</h4>

          <p style="text-align:center"><img src="http://www.dianneblomberg.com/wp-content/uploads/2016/11/wallstreetjournal-logo.png" alt="Image not found!" height="100%" width="100%" style="border: white 1px solid"></p>
          <p><strong>News source: </strong><a href="http://www.wsj.com/xml/rss/3_7085.xml">http://www.wsj.com/xml/rss/3_7085.xml</a>
            <br><strong>Archivist:</strong> Waldo Fouche </br>
          </p>
          <hr width="80%" size=5 px>

          <!-- Headline 1 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_1***"></a>
          <h3>1. ***HEADLINE_1***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_1***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_1***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_1***">***SOURCE_1***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_1*** </br>
           </p>

          <hr width="80%" size=5 px>

          <!-- Headline 2 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_2***"></a>
          <h3>2. ***HEADLINE_2***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_2***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_2***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_2***">***SOURCE_2***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_2*** </br>
          </p>

          <hr width="80%" size=5 px>

          <!-- Headline 3 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_3***"></a>
          <h3>3. ***HEADLINE_3***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_3***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_3***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***IMAGE_4***">***SOURCE_3***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_3*** </br>
          </p>

          <hr width="80%" size=5 px>
          <!-- Headline 4 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_4***"></a>
          <h3>4. ***HEADLINE_4***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_5***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_4***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_4***">***SOURCE_4***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_4*** </br>
          </p>

          <hr width="80%" size=5 px>
              
          <!-- Headline 5 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_5***"></a>
          <h3>5. ***HEADLINE_5***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_6***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_5***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_5***">***SOURCE_5***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_5*** </br>
          </p>

          <hr width="80%" size=5 px>
              
          <!-- Headline 6 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_6***"></a>
          <h3>6. ***HEADLINE_6***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_7***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_6***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_6***">***SOURCE_6***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_6*** </br>
          </p>
              
          <hr width="80%" size=5 px>

          <!-- Headline 7 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_7***"></a>
          <h3>7. ***HEADLINE_7***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_8***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_7***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_7***">***SOURCE_7***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_7*** </br>
          </p>

          <hr width="80%" size=5 px>

          <!-- Headline 9 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_8***"></a>
          <h3>8. ***HEADLINE_8***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_8***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_8***</p>
              <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_8***">***SOURCE_8***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_8*** </br>
          </p>

          <hr width="80%" size=5 px>

          <!-- Headline 9 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_9***"></a>
          <h3>9. ***HEADLINE_9***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_9***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_9***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_9***">***SOURCE_9***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_9*** </br>
          </p>

              <hr width="80%" size=5 px>
          <!-- Headline 10 -->
          <!-- Anchor Link -->
          <a name="***HEADLINE_10***"></a>
          <h3>10. ***HEADLINE_10***</h3>
          <!-- Article Image -->
          <p style="text-align:center"><img src="***IMAGE_10***" alt="Image not found!" height="100%" width="100%" style="border: black 1px solid;" />
          <!-- Story -->
          <p>***DESCRIPTION_10***</p>
          <!-- Source link -->
          <p><strong>Full story:</strong> <a href="***SOURCE_10***">***SOURCE_10***</a>
          <!-- Date of publication -->
          <br><strong>Date Published:</strong> ***DATE_10*** </br>
          </p>

              <hr width="80%" size=5 px>

      </div>

    </body>

</html>
"""

# Radiobutton Indicatoron
MODES = [
        ("11th October, 2017", "InternetArchive/WSJ_11-10-17"),
        ("12th October, 2017", "InternetArchive/WSJ_12-10-17"),
        ("13th October, 2017", "InternetArchive/WSJ_13-10-17"),
        ("14th October, 2017", "InternetArchive/WSJ_14-10-17"),
        ("16th October, 2017", "InternetArchive/WSJ_16-10-17"),
        ("17th October, 2017", "InternetArchive/WSJ_17-10-17"),
        ("23rd October, 2017", "InternetArchive/WSJ_23-10-17"),
        ("Latest", "InternetArchive/Latest")
    ]

v = StringVar()
v.set("InternetArchive/Latest")  # initialize

# If radiobutton equals the selected date's value
def archive_selector():
    try:
        if MODES[0][1] == v.get():
            archive = open('InternetArchive/WSJ_11-10-17.xhtml','r', encoding = 'UTF-8')
            messenger.config(text = MODES[0][0])
        elif MODES[1][1] == v.get():
            archive = open('InternetArchive/WSJ_12-10-17.xhtml','r',encoding = 'UTF-8')
            messenger.config(text = MODES[1][0])
        elif MODES[2][1] == v.get():
             archive = open('InternetArchive/WSJ_13-10-17.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[2][0])
        elif MODES[3][1] == v.get():
             archive = open('InternetArchive/WSJ_14-10-17.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[3][0])
        elif MODES[4][1] == v.get():
             archive = open('InternetArchive/WSJ_16-10-17.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[4][0])
        elif MODES[5][1] == v.get():
             archive = open('InternetArchive/WSJ_17-10-17.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[5][0])
        elif MODES[6][1] == v.get():
             archive = open('InternetArchive/WSJ_23-10-17.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[6][0])
        elif MODES[7][1] == v.get():
             archive = open('InternetArchive/Latest.xhtml','r',encoding = 'UTF-8')
             messenger.config(text = MODES[7][0])
    except FileNotFoundError:
        messenger.config(text = file_error)

for text, mode in MODES:
    b = Radiobutton(archives_frame, text=text, variable=v, value=mode,
                    indicatoron=0, width=30, anchor=W, selectcolor='#757575',
                    bg='#212121', fg='white', font=('Times', 18, 'bold'),
                    borderwidth=0, command=archive_selector).pack()

# Defining Buttons Functions

# Raw XHTML file from the internet archive is converted into
# a HTML file with 10 stories included within. Each story has an Image,
# Heading, Description, Date Published and Link to source


# Using regex, extracts infromation from the xhtml in selected archive
# date of RSS feed
subtitle_tag = '<lastBuildDate>(.*)</lastBuildDate>'
# headlines
headline_tag = '<title>(.*)</title>'
# images
image_tag = 'url="(.*?)"'
# descriptions
desrciption_tag ='<description>(.*)</description>'
# source URL
source_tag = '<link>(.*)</link>'
# Date of publication
date_tag = '<pubDate>(.*)</pubDate>'
        
def xhtml_extract():
    try:
        # Initial conditions
        archive = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        if v.get() == "InternetArchive/WSJ_11-10-17.xhtml":
            subtitle = "11th October 2017"
        elif v.get() == "InternetArchive/WSJ_12-10-17.xhtml":
            subtitle = "12th October 2017"
        elif v.get() == "InternetArchive/WSJ_13-10-17.xhtml":
            subtitle = "S13th October 2017"
        elif v.get() == "InternetArchive/WSJ_14-10-17.xhtml":
            subtitle = "15th October 2017"
        elif v.get() == "InternetArchive/WSJ_16-10-17.xhtml":
            subtitle = "16th October 2017"
        elif v.get() == "InternetArchive/WSJ_17-10-17.xhtml":
            subtitle = "17th October 2017"
        elif v.get() == "InternetArchive/WSJ_23-10-17.xhtml":
            subtitle = "23rd October 2017"
        elif v.get() == "InternetArchive/Latest":
            subtitle = "Latest Update"      

        #----------------------------- Subtitle -----------------------------#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        subtitle = findall(subtitle_tag, xhtml_file.read())[0]

        #--------------------------- News Story 1 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_1 = findall(headline_tag, xhtml_file.read())[2]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_1 = findall(image_tag, xhtml_file.read())[0]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_1 = findall(desrciption_tag, xhtml_file.read())[1]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_1 = findall(source_tag, xhtml_file.read())[2]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_1 = findall(date_tag, xhtml_file.read())[0]
		
	#--------------------------- News Story 2 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_2 = findall(headline_tag, xhtml_file.read())[3]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_2 = findall(image_tag, xhtml_file.read())[1]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_2 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_2 = findall(source_tag, xhtml_file.read())[3]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_2 = findall(date_tag, xhtml_file.read())[1]
		
	#--------------------------- News Story 3 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_3 = findall(headline_tag, xhtml_file.read())[4]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_3 = findall(image_tag, xhtml_file.read())[2]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_3 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_3 = findall(source_tag, xhtml_file.read())[4]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_3 = findall(date_tag, xhtml_file.read())[2]
		
	#--------------------------- News Story 4 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_4 = findall(headline_tag, xhtml_file.read())[5]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_4 = findall(image_tag, xhtml_file.read())[3]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_4 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_4 = findall(source_tag, xhtml_file.read())[5]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_4 = findall(date_tag, xhtml_file.read())[3]
		
	#--------------------------- News Story 5 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_5 = findall(headline_tag, xhtml_file.read())[6]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_5 = findall(image_tag, xhtml_file.read())[4]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_5 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_5 = findall(source_tag, xhtml_file.read())[6]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_5 = findall(date_tag, xhtml_file.read())[4]
		
	#--------------------------- News Story 6 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_6 = findall(headline_tag, xhtml_file.read())[7]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_6 = findall(image_tag, xhtml_file.read())[5]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_6 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_6 = findall(source_tag, xhtml_file.read())[7]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_6 = findall(date_tag, xhtml_file.read())[5]
		
	#--------------------------- News Story 7 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_7 = findall(headline_tag, xhtml_file.read())[8]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_7 = findall(image_tag, xhtml_file.read())[6]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_7 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_7 = findall(source_tag, xhtml_file.read())[8]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_7 = findall(date_tag, xhtml_file.read())[6]
		
	#--------------------------- News Story 8 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_8 = findall(headline_tag, xhtml_file.read())[9]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_8 = findall(image_tag, xhtml_file.read())[7]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_8 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_8 = findall(source_tag, xhtml_file.read())[9]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_8 = findall(date_tag, xhtml_file.read())[7]
		
	#--------------------------- News Story 9 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_9 = findall(headline_tag, xhtml_file.read())[10]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_9 = findall(image_tag, xhtml_file.read())[8]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_9 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_9 = findall(source_tag, xhtml_file.read())[10]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_9 = findall(date_tag, xhtml_file.read())[8]
		
	#--------------------------- News Story 10 ---------------------------#
        # Extracts headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_10 = findall(headline_tag, xhtml_file.read())[11]

        # Extracts image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_10 = findall(image_tag, xhtml_file.read())[9]

        # Excracts description
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        description_10 = findall(desrciption_tag, xhtml_file.read())[3]

        # Extracts news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_10 = findall(source_tag, xhtml_file.read())[11]

        # Extracts date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_10 = findall(date_tag, xhtml_file.read())[9]  
                
        #-------------------------- Updates Template -------------------------#
        # Adds the date of the news
        html_code = html_template.replace('***SUBTITLE***', subtitle)
        
        # Replace the blanks for story 1
        html_code = html_code.replace('***HEADLINE_1***', headline_1)
        html_code = html_code.replace('***IMAGE_1***', image_1)
        html_code = html_code.replace('***DESCRIPTION_1***', description_1)
        html_code = html_code.replace('***SOURCE_1***', source_1)
        html_code = html_code.replace('***DATE_1***', date_1)
		
	# Replace the blanks for story 2
        html_code = html_code.replace('***HEADLINE_2***', headline_2)
        html_code = html_code.replace('***IMAGE_2***', image_2)
        html_code = html_code.replace('***DESCRIPTION_2***', description_2)
        html_code = html_code.replace('***SOURCE_2***', source_2)
        html_code = html_code.replace('***DATE_2***', date_2)
		
	# Replace the blanks for story 3
        html_code = html_code.replace('***HEADLINE_3***', headline_3)
        html_code = html_code.replace('***IMAGE_3***', image_3)
        html_code = html_code.replace('***DESCRIPTION_3***', description_3)
        html_code = html_code.replace('***SOURCE_3***', source_3)
        html_code = html_code.replace('***DATE_3***', date_3)
		
	# Replace the blanks for story 4
        html_code = html_code.replace('***HEADLINE_4***', headline_4)
        html_code = html_code.replace('***IMAGE_4***', image_4)
        html_code = html_code.replace('***DESCRIPTION_4***', description_4)
        html_code = html_code.replace('***SOURCE_4***', source_4)
        html_code = html_code.replace('***DATE_4***', date_4)
		
	# Replace the blanks for story 5
        html_code = html_code.replace('***HEADLINE_5***', headline_5)
        html_code = html_code.replace('***IMAGE_5***', image_5)
        html_code = html_code.replace('***DESCRIPTION_5***', description_5)
        html_code = html_code.replace('***SOURCE_5***', source_5)
        html_code = html_code.replace('***DATE_5***', date_5)
		
	# Replace the blanks for story 6
        html_code = html_code.replace('***HEADLINE_6***', headline_6)
        html_code = html_code.replace('***IMAGE_6***', image_6)
        html_code = html_code.replace('***DESCRIPTION_6***', description_6)
        html_code = html_code.replace('***SOURCE_6***', source_6)
        html_code = html_code.replace('***DATE_6***', date_6)
		
	# Replace the blanks for story 7
        html_code = html_code.replace('***HEADLINE_7***', headline_7)
        html_code = html_code.replace('***IMAGE_7***', image_7)
        html_code = html_code.replace('***DESCRIPTION_7***', description_7)
        html_code = html_code.replace('***SOURCE_7***', source_7)
        html_code = html_code.replace('***DATE_7***', date_7)
		
	# Replace the blanks for story 8
        html_code = html_code.replace('***HEADLINE_8***', headline_8)
        html_code = html_code.replace('***IMAGE_8***', image_8)
        html_code = html_code.replace('***DESCRIPTION_8***', description_8)
        html_code = html_code.replace('***SOURCE_8***', source_8)
        html_code = html_code.replace('***DATE_8***', date_8)
		
    	# Replace the blanks for story 9
        html_code = html_code.replace('***HEADLINE_9***', headline_9)
        html_code = html_code.replace('***IMAGE_9***', image_9)
        html_code = html_code.replace('***DESCRIPTION_9***', description_9)
        html_code = html_code.replace('***SOURCE_9***', source_9)
        html_code = html_code.replace('***DATE_9***', date_9)
		
    	# Replace the blanks for story 10
        html_code = html_code.replace('***HEADLINE_10***', headline_10)
        html_code = html_code.replace('***IMAGE_10***', image_10)
        html_code = html_code.replace('***DESCRIPTION_10***', description_10)
        html_code = html_code.replace('***SOURCE_10***', source_10)
        html_code = html_code.replace('***DATE_10***', date_10)

        #---------------------------- Writes html ----------------------------#
        # Writes the generated HTML code to a file called WSJ.html
        html_file = open('WSJ.html', 'w')
        html_file.write(html_code)
        html_file.close()
        # Display message
        messenger.config(text = extract)
        
    except FileNotFoundError:
        messenger.config(text = extract_fail)
		
    # If Event logger is activated and latest downloaded:
    try:
        if check.get() == 1:
            connection = connect(database= 'event_log.db')
            log_db = connection.cursor()
            event_executed = log_events[1]
            sql_query = sqlite3_template.replace('EVENT' , event_executed)
            log_db.execute (sql_query)
            connection.commit()
    except:
        messenger.config(text = sqlite3_error)
       #-----------------------------------------------------------------------#

# Displays the extracted news
def display_news():
    location = normpath('\WSJ.html')
    path = getcwd()
    fullpath = path + location
    # import exists from os.path
    from os.path import exists
    if exists(fullpath):
        webopen('file://' + fullpath)
        messenger.config(text=displaying_webpage)
    else:
        messenger.config(text=display_error)
        
    # If Event logger is activated and news displayed:
    try:
        if check.get() == 1:
                connection = connect(database= 'event_log.db')
                log_db = connection.cursor()
                event_executed = log_events[3]
                sql_query = sqlite3_template.replace('EVENT' , event_executed)
                log_db.execute (sql_query)
                connection.commit()
    except:
        messenger.config(text = sqlite3_error)

# Download 'Latest' archive
def latest():
    # Web address to download from
    url = 'http://www.wsj.com/xml/rss/3_7085.xml'

    # Open the web document for reading
    latest_archive = urlopen(url)

    # Read its contents as a Unicode string
    latest_archive_contents = latest_archive.read().decode('UTF-8')

    # Write the contents to a text file and overwriting the file if it
    # already exists)
    html_file = open('InternetArchive/latest.xhtml', 'w', encoding='UTF-8')
    html_file.write(latest_archive_contents)
    html_file.close()

    # Display message
    messenger.config(text=downloading)
	
    # If Event logger is activated and latest downloaded:
    try:
        if check.get() == 1:
                connection = connect(database= 'event_log.db')
                log_db = connection.cursor()
                event_executed = log_events[2]
                sql_query = sqlite3_template.replace('EVENT' , event_executed)
                log_db.execute (sql_query)
                connection.commit()
    except:
        messenger.config(text = sqlite3_error)

#-----------------------TKinter GUI CONT.d ---------------------------------------#

# Extract News Button
extract_button = Button(window, text='Extract news from archive',
                        font=('Times', 14), fg='white', bg='#212121',
                        relief='solid', command=xhtml_extract)

extract_button.place(relx=0.515, rely=0.82, height=60, width=120)
extract_button.configure(wraplength='120')

# Display News Button
display_button = Button(window, text='Display news extracted',
                        font=('Times', 14), fg='white', bg='#212121',
                        relief='solid', command=display_news)

display_button.place(relx=0.675, rely=0.82, height=60, width=120)
display_button.configure(wraplength='120')

# Archive News Button
archive_button = Button(window, text='Archive the latest news',
                        font=('Times', 14), fg='white', bg='#212121',
                        relief='solid', command=latest)

archive_button.place(relx=0.835, rely=0.82, height=60, width=120)
archive_button.configure(wraplength='120')

# Gui Messenger label (Text which informs user of programs current task)
messenger = Label(window, text = standard, bg='#757575', fg='black',
            font = ('Times', 22))
messenger.place(relx=0.75, rely=0.65, anchor='center')
messenger.configure(wraplength='260')

# SQLite Event Logger (PART B)

# Create variable for checkbutton
check = IntVar()
check.set("-1") # initialize
				   
# Missing DB file or tampered
sqlite3_error = 'Error event_log.db not found / modified!'

# Create a connection to the database.
connection = connect(database = 'event_log.db')
log_db = connection.cursor()

sqlite3_template = "INSERT INTO Event_log VALUES (NULL, 'EVENT')"

log_events = ['Event Logging Executed',
                   'Extracted news from selection',
                   'Latest news archived',
                   'Displayed exctracted archive',
                   'Event Logging Terminated']


def event_logger ():
    try:
        # If Event logger is Activated:
        if check.get() == 1:
                connection = connect(database= 'event_log.db')
                log_db = connection.cursor()
                event_executed = log_events[0]
                sql_query = sqlite3_template.replace('EVENT' , event_executed)
                log_db.execute (sql_query)
                connection.commit()
                
        # If Event logger is Terminated:
        if check.get() == 0:
                connection = connect(database= 'event_log.db')
                log_db = connection.cursor()
                event_executed = log_events[4]
                sql_query = sqlite3_template.replace('EVENT' , event_executed)
                log_db.execute (sql_query)
                connection.commit()
    
    except:
        messenger.config(text = sqlite3_error)

# Log event checkbox
log_button = Checkbutton(window, text="Log User Events", font = ('Times', 14),
                         fg='#212121', bg='#757575', variable = check,
                         command = event_logger)
log_button.place(relx=0.65, rely=0.7)


# Wall Street Journal image
Label(window, bg = '#212121', height = 12).pack(fill=X, pady=23)
img = PhotoImage(file="WSJ.gif")
img = img.zoom(16)
img = img.subsample(32)
logo = Label(window, image=img, borderwidth=0)
logo.place(relx=0.025, rely=0.04)

# Logo subtitle
logo_subtitle = Label(window, text = 'Wall Street Journal Archive',
                bg='#757575', fg='black', font = ('Times', 22, 'bold'))
logo_subtitle.place(relx=0.625, rely=0.4)
logo_subtitle.configure(wraplength='260')

# -------------------------------------------------------------------#

# Start the event loop
window.mainloop()

