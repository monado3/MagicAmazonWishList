function to_absolute_path(path) {
    const baseUrl = 'https://www.amazon.co.jp/';
    const url = new URL(path, baseUrl);
    return url.href;
}

function is_rel_path(path) {
    return path.startsWith('/');
}

function convert_all_paths_to_abs() {
    const a_lis = document.getElementsByTagName('a');
    for (let i = 0; i < a_lis.length; i++) {
        const i_pathname = a_lis[i].pathname;
        if (is_rel_path(i_pathname)) {
            a_lis[i].href = to_absolute_path(i_pathname);
        }
    }
}


function load_books_json_from_html() {
    return JSON.parse(document.getElementById('books.json').innerText);
}

function change_color_book_bg(book_data, book_div) {
    if (book_data.num_registered > 0) {
        book_div.style.backgroundColor = '#ccffcc';
    }
}

function add_info(book_data, book_div) {
    if (book_data.num_registered > 0) {
        const span = document.createElement('span');
        span.textContent = `${book_data.num_registered} books at `;
        span.className = 'num_registered';
        span.style.fontSize = 'medium';

        const a = document.createElement('a');
        a.innerText = 'OPAC';
        a.href = book_data.opac_link;
        a.className = 'num_registered';
        a.style.fontSize = 'medium';

        const book_right_div = book_div.querySelector('div[id^="itemAction"]');
        book_right_div.appendChild(span);
        book_right_div.appendChild(a);
    }
}

function magic_book(book_data) {
    const book_div = document.getElementById(book_data.amazon_book_id);
    change_color_book_bg(book_data, book_div);
    add_info(book_data, book_div);
}

convert_all_paths_to_abs();
const books = load_books_json_from_html();
for (let i = 0; i < books.length; i++) {
    magic_book(books[i]);
}