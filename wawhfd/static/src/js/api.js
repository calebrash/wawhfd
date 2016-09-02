function paramsToString (dict) {
    return Object.keys(dict).map((d) => `${d}=${encodeURIComponent(dict[d])}`).join('&');
};

function csrfToken () {
    let token;
    document.cookie.split(';').forEach((cookie) => {
        if (cookie.indexOf('csrftoken') >= 0) {
            token = cookie.split('=')[1].trim();
        }
    });
    return token || null;
};

function makeRequest(endpoint, method, data) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        let url = `/api/${endpoint}/`;
        let params = null;

        if (data) {
            params = paramsToString(data);
        }

        xhr.open(method, url, true);
        if (method === 'POST') {
            xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            xhr.setRequestHeader('X-CSRFToken', csrfToken());
        }
        xhr.send(params);

        let getResponse = () => JSON.parse(xhr.responseText);
        xhr.addEventListener('load', () => resolve(getResponse()));
        xhr.addEventListener('error', () => reject(getResponse()));
        xhr.addEventListener('abort', () => reject(getResponse()));
    });
}

const api = {
    get: (endpoint, data) => makeRequest(endpoint, 'GET', data),
    post: (endpoint, data) => makeRequest(endpoint, 'POST', data)
};

export default api;
