import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to restq</h2>
        </div>
        <p className="App-intro">
          This is a restful queue
        </p>
        <p>
          A restful queue can be used for any type of information that needs a
          temporary storage. We use it for batch processing:
        </p>
        <p>
        <code>
        joakim@forsmark:~$ curl -X POST http://localhost/rest_api/
        &#123;
        "project": "131ea961-95c8-4db9-bd52-4ebd27885efc"
        &#125;
        </code>
        </p>
        <p>
        <code>
        curl -H "Content-Type:application/json" -X PUT -d'&#123;	"data":42&#125;	' http://localhost/rest_api/131ea961-95c8-4db9-bd52-4ebd27885efc
&#123;
  "data": 42
&#125;
        </code>
        </p>
        <p>
        <code>
        curl -X GET http://localhost/rest_api/131ea961-95c8-4db9-bd52-4ebd27885efc
        &#123;
  "data": 42
&#125;

        </code>
        </p>
      </div>
    );
  }

  handle_draw() {
    console.log('clicked')
  }
}

export default App;
