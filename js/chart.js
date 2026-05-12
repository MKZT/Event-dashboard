```js id="i0z8mt"
// chart.js

export function getEventChartData(events) {
  const categoryMap = {};
  const cityMap = {};
  const statusMap = {};

  events.forEach((event) => {
    // Category Chart
    categoryMap[event.category] =
      (categoryMap[event.category] || 0) + 1;

    // City Chart
    cityMap[event.city] =
      (cityMap[event.city] || 0) + 1;

    // Status Chart
    statusMap[event.status] =
      (statusMap[event.status] || 0) + 1;
  });

  const categoryChart = Object.keys(categoryMap).map(
    (category) => ({
      name: category,
      total: categoryMap[category],
    })
  );

  const cityChart = Object.keys(cityMap).map((city) => ({
    name: city,
    total: cityMap[city],
  }));

  const statusChart = Object.keys(statusMap).map(
    (status) => ({
      name: status,
      total: statusMap[status],
    })
  );

  return {
    categoryChart,
    cityChart,
    statusChart,
  };
}
```
