let params = {
    toString: function (dict) {
        let result = '';
        for (let key in dict) {
            result += `${key}=${dict[key]}`;
        }
        return result;
    }
};


const api = {
    get: (endpoint, data) => {
        return new Promise((resolve, reject) => {
            let xhr = new XMLHttpRequest();
            let url = `/api/${endpoint}/`;
            if (data) {
                url = `${url}?${params.toString(data)}`;
            }

            xhr.open('GET', url);
            xhr.send();

            let getResponse = () => JSON.parse(xhr.responseText);
            xhr.addEventListener('load', () => resolve(getResponse()));
            xhr.addEventListener('error', () => reject(getResponse()));
            xhr.addEventListener('abort', () => reject(getResponse()));
        });
    }
};

export default api;
