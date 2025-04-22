function zoomImage(img) {
    let modal = document.createElement('div');
    modal.style.display = 'flex';
    modal.style.position = 'fixed';
    modal.style.left = '0';
    modal.style.top = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    
    let zoomedImage = document.createElement('img');
    zoomedImage.src = img.src;
    zoomedImage.style.maxWidth = '90%';
    zoomedImage.style.maxHeight = '90%';

    modal.appendChild(zoomedImage);
    document.body.appendChild(modal);

    modal.onclick = function() {
        document.body.removeChild(modal);
    };
}