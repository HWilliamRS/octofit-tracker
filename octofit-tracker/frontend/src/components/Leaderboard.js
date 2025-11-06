import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Leaderboard API endpoint:', endpoint);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-10">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <h2 className="card-title mb-4 text-center">Leaderboard</h2>
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-light">
                  <tr>
                    <th>#</th>
                    <th>Name</th>
                  </tr>
                </thead>
                <tbody>
                  {leaderboard.map((entry, idx) => (
                    <tr key={entry.id || idx}>
                      <td>{idx + 1}</td>
                      <td>{entry.name || JSON.stringify(entry)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
