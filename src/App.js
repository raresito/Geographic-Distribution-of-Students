import React, { Component } from 'react';
import logo from './logo.svg';
import { Switch, Route } from 'react-router-dom';
import './sass/App.scss';
import HomePage from './home/HomePage.jsx';
import UniversityHome from './university/UniversityHome.jsx';
import GovernmentHome from './government/GovernmentHome.jsx';

class App extends Component {
  render() {
    return (
        <Switch>
          <Route exact path='/' component={HomePage}/>
          <Route path="/uni" component={UniversityHome} />
          <Route path="/gov" component={GovernmentHome} />
        </Switch>
      )}
}

export default App;