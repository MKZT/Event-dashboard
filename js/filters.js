// filter.js

export function filterEvents(events, filters) {
  return events.filter((event) => {
    // Search Filter
    const matchesSearch =
      !filters.search ||
      event.title
        .toLowerCase()
        .includes(filters.search.toLowerCase());

    // Category Filter
    const matchesCategory =
      !filters.category ||
      event.category === filters.category;

    // City Filter
    const matchesCity =
      !filters.city ||
      event.city === filters.city;

    // Date Filter
    const matchesDate =
      !filters.date ||
      new Date(event.date).toDateString() ===
        new Date(filters.date).toDateString();

    // Status Filter
    const matchesStatus =
      !filters.status ||
      event.status === filters.status;

    // Final Result
    return (
      matchesSearch &&
      matchesCategory &&
      matchesCity &&
      matchesDate &&
      matchesStatus
    );
  });
}