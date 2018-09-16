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
    console.log(a_lis);
}

convert_all_paths_to_abs();
