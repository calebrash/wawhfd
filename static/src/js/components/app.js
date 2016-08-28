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
        this.refreshCalender = this.refreshCalender.bind(this);
    }
    componentDidMount () {
        this.refreshCalender();
        this.refreshRecipes();
    }
    refreshCalender (handler) {
        if (!handler) {
            handler = (response) => this.setState({
                calenderData: response
            });
        }
        api.get('dates').then(handler);
    }
    updateHandler () {
        return (recipeData) => {
            this.refreshCalender((response) => {
                this.setState({
                    calenderData: response,
                    recipeData: recipeData
                })
            });
        };
    }
    refreshRecipes () {
        api.get('recipes').then((response) => this.setState({
            requestedData: true,
            recipeData: response
        }));
    }
    getCalender () {
        if (this.state.calenderData !== null) {
            return <CalenderList data={this.state.calenderData} />;
        } else {
            return <div className="calender loading">...</div>;
        }
    }
    getRecipes () {
        if (this.state.recipeData !== null) {
            return <RecipeList data={this.state.recipeData} updateHandler={this.updateHandler()} />;
        } else {
            return <div className="recipes loading">...</div>;
        }
    }
    render () {
        return (
            <div>
                <a href="/" className="logo">wawhfd.</a>
                {this.getCalender()}
                {this.getRecipes()}
            </div>
        );
    }
}
