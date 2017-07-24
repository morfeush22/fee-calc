class List extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      list: []
    };
  }

  componentDidMount() {
    axios.get("/api/list")
      .then(res => {
        const fees = res.data;
        this.setState({list: fees});
        console.log(fees);
      });
  }

  render() {
    var rows = [];
    for (let i = 0; i < this.state.list.length; ++i) {
        let [payee, acceptor, fee] = this.state.list[i]
        rows.push(
            <tr key={payee + acceptor + i}>
                <td>{payee}</td>
                <td>{acceptor}</td>
                <td>{fee}</td>
            </tr>
        );
    }
    return (
      <div>
        <table className="table table-bordered">
            <thead>
                <tr>
                <th>Payee</th>
                <th>Acceptor</th>
                <th>Fee</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
      </div>
    );
  }
}

class Report extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      report: []
    };
  }

  componentDidMount() {
    axios.get("/api/report")
      .then(res => {
        const fees = res.data;
        this.setState({report: fees});
      });
  }

  render() {
    var rows = [];
    for (var payee in this.state.report) {
        for (var acceptor in this.state.report[payee])
            rows.push(
                <tr key={payee + acceptor}>
                    <td>{payee}</td>
                    <td>{acceptor}</td>
                    <td>{this.state.report[payee][acceptor]}</td>
                </tr>
        );
    }
    return (
      <div>
        <table className="table table-bordered">
            <thead>
                <tr>
                <th>Payee</th>
                <th>Acceptor</th>
                <th>Fee</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
      </div>
    );
  }
}

class SummarizedReport extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      report: {}
    };
  }

  componentDidMount() {
    axios.get("/api/summarized_report")
      .then(res => {
        const fees = res.data;
        this.setState({report: fees});
      });
  }

  render() {
    var rows = [];
    for (var item in this.state.report) {
        rows.push(
            <tr key={item}>
                <td>{item}</td>
                <td>{this.state.report[item]}</td>
            </tr>
        );
    }
    return (
      <div>
        <table className="table table-bordered">
            <thead>
                <tr>
                <th>Acceptor</th>
                <th>Fee</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
      </div>
    );
  }
}

ReactDOM.render(
  <List />,
  document.getElementById('list')
);

ReactDOM.render(
  <Report />,
  document.getElementById('report')
);

ReactDOM.render(
  <SummarizedReport />,
  document.getElementById('summarized_report')
);
