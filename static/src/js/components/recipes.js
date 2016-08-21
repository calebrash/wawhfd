import React, { Component } from 'react';

export default class RecipeList extends Component {
    constructor (props) {
        super(props);
        this.state = {
            recipes: this.props.data,
            isAdding: false
        };
        this.startAdding = this.startAdding.bind(this);
    }
    startAdding () {
        this.setState({
            isAdding: true
        });
    }
    recipeStore () {
        return {
            cancelAdding: () => this.setState({
                isAdding: false
            }),
            add: (recipe) => {
                let recipes = this.state.recipes;
                recipe.id = recipes.length;
                recipe.key = btoa(Math.random() * 1000);
                recipes.push(recipe);
                this.setState({
                    recipes: recipes,
                    isAdding: false
                });
            }
        }
    }
    getAddRecipeForm () {
        if (this.state.isAdding) {
            return (
                <AddRecipeForm recipeStore={this.recipeStore()} />
            );
        }
        return '';
    }
    getRecipeItems () {
        return this.state.recipes.map((d) => <RecipeItem data={d} key={d.key} />);
    }
    getAddButtonClassName () {
        var className = 'btn-link';
        if (this.state.isAdding) {
            className += ' disabled';
        }
        return className;
    }
    render () {
        return (
            <div className="recipes">
                <header className="recipes-header">
                    <button className={this.getAddButtonClassName()} onClick={this.startAdding}>Add recipe</button>
                    <h2>Recipes</h2>
                </header>
                {this.getAddRecipeForm()}
                <div className="recipe-search">
                    <input type="text" />
                </div>
                <ul>
                    {this.getRecipeItems()}
                </ul>
            </div>
        );
    }
}

class AddRecipeForm extends Component {
    constructor (props) {
        super(props);
        this.state = {
            name: ''
        };
        this.cancelAdding = this.cancelAdding.bind(this);
        this.onInputName = this.onInputName.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    onSubmit (e) {
        e.preventDefault();
        this.props.recipeStore.add({
            name: this.state.name
        });
    }
    onInputName (e) {
        this.setState({
            name: e.target.value
        });
    }
    cancelAdding () {
        this.props.recipeStore.cancelAdding();
    }
    render () {
        return (
            <form action="/api/recipe/add/" method="POST" onSubmit={this.onSubmit} className="recipes-add">
                <input type="text" placeholder="name" value={this.state.name} onInput={this.onInputName} />
                <div className="row">
                    <button className="btn">Save</button>
                    <a href="#" className="btn-link" onClick={this.cancelAdding}>Cancel</a>
                </div>
            </form>
        );
    }
}

const RecipeItem = React.createClass({
    onSubmit: function () {
        console.log('SUBMIT');
    },
    startEditing: function () {
        this.setState({
            isEditing: true
        });
    },
    cancelEditing: function () {
        this.setState({
            isEditing: false
        });
    },
    getInitialState: function () {
        return {
            isEditing: false
        };
    },
    render: function () {
        if (this.state.isEditing) {
            let formUrl = `/api/recipe/${this.props.data.id}/edit/`;
            return (
                <li className="recipe row form">
                    <form action={formUrl} method="POST" onSubmit={this.onSubmit}>
                        <input type="text" name={this.props.data.name} />
                        <button className="btn">Save</button>
                        <a href="#" className="btn" onClick={this.cancelEditing}>Cancel</a>
                    </form>
                </li>
            );
        } else {
            return (
                <li className="recipe row" onClick={this.startEditing}>
                    {this.props.data.name}
                </li>
            );
        }
    }
});
