import React, { Component } from 'react';

import api from '../api';
import CalenderList from './calender';
import RecipeList from './recipes';


export default class App extends Component {
    constructor (props) {
        super(props);
        this.state = {
            calenderData: null,
            recipeData: null
        };
    }
    componentDidMount () {
        api.get('dates')
            .then((response) => this.setState({
                calenderData: response
            }));

        api.get('recipes')
            .then((response) => this.setState({
                requestedData: true,
                recipeData: response
            }));
    }
    getCalender () {
        if (this.state.calenderData !== null) {
            return <CalenderList data={this.state.calenderData} />;
        } else {
            return <div className="calender">loading...</div>;
        }
    }
    getRecipes () {
        if (this.state.recipeData !== null) {
            return <RecipeList data={this.state.recipeData} />;
        } else {
            return <div className="recipes loading">loading...</div>;
        }
    }
    render () {
        return (
            <div>
                <a href="/" className="logo">C8O</a>
                {this.getCalender()}
                {this.getRecipes()}
            </div>
        );
    }
}
