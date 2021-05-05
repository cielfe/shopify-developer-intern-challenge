// async function getCollectionNames() {
//   const url = "http://localhost:5000/api/collection"
//   const argumentsForFetch = {
//     method: "GET"
//   }

//   const response = await fetch(url, argumentsForFetch);
//   const jsonResponse = await response.json();
 
//   if (response.status >= 200 && response.status <= 299) {
//     const successMessage = `${response.status} ${response.statusText}`;
//     let options = jsonResponse.collections;


//     //create the collection options
//     let collectionList = document.getElementById('collection-list');
  

//     options.forEach(function(item) {
//       var option = document.createElement('option');
//       option.value = item;
//       option.innerHTML = item;
//       collectionList.appendChild(option);
//     });
//   }
//   else{
//      // Handle errors
//      const errorMessage = `${response.status} ${response.statusText} `;
//      let userFeedback = jsonResponse.message;
//      console.log(`An error occurred => ${errorMessage}`);
//   }
// }
async function uploadNewPhotos() {
  let errorOccurred = false;
  let selectedCollection = document.getElementById("collection-list");
  console.log("selectedCollection "+ selectedCollection)
  let uploadFormFilesFiles = document.getElementById("files-to-upload").files;

  // let photos = document.getElementById("files-to-upload").files
  // console.log("photos[0].name "+ photos[0].name)
  // console.log("photos[1].name"+ photos[1].name)
  //   var requestBody = {
  //       "photos":photos
  //   }
  if (uploadFormFilesFiles.length == 0){
    console.log("element to change "+document.getElementById("action-success-message"))
    document.getElementById("action-success-message").value = "No files uploaded";
  }
  for (var i = 0; i <  uploadFormFilesFiles.length; i++ ){
    var data = new FormData()
    data.append('file', uploadFormFilesFiles[0])
    
    console.log(uploadFormFilesFiles[i])
     // the url
     const url = 'http://localhost:5000/api/photo';
  
     const argumentsForFetch = {
       method: 'POST',
       body: data
     };
   
   
     const response = await fetch(url, argumentsForFetch);
     const jsonResponse = await response.json();
     let userFeedback = jsonResponse.message;
     if (response.status >= 200 && response.status <= 299) {
       
       const successMessage = `${response.status} ${response.statusText}`;
       console.log(`The response: ${successMessage}`);
      


   
      
     } else {
       // Handle errors
       const errorMessage = `${response.status} ${response.statusText} `;
       errorOccurred = true;
       console.log(`An error occurred => ${errorMessage}`);
       
     }

     if (uploadFormFiles.length == 1){
      document.getElementById("action-success-message").value = userFeedback;
     }

     //break the loop if multiple files are being uploaded and an error occurs
     if (errorOccurred){
        document.getElementById("action-success-message").value = "ERROR: "+userFeedback;
        break;
     }
  }
  if (!errorOccurred){
    document.getElementById("action-success-message").value = 'All '+ uploadFormFiles.length +' photos were uploaded successfully';
  }
  
   
  }