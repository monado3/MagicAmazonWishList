Magic Amazon WishList
=================
In Amazon WishList, every book will automatically have a link
to its detail page at [U-tokyo OPAC](https://opac.dl.itc.u-tokyo.ac.jp/opac/opac_search), by just execution of one command.

|Before|After|
|----|----|
|<img align="center" src="https://user-images.githubusercontent.com/36162674/45613446-59915d80-baa1-11e8-9581-3a02f348b558.png" ></img>|<img align="center" src="https://user-images.githubusercontent.com/36162674/45613621-e3412b00-baa1-11e8-97fd-d56e4888f155.png"></img>|

## Requirements
- pipenv (Python Package Manager)
- `Google Chrome` or `Chromium`<br> 
***(I've confirmed the operation on `Ubuntu 18.04 LTS` and `Manjaro`)***

## Installation
1. Require `pipenv` module due to easy package install.
`$ pip install pipenv`

1. You need install pip package.
At the project root, `$ pipenv install`

1. add your wishlist info to `setting.py`
    1. To generate `setting.py`, `$ pipenv run setup`
    1. You need to change your wishlist's privacy setting.
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
    1. You need to edit `setting.py` as below.
        ```python
        class AmazonInfo:
           book_wishlist_dic = {
               'wishlist name 1': 'wishlist link 1',
               'wishlist name 2': 'wishlist link 2',
           }
        ```

## Usage

### Main
<table>
    <tr>
        <th colspan="2">feature</th>
        <td><code>$ pipenv run fullupdate</code></td>
        <td><code>$ pipenv run start</code></td>
        <td><code>$ pipenv run opacupdate</code></td>
        <td><code>$ pipenv run show</code></td>
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
|`$ pipenv run setup`|Generate `setting.py` (if it exists, overwrite)|
|`$ pipenv run help`|Open [this](https://github.com/monado3/MagicAmazonWishList) page (Needs environment variable `$BROWSER`)|

## Notes
- This program uses Amazon.co.jp as default,<br>because this program is written on the assumption that it is used in Japan.<br>
You need to change some parts of codes, if you'd like to use other countries' Amazon.
- From the second time use of main.py, the execution time will be shorter thanks to cache.
- If you'd like to use more than one wishlist, add wishlists' links to `book_wishlist_dic`(list) of `AmazonInfo` class
in `setting.py`.

## License
[MIT](https://github.com/monado3/MagicAmazonWishList/blob/master/LICENSE)

## Author
[monado3](https://github.com/monado3)
