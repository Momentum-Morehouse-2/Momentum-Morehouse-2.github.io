---
layout: post
title: Welcome to your first day of class
tags: front-end 
---

## Today's topics

- Orientation
- Group Agreement
- Developer tools
  - Setting up your computer
    - [Mac instructions](https://docs.google.com/document/d/1ibV4dA4ciQsxn9MT7TV4-e_KgzUQwCQ7O1zEVfxy_28)
    - [Windows instructions](https://docs.google.com/document/d/1OMtagvx9622O1tPf_ICdXXwUHyWwUShd9hgj1LeiFZg/edit?usp=sharing)
    - Internet Speed Test
  - How to approach code 

### Project
#### In teams of two
The objective is to figure out how we approach code, not necessarily to completely figure out what it does.

- Read this Java code sample and discuss what you think it does
- Record any strategies that you use to try to figure it out

{% highlight java linenos %}
import java.util.Scanner;
class JavaExample
{
   public static void main(String[ ] arg)
   {
	boolean isVowel=false;;
	Scanner scanner=new Scanner(System.in);
	System.out.println("Enter a character : ");
	char ch=scanner.next().charAt(0); 
	scanner.close();
	switch(ch)
	{
	   case 'a' :
	   case 'e' :
    	   case 'i' :
	   case 'o' :
	   case 'u' :
	   case 'A' :
	   case 'E' :
	   case 'I' :
	   case 'O' :
	   case 'U' : isVowel = true;
	}
	if(isVowel == true) {
	   System.out.println(ch+" is  a Vowel");
	}
	else {
	   if((ch>='a'&&ch<='z')||(ch>='A'&&ch<='Z'))
		System.out.println(ch+" is a Consonant");
	   else
		System.out.println("Input is not an alphabet");		
        }
   }
}
{% endhighlight %}

### TODO

1. Read the how we work remotely doc.
2. Make sure your computer is all set up and ready to go.
3. Complete the pre-work assignments.

### Links from class

* [How we work remotely](https://docs.google.com/document/d/1l2RYOM-fdJCgd7nWbXp2k_t6xNDNRVZDlqEfn83TACg/edit?usp=sharing)
* [Setting up your computer](https://drive.google.com/open?id=1ibV4dA4ciQsxn9MT7TV4-e_KgzUQwCQ7O1zEVfxy_28&authuser=1)
* [Team Two Group Agreement]
* [Class Video](https://us02web.zoom.us/rec/share/vM9EM5XB51tORZHK6kvHYPELHYbaaaa8gXUfrKAKmUzZ4YG0GWSBM8t4jrd9cCJP) Passcode: YK4?sFWd 

