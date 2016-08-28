import React, { Component } from 'react';
import api from '../api';

let canonicalRecipes;
let currentFilterText = '';
let filteredCanonicalRecipes = () => {
    return canonicalRecipes.filter((recipe) => {
        let searchText = (`${recipe.name} ${recipe.description}`).toLowerCase();
        return searchText.indexOf(currentFilterText) >= 0
    });
};

export default class RecipeList extends Component {
    constructor (props) {
        super(props);
        this.state = {
            recipes: props.data,
            isAdding: false
        };
        this.recipeStore = this.getRecipeStore();
        this.startAdding = this.startAdding.bind(this);
        canonicalRecipes = props.data;
    }
    componentWillReceiveProps (props) {
        this.setState({
            recipes: props.data
        });
        canonicalRecipes = props.data;
    }
    startAdding () {
        this.setState({
            isAdding: true
        });
    }
    getRecipeStore () {
        let genericResponseHandler = (response) => {
            canonicalRecipes = response;
            this.props.updateHandler(canonicalRecipes);
        };
        return {
            cancelAdding: () => this.setState({
                isAdding: false
            }),
            add: (recipe) => {
                api.post('recipes/add', recipe).then((response) => {
                    canonicalRecipes = response;
                    this.setState({
                        recipes: canonicalRecipes,
                        isAdding: false
                    })
                });
            },
            edit: (recipe) => {
                api.post(`recipes/${recipe.id}/edit`, recipe).then(genericResponseHandler);
            },
            delete: (recipe) => {
                api.post(`recipes/${recipe.id}/delete`, recipe).then(genericResponseHandler);
            },
            search: (text) => {
                currentFilterText = text.toLowerCase();
                this.setState({
                    recipes: filteredCanonicalRecipes()
                });
            }
        }
    }
    getAddRecipeForm () {
        if (this.state.isAdding) {
            return (
                <AddRecipeForm recipeStore={this.recipeStore} />
            );
        }
        return '';
    }
    getRecipeItems () {
        return this.state.recipes.map((d) => <RecipeItem data={d} key={d.key} recipeStore={this.recipeStore} />);
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
                    <button className={this.getAddButtonClassName()} onClick={this.startAdding}>
                        Add recipe
                    </button>
                    <h2>Recipes</h2>
                </header>
                {this.getAddRecipeForm()}
                <RecipeSearchInput recipeStore={this.recipeStore} />
                <ul className="recipe-list">
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
            name: '',
            description: '',
            link: ''
        };
        this.cancelAdding = this.cancelAdding.bind(this);
        this.inputHandler = this.inputHandler.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    onSubmit (e) {
        e.preventDefault();
        this.props.recipeStore.add(this.state);
    }
    inputHandler (field) {
        return (e) => {
            this.setState({
                [field]: e.target.value
            });
        };
    }
    cancelAdding () {
        this.props.recipeStore.cancelAdding();
    }
    render () {
        return (
            <form action="#" method="POST" onSubmit={this.onSubmit} className="recipes-add">
                <label htmlFor="recipe-new-name">Name</label>
                <input type="text"
                    id="recipe-new-name"
                    placeholder="name"
                    value={this.state.name}
                    onChange={this.inputHandler('name')}
                    autoComplete="off" />

                <label htmlFor="recipe-new-description">Description</label>
                <input type="text"
                    id="recipe-new-description"
                    placeholder="description"
                    value={this.state.description}
                    onChange={this.inputHandler('description')}
                    autoComplete="off" />

                <label htmlFor="recipe-new-link">Link</label>
                <input type="text"
                    id="recipe-new-link"
                    placeholder="link"
                    value={this.state.link}
                    onChange={this.inputHandler('link')}
                    autoComplete="off" />

                <div className="row">
                    <button className="btn">Save</button>
                    <a href="#" className="btn-link" onClick={this.cancelAdding}>Cancel</a>
                </div>
            </form>
        );
    }
}

class RecipeSearchInput extends Component {
    constructor (props) {
        super(props);
        this.state = {
            value: ''
        };
        this.onInput = this.onInput.bind(this);
    }
    onInput (e) {
        let value = e.target.value;
        this.setState({
            value: value
        });
        this.props.recipeStore.search(value);
    }
    render () {
        return (
            <div className="recipe-search">
                <input type="text"
                    placeholder="Search"
                    value={this.state.value}
                    onInput={this.onInput}
                    autoComplete="off" />
            </div>
        );
    }
}

class RecipeItem extends Component {
    constructor (props) {
        super(props);

        this.state = this.props.data;
        this.state.isEditing = false;

        this.onSubmit = this.onSubmit.bind(this);
        this.onDelete = this.onDelete.bind(this);
        this.onDragStart = this.onDragStart.bind(this);
        this.startEditing = this.startEditing.bind(this);
        this.cancelEditing = this.cancelEditing.bind(this);
        this.inputHandler = this.inputHandler.bind(this);
    }
    onSubmit (e) {
        e.preventDefault();
        this.setState({
            isEditing: false
        });
        this.props.recipeStore.edit(this.state);
    }
    onDelete () {
        this.props.recipeStore.delete(this.state);
    }
    onDragStart (e) {
        e.dataTransfer.setData('text/plain', JSON.stringify(this.state));
    }
    inputHandler (field) {
        return (e) => {
            let state = {};
            state[field] = e.target.value;
            this.setState(state);
        };
    }
    onClickLink (e) {
        e.stopPropagation();
    }
    startEditing () {
        this.setState({
            isEditing: true
        });
    }
    cancelEditing () {
        this.setState({
            isEditing: false
        });
    }
    getDescription () {
        if (this.state.description) {
            return <p className="description">{this.state.description}</p>
        }
        return '';
    }
    getLink () {
        if (this.state.link) {
            return (
                <p className="link">
                    <a href={this.state.link} onClick={this.onClickLink} target="_blank">
                        {this.state.link}
                    </a>
                </p>
            );
        }
        return '';
    }
    render () {
        if (this.state.isEditing) {
            return (
                <li className="recipe row form">
                    <form action="#" method="POST" onSubmit={this.onSubmit}>
                        <label htmlFor={`recipe-${this.state.id}-name`}>Name</label>
                        <input type="text"
                            id={`recipe-${this.state.id}-name`}
                            placeholder="Name"
                            value={this.state.name}
                            onChange={this.inputHandler('name')}
                            autoComplete="off" />

                        <label htmlFor={`recipe-${this.state.id}-description`}>Description</label>
                        <input type="text"
                            id={`recipe-${this.state.id}-description`}
                            placeholder="description"
                            value={this.state.description || ''}
                            onChange={this.inputHandler('description')}
                            autoComplete="off" />

                        <label htmlFor={`recipe-${this.state.id}-link`}>Link</label>
                        <input type="text"
                            id={`recipe-${this.state.id}-link`}
                            placeholder="Link"
                            value={this.state.link || ''}
                            onChange={this.inputHandler('link')}
                            autoComplete="off" />

                        <div className="row">
                            <button className="btn">Save</button>
                            <a href="#" className="btn-link" onClick={this.cancelEditing}>Cancel</a>
                            <a href="#" className="btn-link danger" onClick={this.onDelete}>Delete</a>
                        </div>
                    </form>
                </li>
            );
        } else {
            return (
                <li className="recipe row" onClick={this.startEditing} draggable="true" onDragStart={this.onDragStart}>
                    <h4>{this.props.data.name}</h4>
                    {this.getDescription()}
                    {this.getLink()}
                </li>
            );
        }
    }
}
