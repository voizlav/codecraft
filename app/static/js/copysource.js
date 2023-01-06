async function getSourceFromRoute(route) {
  const response = await fetch(route);
  return response.text();
}

function copySource(button, icon, getSource) {
  button.addEventListener("click", async () => {
    try {
      const source = await getSource();
      await navigator.clipboard.writeText(source);
      
      icon.textContent = "check_circle";
      setTimeout(() => {
        icon.textContent = "content_copy";
      }, 1500);
    } catch (error) {
      console.error(error);
    }
  });
}

const copyButtons = document.querySelectorAll(".copybutton");
const copyIcons = document.querySelectorAll(".copyicon");

for (let i = 0; i < copyButtons.length; i++) {
  const copyButton = copyButtons[i];
  const copyIcon = copyIcons[i];
  const route = copyButton.getAttribute("dataroute");
  
  copySource(copyButton, copyIcon, () => getSourceFromRoute(route));
}