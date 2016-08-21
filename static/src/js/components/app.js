import React, { Component } from 'react';

import api from '../api';
import CalenderList from './calender';
import RecipeList from './recipes';


export const App = React.createClass({
    getInitialState: function () {
        return {
            requestedData: false,
            calenderData: [],
            recipeData: []
        };
    },
    componentDidMount: function () {
        api.get('dates')
            .catch(() => this.setState({
                requestedData: true
            }))
            .then((response) => this.setState({
                requestedData: true,
                calenderData: response
            }));

        api.get('recipes')
            .catch(() => this.setState({
                requestedData: true
            }))
            .then((response) => this.setState({
                requestedData: true,
                recipeData: response
            }));
    },
    render: function () {
        if (this.state.calenderData.length) {
            return (
                <div>
                    <a href="/" className="logo">C8O</a>
                    <CalenderList data={this.state.calenderData} />
                    <RecipeList data={this.state.recipeData} />
                </div>
            );
        } else {
            return <div>loading...</div>;
        }
    }
});
