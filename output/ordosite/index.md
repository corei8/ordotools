---
layout: default
title: "Ordo Media"
---

<h1 class="display-1 text-center mt-5">
    <b>Ordo</b><small>.media</small>
</h1>

You will find on this website the documentation (coming soon) and some demonstration of an
ordo- and calendar-generating application. The algorithms are very difficult to
develop for a single year, and even much trouble arises when attemping to write
an application that has to work year after year. Some parts of this website
(what of it is available to the public) may seem scattered, erroneous, or
incomplete. This is not intentional, in the strict sense of the term, but it is
the result of the careful and tedious calculations that have to be performed in
order to produce the liturgical calendar. You can view the progress of the
calendar [here](/calendar.html). Its accurracy improves slowly, so the
developer will try to maintain a [changelog](/changelog.html) so that the viewer can see the
progress being made, or perhaps be informed of progress which cannot be seen.

# Goals

Making this website pretty is not a high priority, but I will try to do that as
much as I am able.

### Calendar

 1. As a LaTeX document, for producing publishable calendars;
 2. As an ICS file, for adding the liturgical year to a mobile calendar;
 3. As a python dictionary, which can be used for various purposes.

The calendar is the hardest part of the entire project, but happily, at the
time of writing, it is close to complete.

### Ordo

This is the hardest part, and the original goal of the entire project. The task
of producing an ordo by hand is so laborious and time comsuming, not to mention
prone to errors, that making writing a program to do the job seems to be the
best answer to the problem.

Any application which produces an ordo has several requirements:

1. It must be easy to maintain. This seems obvious, but writing spaghetti code
   to produce a calendar for one year that breaks on the next year is quite out
   of the question. This true for all calendar programs, but especially for the
   liturgical year because of the many complexities and overlaps that occur each
   year, which repeat but in slightly different ways every year.
2. It must be extensible. This is the most difficult challenge (and has caused
   the autor to re-write his program three times before settling on its current
   structure), but is the most necessary requirement.

# Questions and Answers

#### Where is the code?

In a private repository on GitHub. It will be made public soon.

#### How can I help?

When the repository is made public all contributions will be welcome. The most
useful contribution will be updating the diocese and country directories.
Familiarity with python might be useful but is not necessary, since the
dictionaries that hold the information and the documentation that is being
prepared will be very easy to follow and figure out.
