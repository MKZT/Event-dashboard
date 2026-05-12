// ui.js

export function formatEventCard(event) {
  return {
    id: event.id,
    title: event.title,
    category: event.category,
    city: event.city,
    venue: event.venue,
    date: formatDate(event.date),
    status: formatStatus(event.status),

    badgeColor: getBadgeColor(event.status),

    image:
      event.image ||
      "/images/default-event.jpg",
  };
}

// =========================
// FORMAT DATE
// =========================

export function formatDate(date) {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

// =========================
// FORMAT STATUS
// =========================

export function formatStatus(status) {
  return status.charAt(0).toUpperCase() +
    status.slice(1);
}

// =========================
// BADGE COLORS
// =========================

export function getBadgeColor(status) {
  switch (status) {
    case "active":
      return "green";

    case "inactive":
      return "red";

    case "upcoming":
      return "blue";

    default:
      return "gray";
  }
}