# Syllabus, with teaching notes following the 2017-11-20 Price Lab two-day workshop

## Before the workshop

We sent the following email to participants, pointing them toward the installation instructions developed by the Software Carpentry community:

> We are very excited about the Python for Humanists workshop this weekend (Nov. 18-19) and hope you are too! Here are a few things you should know in advance.

>- We designed this workshop with the assumption that everyone is an absolute beginner.
>- To make things go a bit more smoothly in the morning, please install Bash and Python 3.6 or higher on your machine. Instructions for doing both can be found here: http://installation.software-carpentry.org/
>- We will get started at 10AM. There will be breakfast by 9:30 so feel free to get in a little early so you can eat something.

The workshop had 17 participants on the first day, and (due to illness) 16 on the second day. We originally planned to have a second instructor available to answer questions, but further illness during the weekend of the workshop prevented this from being realized. In general, it was ok having only one instructor, as it was instructive to talk through errors that individual participants were having in front of the group, to model a debugging process (e.g., moving from "I'm seeing an error" to "I'm seeing a *syntax* error" or "I'm seeing a *ModuleNotFound* error," and then diagnosing and correcting the underlying problem together). I have added notes below on areas that did require the workshop to stop (mostly Windows-related cross-platform issues).

## Day 1

### Introduction: Pedagogical philosophy and expectations

- My starting point: Jamie Pennebaker, when visiting the University of Oregon and talking with graduate students in Psychology about working with developers, noted that, from his work as a psychologist who works a lot with developers, (I'm paraphrasing from memory:) "You don't need to become a developer! But you *do* need to learn to *talk with* developers -- to understand their language, to use their language."

With this in mind, the workshop was about first **learning to talk with developers.** And then, from that vocabulary, **learning to develop code oneself.**

The workshop was 10:00-17:00 each day. That's 7 hours per day. With a 1 hour lunch break and two 10-15 minute breaks, that means we shared `7.0 - 1.0 - 0.25 - 0.25 = 5.5` hours of instructional time per day.

- Day 1 (5.5 hours of instruction): Learn to talk with coders.
    - Introductions
        - Who am I?
            - Background, current position, email
            - Setting a tone:
                - The "Unix Magic" poster by Gary Overacre
                - The ["hacker's mindset"](https://en.wikipedia.org/wiki/Hacker_culture) (in the 1970s definitional sense)
        - Who are each of you?
            - Name, department, project interest(s) -- *like you're explaining it to a kindergartner.*
        - This is a space to fail. To muddle through. To bash on things.
            - Part of being ok with failing: I'm ok with saying "I don't know" -- so this space of the whiteboard is going to be a place for writing questions that I don't know, that we can come back to (we can research them together).
                - My point here: People who are professional developers often have to Google things as they go. The point isn't to be able to memorize all possible commands -- it's to know where to find them. Which is a lot like grad school in general, I think.
        - Goals for this weekend
            - The J. Pennebaker quote above
            - My goals:
                - By the end of the weekend, you won't be able to write Python fluently -- that's not a realistic expectation for a two-day workshop; but you will be able to *read* it with some fluency, and to modify code that you find. Those are more realistic expectations.
                    - Specifically, you'll be able to understand new code that you see (as we'll have gone through several real-world example scripts that accomplish actual [non-toy] goals), and, based on your new understanding of python's syntax:
                        1. Understand the structure of the code you're looking at.
                        2. Be able to look up help (whether within Python, or using appropriate/accurate vocabulary terms [such as *method/function,* *module,* *"for loop,"* etc.] in a search engine like Google) *and understand it*.
                - By the end of the first day, you'll be able to explain, to each other, the primary tools in a "hacker's toolkit" [see below].
                - By the end of the first day, given a project description, you'll be able to plan out, step-by-step, what you need to do to bring it about. (Put differently, you'll have the vocabulary to do that.)
                - By the end of the second day, you'll be able to understand several example scripts, and to *articulate how* you'd need to change them for a new project you might work on (even if not yet be able to *do so* fluently / on the first try).
        - I have a lot of topics that we can talk about. My plan is to remain open-minded and flexible around them. So, we might break out into groups periodically, to check in with where you're at.
            - What I'm trying to *avoid* here: You passively typing things into a script, feeling like you're learning, but then not really retaining any of it.
            - If you learn like me, *retention comes from practice.* Specifically, it comes from making mistakes and then taking notes so that you won't forget to do it a different way the next time.
            - Statistics of asking questions: If you have a question, it's likely that someone else does, too.
                - I've been a grad student, and I know the "nodding thoughtfully" look. If you have a question, just ask it : P
    - What is code? What is a "script"?
        - Commands, (here) read top to bottom, left to right
    - Why would you use code?
        - *Automation*
        - Doesn't have to *replace* workflow -- can *complement* workflow.
            - [Veccompare](https://github.com/publicus/r-veccompare) example with 8 maps.
    - Why would you use one language over another?
        - What kinds of questions can you ask? What is it that / What is the domain in which scripting/programming in that language can do?
        - How active is the community? For what types of work?
    - Tools for the toolbox:
        *All of this can be in pseudocode (which will be Python-flavored, but the students won't know that yet). NO REAL code for this, just ideas.*
        1. Commands / functions
            - Start by relating this to Excel
            - A function is "a summary word for a series of steps."
            - We have functions in our everyday lives -- for example, we have a function called "Write on the board."
        2. Strings vs. numbers vs. lists
            - It makes sense to do certain things (like rounding, or capitalizing) to some types of things, but not to others.
        3. If statements
        4. For loops
            - Example: Converting wav to MP3 files in a directory.
            - (We didn't cover this) List comprehensions (just write this out, sliding it in as an example of lay "for-loop-like" language.)
            - (The idea that you can have) Nested for loops, if statements, etc.
                - Example: For each book in a list, loop through and tell me which Libraries list have a copy of it.
        5. While loops
            - These were only explained conceptually -- I did not show code for this topic.
            - Example: Keeping track of how many downloads you've made from Google Maps, so that you don't go over their (example) threshold of 5,000 per day.
        7. Libraries/modules (think of browser extension metaphor, plus the metaphor of asking a friend who knows better how to do something (think of Python's `pd.read_csv` syntax))
    - An introduction to `bash`, for navigating around and understanding file trees, and for understanding the basics of how code works.
        - I drew selectively from the [Software Carpentry "Unix shell" lesson](http://swcarpentry.github.io/shell-novice/) for this section.  
      (This included attribution to meet the SC CC-BY license terms for their content.)
    - Looking at Python basic syntax
        - General formatting notes (indentation, colons, etc.)
        - PEP8 (introduce students to it before they know enough to be annoyed by it)
            - Graduate students are used to following style guides when writing, as with APA and MLA formats. I approached PEP8 in this same way, and after showing PEP20, "The Zen of Python," and its emphasis on readability.
        - Go through the six items / basic building blocks of the "Hacker's toolbox" above, showing how each looks in Python.
            - For `type`s, I drew from the [Software Carpentry "built-in functions" lesson](https://swcarpentry.github.io/python-novice-gapminder/04-built-in/).
            - For for loops and if statements, we created together, on the fly (and introducing dictionaries at the same time, [explained as "premium lists and lists with named elements," since they use `{}`, which visually looks like an "upgrade" to the `[]` that lists use] an example in which we defined a dictionary of characters in Romeo and Juliet (by house -- Montague, Capulet, and Other), and then created a for loop that would unlist them and put them into a single list, regardless of house. We then took that list, joined it with commas (`', '.join(the_list)`), and embedded it in a multi-line f-string (introducing multi-line strings at the same time) as part of an email to an advisor that we could then copy and paste ("I have concluded that the characters in Romeo and Juliet are...").
            - For functions vs. methods:
                - I initially did not use the word "method," but instead explained that it's two places a function goes in Python3, *though they always look like `commandname(option1, option1)`, regardless of placement.* I started using "method" on the second day.
                - I used `len` and `round` as examples of functions, and `capitalize` and `upper` as examples of methods
                - I initially used the explanation that functions are a type of command that make sense to try to execute anywhere, whereas methods only make sense to try for certain types of things, but `len()` broke this explanation, as it fails with `int`s. This left participants confused.
                    - The better explanation I then came up with (to which participants responded well) is that functions like `len()` were defined by the people who wrote Python itself, whereas methods like `upper()` were defined *by the people who defined what a `str` is* -- `upper()` is defined *inside of the definition of what a string is,* while there are other commands that are defined *inside of the definition of what, e.g., an `int` is.*
            - For modules, I drew from the [Software Carpentry "libraries" lesson](https://swcarpentry.github.io/python-novice-gapminder/06-libraries/).
- Day 2 (5.5 hours of instruction): Learn to be one.
    - *Everything here is based on looking through existing scripts. Learning from usable code **in parallel with / as a support for** writing your own.*
    - Four vignettes: (Note: These do not include Natural Language Processing, except maybe in passing)
        - Converting files in a directory from MP3 to WAV
        - Downloading things by scraping a website
        - Downloading things by querying an API (We did not cover this, except in passing (as noted below)
            - Pandas for data management (looking toward ggplot2) (We did not have time to cover this)
            - (If we have time) Make a network graph from an edge list (We did not have time to cover this)
        - ggplot2 (for graphing) (We did not have time to cover this)
    - Final session of the second day: Discussion, answering questions that come up, working on / hacking on things together



## The *approximate* timeline of the workshop (this is including a one-hour lunch break, but not smaller breaks, and is also from my memory two days after the workshop's completion):

## Day 1

- 10:00-10:45 Introduction to the workshop, people introductions, and expectations
- 10:45-13:00 Talking through the six concepts in the "toolbox" above (without looking at any code)
- 14:00-15:00 Introduction to `bash`, to understand how file directory structures work, and to understand the stakes of working with command-line interfaces (i.e., no Recycle Bin, not always prompts to make sure of something, etc.)
    - We talked through `ls`, `cd`, `mkdir`, `touch`, `less`, `head`, `grep`, `rm`, `cp`, `mv`, `wc (-l)`, `man`/`command --help`, and pipes (not necessarily in that order).
        - *Note:* GitBash on Windows does not have `man` installed. `commandname --help` will often work instead.
- 15:00-17:00 Demonstrating Python 3 syntax for each of the elements in the "toolbox"  
  We got through `if/elif/else` statements on this day.
  - I used the Query OCLC API example script to show use of an `if` statement (and a `for loop`, though students hadn't seen the syntax for that yet) in real-world code, at the request of one of the participants.

## Day 2

- 10:00-10:30 Check-in from the previous day
- 10:30-13:00 Demonstrating Python 3 syntax for each of the elements in the "toolbox"  
  We got through the remainder of the "toolbox" items (skipping over `while` loops, except just speaking conceptually about them, with the example of counting one's downloads and not going over a threshold).
- 14:00-16:30 Example scripts:
    - The motivation of this portion: *We were looking through existing, real-world scripts, of the type participants will need to understand when they view others' code, modify others' code, or read StackOverflow and similar help posts online. I.e., teaching "don't panic, you can figure this out."*
    - We practiced a three-part process for writing code for participants' own projects:  
      (This was introduced on the second day -- before looking at each of the example scripts, I explained the goal, and we wrote out a narrative and then a checklist together, and then checked off items from that list as we went through the example script).
        1. Write out what you want to do *in narrative form, as though you are explaining it to a kindergartner.*
        2. Take each phrase from the paragraph you've written above, and turn it into a checklist item (still in lay language), identifying key phrases from your paragraph to translate into technical coding terms *by drawing from our "toolkit" of six concepts* (e.g., "go through *each of*..." can be translated "create a *"for loop"* over...").
        3. Write code from your checklist items.
    - Converting files in a directory from MP3 to WAV  
      *Notes:*
        - This script will not work if `ffmpeg` or `avconv` is not installed. Thus, students needed to just look on with me demonstrating when it came time to run the `AudioSegment()` command in the script.
        - For installing `pydub` (and other modules) using `pip`:
            - Mac OSX users can use `bash`.
            - Windows users need to use *not* GitBash, but "Anaconda Prompt," which is installed in their Start menu when Anaconda is installed.
        - For launching Spyder:
            - OSX users can run `spyder` from `bash`.
            - Windows users may need to open "Anaconda Launcher," which is installed in their Start menu when Anaconda is installed, and launch Spyder from there (using a button that is labeled "Launch" under the Spyder logo).
    - Scraping a website
        - I prefaced this with a discussion of the Computer Fraud and Abuse Act, and about ethical responsibilities in web scraping (including not DoS-ing a web server, by rate limiting).
- 16:30-17:00 Wrap-up discussion about next steps, areas of particular lingering confusion, excitement, joy, etc. Areas where participants could see these approaches and tools applying in their own work (with the idea that participants might have similar interests, and that opportunities for collaboration might thus be presented here).
