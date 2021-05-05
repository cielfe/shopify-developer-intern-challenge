async function getCollectionNames() {
  const url = "http://localhost:5000/api/collection"
  const argumentsForFetch = {
    method: "GET"
  }

  const response = await fetch(url, argumentsForFetch);
  const jsonResponse = await response.json();
 
  if (response.status >= 200 && response.status <= 299) {
    const successMessage = `${response.status} ${response.statusText}`;
    let options = jsonResponse.collections;


    //create the collection options
    let collectionList = document.getElementById('collection-list');
  

    options.forEach(function(item) {
      var option = document.createElement('option');
      option.value = item;
      option.innerHTML = item;
      collectionList.appendChild(option);
    });
  }
  else{
     // Handle errors
     const errorMessage = `${response.status} ${response.statusText} `;
     let userFeedback = jsonResponse.message;
     console.log(`An error occurred => ${errorMessage}`);
  }
}

getCollectionNames();