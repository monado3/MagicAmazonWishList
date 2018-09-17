Magic Amazon WishList
=================
In Amazon WishList, every book will automatically have a link  
to its detail page at U-tokyo OPAC , by just execution of one command.

## Requirements
- pipenv (Python Package Manager)
- Google Chrome

## Installation
1. You need install pip package.  
At the project root, `$ pipenv install`

1. add your wishlist info to `settings.py`
    1. To generate `settings.py`, `$ pipenv run setup`
    1. You need to change your wishlist's privacy settings.
        1. Visit Amazon website on the browser
        1. Move to the page of wishlist of books you'd like to cast a spell on
        1. Click `･･･` of the upper right
        1. Open `Manage list`
        1. Set `Privacy` to `Shared` or `Public`
        1. Save changes (Don't close the page)
    1. You need to find your wishlist's URL for share.
        1. Open `Send list to others` of the upper right
        (this is very next to `･･･`)
        1. Copy `Permalink` to your clipboard
    1. You need to edit `settings.py` as below.
        1. Replace `please input your wishlist url for share` with your wishlist Permalink (Paste from clipboard)
        
## Usage
| Command | Behavior |
----|----
|`$ python main.py` or `$ pipenv run start`|Fetch the latest information from Amazon, and Show Magic Wishlist | 
|`$ pipenv run show`| Show cached Magic Wishlist (Not fetch the latest information) 
|`$ pipenv run clear`| Delete all the cached file (`data/books.json`)|
|`$ pipenv run clear`| Delete all the cached file (`data/books.json`)|

***Note:*** *when a book has cached information,<br>
this program does not fetch the information of the book from U-tokyo OPAC.<br>
Therefore, when you'd like to fetch the latest information,* `$ pipenv run opac clear && pipenv run start`

## Notes
- This program uses Amazon.co.jp as default,<br>because this program is written on the assumption that it is used in Japan.<br>
You need to change some parts of codes, if you'd like to use other countries' Amazon.
- From the second time use of main.py, the execution time will be shorter thanks to cache. 

## Examples