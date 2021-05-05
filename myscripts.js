async function uploadNewPhotos() {
  let photos = document.getElementById("files-to-upload").files
    var requestBody = {
        "photos":photos
    }
  
    // the url
    const url = 'http://localhost:5000/api/photo';
  
    const argumentsForFetch = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
      body: JSON.stringify(requestBody),
    };
  
    console.log(
      `calling url: ${url} with arguments ${JSON.stringify(
        argumentsForFetch,
        null,
        2
      )}`
    );
    const response = await fetch(url, argumentsForFetch);
  
    if (response.status >= 200 && response.status <= 299) {
      // in this case, we get a `201 Created`, so there is
      // no JSON data returned. (See server.js for details)
  
      // so....no need to do this:
      ///////const jsonResponse = await response.json();
      ///////const responseAsString = JSON.stringify(jsonResponse,null,2);
  
      // when you stop the debugger in browser, you can see that
      // response object above has: status and statusText fields
  
      const successMessage = `${response.status} ${response.statusText}`;
      console.log(`The response: ${successMessage}`);
  
     
    } else {
      // Handle errors
      const errorMessage = `${response.status} ${response.statusText}`;
      console.log(`An error occurred => ${errorMessage}`);
     
    }
  }