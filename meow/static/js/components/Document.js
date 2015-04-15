'use strict';

import React from 'react';
import _ from 'lodash';
import truncate from 'html-truncate';
import Router from 'react-router';
import WebAPIMixin from '../mixins/WebAPIMixin';


const Link = Router.Link;

export default React.createClass({
    propTypes: {
        id: React.PropTypes.number.isRequired,
        title: React.PropTypes.string.isRequired,
        categories: React.PropTypes.array.isRequired
        duration: React.PropTypes.string.is.Required,
        images: React.PropTypes.array.isRequired
    },
    contextTypes: {
        router: React.PropTypes.func
    },
    handleClick() {
        this.context.router.transitionTo('post', {postId: this.props.id});
    },
    render() {
        return (
            <div className="tile" onClick={this.handleClick}>
                <img src={this.props.cover.img.medium} style={styles.tileImg}></img>
                <div className="intro" >
                    <div className="info" style={styles.tileIntroInfo}>
                        { this.props.category} | {new Date(this.props.created_at).toDateString()}
                    </div>
                    <div className="heading" style={styles.tileIntroHeading}>
                        {this.props.zh_title}
                    </div>
                    <div className="sub-heading" style={styles.tileIntroSubHeading}>
                        {this.props.en_title}
                    </div>

                    <div className="divider" style={styles.tileIntroDivider}>
                        <span className="twin circle-divider" style={styles.circleDivider}></span>
                        <span className="twin circle-divider" style={styles.circleDivider}></span>
                    </div>

                    <div className="synopsis" style={styles.tileIntroSynopsis} 
                        dangerouslySetInnerHTML={{__html: truncate(this.props.content, 50)}}>
                    </div>
                </div>
                <div className="triangle" style={styles.tileTriangle}></div>
            </div>
        );
    }
});