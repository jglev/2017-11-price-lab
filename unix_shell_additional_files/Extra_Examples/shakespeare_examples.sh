cd "/home/jacoblevernier/Documents/Teaching/2017-11_Price_Lab_Digital_Humanities_Workshop/unix_shell_additional_files/Extra_Examples"

# Number of Tybalt lines:
grep "_Tybalt._" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | wc --lines

# Total number of Tybalt lines + mentions
grep "Tybalt" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | wc --lines

# Let's explore those...
grep "Tybalt" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | less

# ...Or save them...
grep "Tybalt" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt > Tybalt_Mentions.txt


# Let's do the first lookup, but for each of several characters:
for character_name in Tybalt Romeo Juliet Benvolio
do
	echo "$character_name's number of lines:"
	grep "_$character_name._" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | wc --lines
done

# How many times does love get mentioned?
grep "love" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | wc --lines

# Does that number change if we ignore case?
grep --ignore-case "love" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt | wc --lines

# Let's see the 6 examples where "Love" is capitalized -- are they all the start of sentences, or are some references to Love as a person?
grep "Love" ./Romeo_and_Juliet_from_Project_Gutenberg_47960_Notes_Removed.txt

# What if we want to alphabetize our characters' names?
echo "Tybalt
Romeo
Juliet
Benvolio" | sort
