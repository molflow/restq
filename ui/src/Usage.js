import React from 'react';
import marked from "marked";
import 'github-markdown-css/github-markdown.css';
import './Usage.css'


class Usage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {};
  }

  componentWillMount() {
    const readmePath = require("./README.md");

    fetch(readmePath)
      .then(response => {
        return response.text()
      })
      .then(text => {
        this.setState({
          markdown: marked(text)
        })
      })
  }

  render() {
    const { markdown } = this.state;
    return (
      <section className="markdown-body">
        <article dangerouslySetInnerHTML={{__html: markdown}}></article>
      </section>
    )
  }
}

export default Usage;
