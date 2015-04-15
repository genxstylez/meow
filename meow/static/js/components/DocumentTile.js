'use strict';

import React from 'react';
import _ from 'lodash';
import truncate from 'html-truncate';
import Router from 'react-router';
import WebAPIMixin from '../mixins/WebAPIMixin';

const Link = Router.Link;

export default React.createClass({
    SlideshowInterval: 1000,
    propTypes: {
        id: React.PropTypes.number.isRequired,
        title: React.PropTypes.string.isRequired,
        categories: React.PropTypes.array.isRequired,
        duration: React.PropTypes.string.isRequired,
        images: React.PropTypes.array.isRequired,
        views: React.PropTypes.number.isRequired
    },
    contextTypes: {
        router: React.PropTypes.func
    },
    handleClick() {
        this.context.router.transitionTo('document', {documentId: this.props.id});
    },
    handleMouseOver() {
        this.interval = setInterval(() => {
            this.setState({
                current_index: this.state.current_index < this.props.images.length-1 ? this.state.current_index += 1 : 0
            });
        }, this.SlideshowInterval);
    },
    handleMouseOut() {
        if (_.has(this, 'interval')) {
            clearInterval(this.interval);
        }
    },
    getInitialState() {
        return {
            current_index: 0,
            imgs: [{ url: STATIC_URL + "img/oporn.png"}, ],
        }
    },
    _checkViewport() {
        if (!this.isMounted()) {
          return;
        }
        var el = this.getDOMNode();
        if(this.props.images.length > 0)
            this.setState({
                imgs: this.props.images
            });
    },
    componentDidMount() {
        setTimeout(this._checkViewport, 100);
    },
    render() {
        const DocumentCategoriesNodes = _.map(this.props.categories, category => {
            var current_category_id = this.context.router.getCurrentParams().categoryId;
            var badge_class = "badge "
            badge_class += current_category_id == category.id ? "badge-warning" : "badge-info"
            return (
                <Link key={category.id} className={badge_class} to="category" params={{categoryId: category.id}}>
                    {category.title}
                </Link>
            );
        })
        var marginBottom = {marginBottom: 8};
        var marginRight = {marginRight: 5};
        console.log(this.state.imgs);

        return (
            <div itemScope itemType="http://schema.org/WebPage" 
                className="item col-lg-2 col-md-2 col-sm-6 col-xs-12">
                <div itemProp="audience" itemScope itemType="http://schema.org/PeopleAudience" 
                    className="thumbnail" onMouseOver={this.handleMouseOver} onMouseOut={this.handleMouseOut}> 
                    <meta itemProp="minAge" content="18"/>
                    <Link key={this.props.id} to="document" params={{documentId:this.props.id}}>
                        <img src={this.state.imgs[this.state.current_index].url} />
                    </Link>
                    <div className="caption text-center">
                        <h6>
                            <Link key={this.props.id} to="document" params={{documentId:this.props.id}}>
                                {this.props.title}
                            </Link>
                        </h6>
                    </div>
                    <div>
                        <div style={marginBottom}>
                            <span className="label label-primary" style={marginRight}>Duration: { this.props.duration }</span>
                            <span className="label label-danger">{ this.props.views } Views</span>
                        </div>
                        <div>
                            {DocumentCategoriesNodes}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
});