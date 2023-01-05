const DATASIZE = 2900

function measureTextSizeInBytes(text) {
  const encoder = new TextEncoder();
  const bytes = encoder.encode(text);

  return bytes.byteLength;
}

const textarea = document.getElementById("newcodebox");

let text = textarea.value;
let sizeInKB = measureTextSizeInBytes(text) / 1024;

let measurementElement = document.getElementById("sizeMeasurement");
measurementElement.innerText = sizeInKB.toFixed(2) + " KB";
measurementElement.className = "badge rounded-pill bg-secondary";
measurementElement.title = "the source does not contain any data";

textarea.addEventListener("input", function() {

  text = textarea.value;
  sizeInKB = measureTextSizeInBytes(text) / 1024
  const sizeInBytes = measureTextSizeInBytes(text);
  const compressedInput = pako.deflate(text, {level: 9});
  const compressedInputSize = compressedInput.length;

  measurementElement.innerText = sizeInKB.toFixed(2) + " KB";
  if (sizeInBytes === 0) {
    measurementElement.className = "badge rounded-pill bg-secondary";
    measurementElement.title = "the source does not contain any data";
  } else if (sizeInBytes < DATASIZE) {
    measurementElement.className = "badge rounded-pill bg-success";
    measurementElement.title = "the size of the source is allowed";
  } else if (compressedInputSize < DATASIZE) {
    measurementElement.className = "badge rounded-pill bg-warning text-dark";
    measurementElement.title = "the source will be compressed";
  } else {
    measurementElement.className = "badge rounded-pill bg-danger";
    measurementElement.title = "the source exceeds the allowed limits";
  }
});