import React, { Component } from 'react';

import api from '../api';
import CalendarList from './calendar';
import RecipeList from './recipes';


export default class App extends Component {
    constructor (props) {
        super(props);
        this.state = {
            calendarData: null,
            recipeData: null
        };
        this.refreshCalendar = this.refreshCalendar.bind(this);
    }
    componentDidMount () {
        this.refreshCalendar();
        this.refreshRecipes();
    }
    refreshCalendar (handler) {
        if (!handler) {
            handler = (response) => this.setState({
                calendarData: response.data
            });
        }
        api.get('dates').then(handler);
    }
    updateHandler () {
        return (recipeData) => {
            this.refreshCalendar((response) => {
                this.setState({
                    calendarData: response.data,
                    recipeData: recipeData
                })
            });
        };
    }
    refreshRecipes () {
        api.get('recipes').then((response) => this.setState({
            requestedData: true,
            recipeData: response.data
        }));
    }
    getCalendar () {
        if (this.state.calendarData !== null) {
            return <CalendarList data={this.state.calendarData} />;
        } else {
            return <div className="calendar loading">...</div>;
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
                {this.getCalendar()}
                {this.getRecipes()}
            </div>
        );
    }
}
