import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities API endpoint:', endpoint);
        console.log('Fetched activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-10">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <h2 className="card-title mb-4 text-center">Activities</h2>
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-light">
                  <tr>
                    <th>#</th>
                    <th>Name</th>
                  </tr>
                </thead>
                <tbody>
                  {activities.map((activity, idx) => (
                    <tr key={activity.id || idx}>
                      <td>{idx + 1}</td>
                      <td>{activity.name || JSON.stringify(activity)}</td>
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

export default Activities;
