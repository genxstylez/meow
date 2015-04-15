'use strict';

import React from 'react';
import _ from 'lodash';
import DocumentList from '../components/DocumentList';

export default React.createClass({
    mixins: [],

    contextTypes: {
        router: React.PropTypes.func
    },
    render() {
        var categoryId = this.context.router.getCurrentParams().categoryId;

        return (
            <div>
                <DocumentList 
                    categoryId={categoryId} />
            </div>
        );
    }

});