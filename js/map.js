// map.js

export function getEventMapData(events) {
  return events.map((event) => ({
    id: event.id,
    title: event.title,
    category: event.category,
    city: event.city,
    venue: event.venue,
    date: event.date,
    status: event.status,

    // Coordinates
    latitude: event.latitude,
    longitude: event.longitude,

    // Marker Info
    marker: {
      title: event.title,
      description: `${event.category} event in ${event.city}`,
    },
  }));
}