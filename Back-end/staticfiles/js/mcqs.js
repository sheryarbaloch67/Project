// Add an event listener to the "Add Next" button
document.getElementById("add-next-btn").addEventListener("click", function(event) {
    // Prevent the default behavior of the submit button
    event.preventDefault();
    
    // Get the form data
    var form = document.getElementById("question-form");
    var formData = new FormData(form);
    
    // Send the form data to the server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "#");
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Clear the form
        form.reset();
      } else {
        alert("There was an error adding the question.");
      }
    };
    xhr.send(formData);
  });
  
  // Function to get the value of a cookie
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  
  document.getElementById("clear-btn").addEventListener("click", function(event) {
    event.preventDefault();
    var form = document.getElementById("question-form");
    form.reset();
  });
  