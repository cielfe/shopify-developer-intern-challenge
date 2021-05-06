

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

async function loadGallery() {
  const UPLOAD_FOLDER = './uploads';
  const url = "http://localhost:5000/api/photo"
  const argumentsForFetch = {
    method: "GET"
  }

  const response = await fetch(url, argumentsForFetch);
  const jsonResponse = await response.json();

  if (response.status >= 200 && response.status <= 299) {
    const successMessage = `${response.status} ${response.statusText}`;
  
    // //create the collection options
    let photoDisplayParent = document.getElementById("photo-gallery");
    let collections = Object.keys(jsonResponse);
    for (var i = 0; i < collections.length;i++){

    //   <div id="collection1">
    //   <h3>Toronto</h3>
    //   <img src="./uploads/vacation/venice.png"  style="width:10%;height:10%;">
    // </div>
      //create a new element for each collection
      var collectionDiv = document.createElement('div');
      collectionDiv.id =  collections[i];
      
      //only give titles all elements except the first one
      if (i > 0){
        var collTitle = document.createElement('h3');
        collTitle.innerHTML = collections[i];
        collectionDiv.appendChild(collTitle);

      }
      //append all the photos in the current collection to a parent div
      console.log("collection "+ collections[i]);
      photos = jsonResponse[collections[i]];

      //create figure and image elements for each photo

      photos.forEach(function(item) {
          var figure = document.createElement('figure');
          var image = document.createElement('img');

          let src_path = UPLOAD_FOLDER+'/'+item;
          if (i > 0){
            src_path = UPLOAD_FOLDER+'/'+collections[i]+'/'+item;
          }
          console.log("src_path "+ src_path);

          image.src = src_path;

          image.style = "width:10%;height:10%;padding:5px;";
          //add image and caption as children to figure
          //create a caption
          var caption = document.createElement('figcaption');
          caption.innerHTML = item;
          caption.style = "  background-color: black; width: 10%;color: white;font-style: italic; text-align: center; overflow-wrap:break-word";
          figure.appendChild(image);
          figure.appendChild(caption);
          collectionDiv.appendChild(figure);
        });

     
      //add a break in between collections
      collectionDiv.appendChild(document.createElement('br'));
      //add the collection and its photos to the main div for photo display
      photoDisplayParent.appendChild(collectionDiv);

    }
   
  }
  else{
     // Handle errors
     const errorMessage = `${response.status} ${response.statusText} `;
     let userFeedback = jsonResponse.message;
     console.log(`An error occurred => ${errorMessage}`);
  }
}

getCollectionNames();
loadGallery();