let chart;
async function loadData(){
  const res = await fetch('/dashboard-data');
  const data = await res.json();
  const labels = Object.keys(data);
  const counts = Object.values(data);
  if(chart) chart.destroy();
  const ctx = document.getElementById('sentChart').getContext('2d');
  chart = new Chart(ctx, {
    type: 'pie',
    data: { labels, datasets:[{ data:counts }] },
    options:{ responsive:true }
  });
}
window.onload = loadData;
