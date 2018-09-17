Magic Amazon WishList
=================
In Amazon WishList, every book will automatically have a link
to its detail page at U-tokyo OPAC , by just execution of one command.

|Before|After|
|----|----|
|<img align="center" src="https://user-images.githubusercontent.com/36162674/45613446-59915d80-baa1-11e8-9581-3a02f348b558.png" ></img>|<img align="center" src="https://user-images.githubusercontent.com/36162674/45613621-e3412b00-baa1-11e8-97fd-d56e4888f155.png"></img>|

## Requirements
- pipenv (Python Package Manager)
- Google Chrome

## Installation
1. You need install pip package.
At the project root, `$ pipenv install`

1. add your wishlist info to `settings.py`
    1. To generate `settings.py`, `$ pipenv run setup`
    1. You need to change your wishlist's privacy settings.
        1. Visit [Amazon](https://www.amazon.co.jp) on the browser
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

### Main
<table>
    <tr>
        <th colspan="2">feature</th>
        <td><code>$ pipenv run fullupdate</code></td>
        <td><code>$ pipenv run start</code></td>
        <td><code>$ pipenv run opacupdate</code></td>
        <td><code>$ pipenv run open</code></td>
    </tr>
    <tr>
        <td colspan="2">fetch the latest wishlist from Amazon</td>
        <td align="center">○</td>
        <td align="center">○</td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
    <tr>
        <td rowspan="2">fetch the latest info from OPAC</td>
        <td align="center">all update<sup>※1</sup></td>
        <td align="center">○</td>
        <td align="center"></td>
        <td align="center">○</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">newly added to wishlist<sup>※2</sup></td>
        <td align="center"></td>
        <td align="center">○</td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
    <tr>
        <td colspan="2">make the magic wishlist</td>
        <td align="center">○</td>
        <td align="center">○</td>
        <td align="center">○</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td colspan="2">open the magic wishlist</td>
        <td align="center">○</td>
        <td align="center">○</td>
        <td align="center">○</td>
        <td align="center">○</td>
    </tr>
</table>

***※1*** *All books in the wishlist are updated how many they are registered to OPAC*<br>
***※2*** *Only Newly added books to the wishlist are updated how many they are registered to OPAC*

### Sub
|Command|Behavior|
|----|----|
|`$ pipenv run clear`|Delete the cached file (`data/books.json`)|
|`$ pipenv run setup`|Generate `settings.py` (if it exists, overwrite)|

***Note:*** *when a book has cached information,<br>
this program does not fetch the information of the book from U-tokyo OPAC.<br>
Therefore, when you'd like to fetch the latest information,* `$ pipenv run opac clear && pipenv run start`

## Notes
- This program uses Amazon.co.jp as default,<br>because this program is written on the assumption that it is used in Japan.<br>
You need to change some parts of codes, if you'd like to use other countries' Amazon.
- From the second time use of main.py, the execution time will be shorter thanks to cache.
