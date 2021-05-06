async function createNewCollection() {
  let newCollection = document.getElementById("new-coll-name").value;
  if (newCollection == ''){
    document.getElementById("collection-creation-message").value = "WARNING: No collection was created because no text was inputted";
    return
  }
 
  // the url
  const url = 'http://localhost:5000/api/collection';

  const argumentsForFetch = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8',
    },
    body: JSON.stringify({'name':newCollection})
  };


  const response = await fetch(url, argumentsForFetch);
  const jsonResponse = await response.json();
  let userFeedback = jsonResponse.message;

  if (response.status >= 200 && response.status <= 299) {
    
    const successMessage = `${response.status} ${response.statusText}`;
    document.getElementById("collection-creation-message").value = "Successfully created collection!";

        
  } else {
    // Handle errors
    const errorMessage = `${response.status} ${response.statusText} `;
    document.getElementById("collection-creation-message").value = "ERROR: "+userFeedback;
    
  }
}
async function uploadNewPhotos() {
  //setup request body parameters 
  let errorOccurred = false;
  let selectedCollection = document.getElementById("selected-collection").value;

  if (selectedCollection == ''){
    selectedCollection = 'Main Gallery'
  }
  let uploadFormFiles= document.getElementById("files-to-upload").files;
  
  //let the user know that no files were selected to be updated
  if (uploadFormFiles.length == 0){
   
    document.getElementById("action-success-message").value = "No files were uploaded";
    return
  }

  //upload each photo individually
  for (var i = 0; i <  uploadFormFiles.length; i++ ){
    var data = new FormData()
    data.append('file', uploadFormFiles[i])
    data.append('collection',selectedCollection)
    
    console.log(uploadFormFiles[i])
     // the url
     const url = 'http://localhost:5000/api/photo';
  
     const argumentsForFetch = {
       method: 'POST',
       body: data
     };
   
   
     const response = await fetch(url, argumentsForFetch);
     const jsonResponse = await response.json();
     let userFeedback = jsonResponse.message;
     let errorPhoto = "";
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
        errorPhoto = uploadFormFiles[0].name;
        document.getElementById("action-success-message").value = 'ERROR for \"'+errorPhoto+"\": "+userFeedback;
        break;
     }
  }
  if (!errorOccurred){
    document.getElementById("action-success-message").value = 'All '+ uploadFormFiles.length +' photos were uploaded successfully. Please reload the page to see the new collections';
  }
  
   
  }