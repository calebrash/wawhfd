import React, { Component } from 'react';
import api from '../api';

export default class CalenderList extends Component {
    getCalenderItems () {
        return this.props.data.map((d) => <CalenderItem data={d} key={d.key} />);
    }
    render () {
        return <div className="calender">{this.getCalenderItems()}</div>;
    }
}

class CalenderItem extends Component {
    constructor (props) {
        super(props);
        this.state = props.data;
        this.state.over = false;
        this.onDragEnter = this.onDragEnter.bind(this);
        this.onDragLeave = this.onDragLeave.bind(this);
        this.onDrop = this.onDrop.bind(this);
        this.onClickDelete = this.onClickDelete.bind(this);

        this.dragCounter = 0;
    }
    onDragEnter (e) {
        e.preventDefault();
        this.dragCounter ++;
        this.setState({
            over: true
        });
    }
    onDragLeave (e) {
        this.dragCounter --;
        if (this.dragCounter === 0) {
            this.setState({
                over: false
            });
        }
    }
    onDragOver (e) {
        e.preventDefault();
    }
    onDrop (e) {
        let recipe = JSON.parse(e.dataTransfer.getData('text/plain'));
        api.post(`dates/${this.state.date}/edit`, recipe).then(this.setState({
            over: false,
            recipe: recipe
        }));
    }
    onClickDelete (e) {
        e.preventDefault();
        api.post(`dates/${this.state.date}/delete`).then(this.setState({
            recipe: null
        }));
    }
    getClassNames () {
        let classes = 'calender-item row';
        if (!this.state.recipe || this.state.over) {
            classes += ' droppable';
        }
        if (this.state.over) {
            classes += ' drag-over';
        }
        return classes;
    }
    renderReceipe () {
        if (this.state.recipe) {
            return (
                <p>
                    {this.state.recipe.name}
                    <a href="#" onClick={this.onClickDelete}>&times;</a>
                </p>
            );
        }
        return '';
    }
    render () {
        return (
            <div className={this.getClassNames()} onDragEnter={this.onDragEnter} onDragLeave={this.onDragLeave}>
                <h2 title={this.state.date_string}>{this.state.title}</h2>
                <div className="drop-target" onDragOver={this.onDragOver} onDrop={this.onDrop}>
                    Drop recipe here
                </div>
                <div className="recipe">
                    {this.renderReceipe()}
                </div>
            </div>
        );
    }
}
