'use strict';

import request from 'superagent';

export default {

    /**
     * get all/categorised posts from the server
     * @param {number} id
     * @param {function} cb
     */
    getDocuments(url, category_id, cb) {
        if (url==null) {
            var suffix = "";
            if(category_id) {
                suffix = '&categories=' + category_id;
            };
            url = '/api/v1/documents/?format=json' + suffix
        }
        request.get(url)
            .type('application/json')
            .accept('application/json')
            .end(cb);
    },

    /**
     * get post detail from the server
     * @param {number} id
     * @param {function} cb
     */
    getDocument(id, cb) {
        request.get('/api/v1/documents/' + id + '/?format=json')
            .type('application/json')
            .accept('application/json')
            .end(cb);
    }

};