async function sendMsg(){
  const box=document.getElementById("chat-box");
  const inp=document.getElementById("chat-input");
  const text=inp.value.trim();
  if(!text) return;
  box.innerHTML += `<div class="chat-bubble bubble-user ms-auto">${text}</div>`;
  inp.value="";
  const res=await fetch("/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:text})});
  const data=await res.json();
  box.innerHTML += `<div class="chat-bubble bubble-bot">${data.response}</div>`;
  box.scrollTop=box.scrollHeight;
}

async function submitFb(){
  const txtArea=document.getElementById("fb");
  const text=txtArea.value.trim();
  if(!text) return alert("Type feedback first!");
  const res=await fetch("/feedback",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({text})});
  const d=await res.json();
  alert("Sentiment recorded as: "+d.sentiment);
  txtArea.value="";
}
