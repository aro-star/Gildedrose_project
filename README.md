## Formation Instructions

Consider this an exercise in refactoring a legacy system to
make your feature easier to implement and leave things in a
more maintainable state than you found them in.

As is with most legacy systems we can't be fully sure it
follows the specifications correctly, and should consider
the possibility that it contains bugs that other systems
rely upon. We should act like this is a legitimate legacy
system that is impractical to full rewrite.

To complete this exercise perform gradual changes, showing
your work with commits (err on the side of more commits to show thinking) 
as you make step-by-step changes. Implement the new feature of conjured 
items when the code has improved enough or it's safe enough to do so.

You'll need to initialize a new git repository to start:

```
git init
git add -A
git commit -m "Welcome to The Gilded Rose"
```

And you can package up a bundle of your completed work with:

```
git bundle create your_name.bundle main
```

## The Gilded Rose Requirements & Specifications

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We
have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:

	- All items have a SellIn value which denotes the number of days we have to sell the item
	- All items have a Quality value which denotes how valuable the item is
	- At the end of each day our system lowers both values for every item

Pretty simple, right? Well this is where it gets interesting:

	- Once the sell by date has passed, Quality degrades twice as fast
	- The Quality of an item is never negative
	- "Aged Brie" actually increases in Quality the older it gets
	- The Quality of an item is never more than 50
	- "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
	- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
	Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	Quality drops to 0 after the concert

We have recently signed a supplier of conjured items. This requires an update to our system:

	- "Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything
still works correctly. However, do not alter the Item class or Items property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover
for you).

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
legendary item and as such its Quality is 80 and it never alters.

### What we do

Open our take-home repo and click `Code` > `Download ZIP` and send this to you.

We recieve your bundle and clone it, then we add our remote and push it up as a branch
to evaluate as a pull request.

```
git clone yourname.bundle yourname-submission
git remote add fmn git@github.com:FormationAI/take-home.git
git push fmn main:yourname-submission
```
