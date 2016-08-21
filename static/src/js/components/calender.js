import React, { Component } from 'react';

export default class CalenderList extends Component {
    getCalenderItems () {
        return this.props.data.map((d) => <CalenderItem data={d} key={d.key} />);
    }
    render () {
        return <div className="calender">{this.getCalenderItems()}</div>;
    }
}

class CalenderItem extends Component {
    render () {
        return (
            <div className="calender-item row">
                <h2>{this.props.data.title}<small>{this.props.data.date_string}</small></h2>
                <p>{this.props.data.content}</p>
            </div>
        );
    }
}
