const closeAlert = () => {
    const alertElement = document.getElementById("alert");
    if (alertElement) {
        alertElement.style.display = "none";
    }
};

const gotoShard = (link) => {
    const shardURL = `/shards${link}`;
    window.location.href = shardURL;
};

const openRawShard = (link) => {
    const shardURL = `https://storage.googleapis.com/infoshards.appspot.com/public${link}.json`;
    window.open(shardURL);
};

const openPrettyShard = (link) => {
    const shardURL = `/shards/view?link=${encodeURIComponent(link)}`;
    window.open(shardURL);
}

const copyShard = (link) => {
    const shardURL = `https://storage.googleapis.com/infoshards.appspot.com/public${link}.json`;
    navigator.clipboard.writeText(shardURL)
        .then(() => {
            window.alert("Copied to clipboard!")
        })
        .catch((error) => {
            window.alert(`Couldn't copy to clipboard... ${error}`)
        });
};
