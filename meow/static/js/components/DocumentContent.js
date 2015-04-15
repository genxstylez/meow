'use strict';

import React from 'react';
import _ from 'lodash';
import Router from 'react-router';
import WebAPIMixin from '../mixins/WebAPIMixin';


const Link = Router.Link;

export default React.createClass({
    contextTypes: {
        router: React.PropTypes.func
    },

    mixins: [WebAPIMixin],

    propTypes: {
        id: React.PropTypes.string.isRequired,
    },

    getInitialState() {
        return {
            id: '',
            title: '',
            categories: [],
            duration: '',
            images: [],
            embed: '',
            views: 0,
            desc: ''
        }
    },
    _getDocument(Id) {
        this.getDocument(Id, (error, response) => {
            var doc = error ? [] : response.body;
            this.setState({
                id: doc.id,
                title: doc.title,
                categories: doc.categories,
                duration: doc.duration,
                images: doc.images,
                views: doc.views,
                embed: doc.embed,
                desc: doc.desc
            });
        });
    },
    componentDidMount() {
        this._getDocument(this.props.id);
    },

    componentDidUpdate(prevProps, prevState) {},

    handeClickOnCross() {
       if(!this.context.router.goBack()) {
            this.context.router.transitionTo('/')
       }
    },

    render() {
        const DocumentCategoriesNodes = _.map(this.state.categories, category => {
            return (
                <Link to="category" params={{categoryId: category.id}}>
                    <span className="badge badge-info">{category.title}</span>
                </Link>
            );
        });
        var height60 = {height: "60%"}
        var marginBottom = {marginBottom: 8};
        var marginRight = {marginRight: 5};
        var marginBottom20 = {marginBottom: 20};
        return (
                <div className="row">
                    <div className="col-md-8 centered" style={height60}>
                        <div className="panel panel-primary">
                            <div className="panel-heading">
                                <h1 className="panel-title">{ this.state.title }</h1>
                            </div>

                            <div itemProp="audience" itemScope itemType="http://schema.org/PeopleAudience" className="panel-body">
                                <div className="row centered" id="player" style={marginBottom20}>
                                    <video width="100%" controls autoPlay key={this.state.embed}>
                                        <source src={this.state.embed} />
                                    </video>
                                </div>
                                <div style={marginBottom}>
                                    <span className="label label-success">Description</span>
                                    <p>{ this.state.desc }</p>
                                </div>
                                <div style={marginBottom}>
                                    <span className="label label-primary">Duration: { this.state.duration }</span>
                                    <span className="label label-danger">{ this.state.views } Views</span>
                                </div>
                                <div>
                                    {DocumentCategoriesNodes}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        );
    }
});