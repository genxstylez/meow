'use strict';

import React from 'react';
import _ from 'lodash';
import Router from 'react-router';
import WebAPIMixin from '../mixins/WebAPIMixin';
import DocumentTile from './DocumentTile';
import MansonryMixin from 'react-masonry-mixin';
import ScrollListenerMixin from '../mixins/ScrollListenerMixin';

const Link = Router.Link;

const mansonryOptions = {
    transitionDuration: 1
}

export default React.createClass({
    mixins: [MansonryMixin('mansonryContainer', mansonryOptions), WebAPIMixin, ScrollListenerMixin],

    pollInterval: 60000,

    propTypes: {
        categoryId: React.PropTypes.string,
    },

    getInitialState() {
        return {
            documents: [],
            next_page : null,
            has_next: false,
            is_loading: false
        }
    },


    onPageScroll() {
        var bottomOffset = this.refs.mansonryContainer.getDOMNode().scrollHeight - this.state.scrollTop;
        if (bottomOffset < 1500 && !this.state.is_loading && this.state.has_next) {
            this.setState({
                is_loading: true
            });
            this._getDocuments(this.state.next_page);
        }
    },
                
    _getDocuments(url, categoryId) {
        this.getDocuments(url, categoryId, (error, response) => {
            var new_elements = error ? [] : response.body.objects,
                next_page = response.body.meta.next, 
                has_next = response.body.meta.next != null; 
            this.setState({
                documents: this.state.documents.concat(new_elements),
                next_page: next_page,
                has_next: has_next,
                is_loading: false
            });
        });
    },

    componentWillReceiveProps(nextProps) {
        if (nextProps.categoryId != this.props.categoryId || nextProps.subcategoryId != this.props.subscategoryId){
            // if category changes, start with a new list of posts
            this.setState({
                documents: []
            });
            this._getDocuments(null, nextProps.categoryId);
        }
    },
    /**
     * React component lifecycle method
     */
    componentDidMount() {
        this._getDocuments(null, this.props.categoryId);
    },

    /**
     * render
     * @returns {XML}
     */

    render() {
        const DocumentTileNodes = _.map(this.state.documents, doc => {
            return (
                <DocumentTile 
                    key={doc.id} 
                    id={doc.id} 
                    title={doc.title}
                    categories={doc.categories}
                    duration={doc.duration}
                    images={doc.images} 
                    views={doc.views} />
            );
        });
        return (
            <div className="mansonryContainer" ref="mansonryContainer">
                {DocumentTileNodes}
            </div>
        );
    }

});