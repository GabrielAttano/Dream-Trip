import React from 'react';
import { Switch, Route } from 'react-router-dom';

import CreatePackage from '../pages/createPackage';
import UserInfo from '../pages/userInfo';

export default function Routes() {
  return (
    <Switch>
      <Route exact path="/" component={CreatePackage} />
      <Route path="/userinfo" component={UserInfo} />
    </Switch>
  );
}
