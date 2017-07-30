class DescriptionBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            style: {
                display: "none"
            }
        };
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.hidden)
            this.setState({style: {display: "none"}});
        else
            this.setState({style: {display: "block"}});
    }

    render() {
        return (
            <div className="row" style={this.state.style}>
                <div className="col-md-12">{this.props.description}</div>
            </div>
        )
    }
}

class Fee extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            expanded: false
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(prevState => ({
            expanded: !prevState.expanded
        }));
    }

    render() {
        return (
            <div className="row" onClick={this.handleClick}>
                <div className="col-md-4">{this.props.payee}</div>
                <div className="col-md-4">{this.props.acceptor}</div>
                <div className="col-md-4">{this.props.balance}</div>
                <DescriptionBox description={this.props.others.description} hidden={!this.state.expanded} />
            </div>
        )
    }
}

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
      });
  }

  render() {
    var rows = [];
    for (let i = 0; i < this.state.list.length; ++i) {
        let {payee, acceptor, balance, ...others} = this.state.list[i];
        rows.push(
            <Fee payee={payee} acceptor={acceptor} balance={balance} others={others} key={"fee-" + i} />
        );
    }
    return (
      <div>
        <div className="row">
            <div className="col-md-4">Payee</div>
            <div className="col-md-4">Acceptor</div>
            <div className="col-md-4">Balance</div>
        </div>
        {rows}
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
