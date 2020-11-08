# Hasch Code 2019

## Introduction ✏
Competition organised by Google in 2019. The objective is to answer a given 
problem, on the theme of data processing.
The script is made in Python V3. No external library is needed.
The results are calculated and displayed directly in the terminal.

## Issue
As the saying goes, "a picture is a thousand words".
We agree, photos are an important part of contemporary digital and cultural 
life. Around 2.5 billion people worldwide carry a camera, in the form of a 
smartphone, in their pocket every day. We are also making good use of them, 
taking more photos than ever before (in 2017, Google Photos announced that it 
was supporting more than 1.2 billion photos and videos a day). 
The rise of digital photography creates an interesting challenge: what should 
we do with all these photos? In this competition issue, we will explore the 
idea of composing a slideshow from a collection of photos.

### Objectives ✔
Based on the list of photos and the tags associated with each one, arrange the 
photos into a slide show that is as interesting as possible.

A photo is described by a set of tags. For example, a photo with a cat on a 
beach, on a sunny afternoon, could be with the following tags : [cat, beach, sun].
The orientation of each photo is either horizontal or vertical.

A slide show is an ordered list of slides. Each slide contains one or the other:
    - A single horizontal photo
    - Two vertical photos side by side

### Score Calculation 
The slide show is graded according to the interest of the transitions between 
each pair of its following slides have.
We want the transitions to have something in common to preserve continuity 
(the two slides should not be totally different).
The similarity of two vertical photos on the same slide is not taken into 
account for the notation.
This means that two photos may, but need not, have tags in common.

For the next two slides S i and S i+1, the interest factor is the minimum (the 
smallest number of the three):
    - The number of common tags between S i and S i+1
    - The number of tags in S i but not in S i+1
    - The number of tags in S i+1 but not in S i .

## Solution 
### Principle 
This is a rather crude method. 
To do this, a random image is chosen from the given list.
We are going to look for the combination of images, to form the slide, which 
yields as many points as possible.
So we compare the tags of our image with all the other images. Once found, we 
start again with the new slide. And those until as long as there are images left. 

### Score
This is calculated directly by the script.
File                    | Pictures | Slides  | Unrelated pictures | Points  | Time
----------------------- | -------- | ------- | ------------------ | ------- | --------
a_example.txt           | 4        | 3       | 0                  | 2       | 00:00:00
b_lovely_landscapes.txt | 80 000   | 80 000  | 11 993             | 204 018 | 00:36:15
c_memorable_moments.txt | 1 000    | 750     | 26                 | 1 530   | 00:00:00
d_pet_pictures.txt      | 90 000   | 60 000  | 12                 | 266 253 | 00:40:35
e_shiny_selfies.txt     | 80 000   | 40 000  | 2                  | 371 863 | 00:46:57
Total                   | 251 004  | 180 753 | 12 033             | 843 966 | 02:03:47

### Limits ⚠
    - The first image is chosen at random. This varies the results.
    - The method gives a high score but is very time consuming.
