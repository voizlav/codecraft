const dates = document.querySelectorAll(".historydate")

for (i = 0; i < dates.length; i++) {
  const offset = new Date().getTimezoneOffset();
  const utcDate = new Date(dates[i].innerText);
  const localDate = new Date(utcDate.getTime() - offset * 60000);
  const diff = new Date().getTime() - localDate.getTime();

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diff % (1000 * 60)) / 1000) + 1;

  let timeAgo;
  if (days > 0) {
    timeAgo = `${days} day${days > 1 ? 's' : ''} ago`;
  } else if (hours > 0) {
    timeAgo = `${hours} hour${hours > 1 ? 's' : ''} ago`;
  } else if (minutes > 0) {
    timeAgo = `${minutes} minute${minutes > 1 ? 's' : ''} ago`;
  } else {
    timeAgo = `${seconds} second${seconds > 1 ? 's' : ''} ago`;
  }
  dates[i].innerText = timeAgo;
}