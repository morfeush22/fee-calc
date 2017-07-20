class Report extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      posts: []
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
  <Report />,
  document.getElementById('report')
);

ReactDOM.render(
  <SummarizedReport />,
  document.getElementById('summarized_report')
);
