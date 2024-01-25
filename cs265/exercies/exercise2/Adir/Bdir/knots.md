% Sample Pandoc Markdown
% Prof. Long
% 20 JAN 2021

# Sample (Pandoc) Markdown (header 1)

## Intro (Level 2)

Note, we really don't have comments.  **Huge** ommission in markdown.

Vim knows markdown, too.

Pandoc is a handy utility, takes and input several formats, including text, markdown, and HTML.  Outputs to many
formats, including HTML, LaTeX, PDF, and RTF.

## Markdown

### Fonts and Effects

We _can get an_ underscore.  Huh.  Italics.  :/

*This is a single asterisk* (Bold?  Italics?)

**Two asterisks.**

***Three asterisks***

~~Strikethrough~~

Seems we have super^scripts^ and sub~scripts~, too.

Pandoc allows us to embed a subset of LaTeX math:  $y = 3n + 7$

`Back ticks give us code font, inline`

### Layout

This is
a 
single
paragraph.

This is another paragraph.

We can explicitly\
break lines\
like this.

#### Lists

Here's an unordered list:

- Cleat Hitch
- Sheet Bend
- A reliable loop:
	- Bowline 
	- Tugboat Hitch
- Spar Hitch
- Clove Hitch
- Reef Knot

Ordered list:

1. We can use # to get PD to count for us
#. Next thing
	a. And we can nest these things, too
	#. And these things
#. Done
	i. I lied
	#. Note, we can specify the characters to be used

#### Blockquotes

>This is indented a bit.

>>This is indented further

**Note:**  Lists, blocks, and other things need blank lines around them.

~~~~~
	/* Code blocks between lines of tildes */

	void hello( char *n )
	{
		printf( "Heeeelllo, %d\n", n ) ;
	}
~~~~~

### Links

[Learn some knots]( http://animatedknots.com, "Optional Title" )

---------------

## Publishing

`-i` specifies the input file, and `-o` specifies the output file.  Often, the formats can be gleaned from the file
extensions.  You can help Pandoc out.  `-f` lets you specify the from formate, and `-t` the target format.

>~~~~
>$ pandoc -i knots.md -o knots.html
>~~~~

Or,

>~~~~
>$ pandoc -i knots.md -o knots.rtf
>~~~~

To publish to LaTeX or PDF, specify `latex` as the target format:

>~~~~
>$ pandoc -t tex -i knots.md -o knots.pdf
>~~~~

**********

## Closing

There are other features, but, this is a good start.

