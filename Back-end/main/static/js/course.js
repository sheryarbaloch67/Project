const addCourseButton = document.querySelector('.addCourse-button');
const courseDiv = document.querySelector('.course-div');

addCourseButton.addEventListener('click', () => {
  const form = document.querySelector('.new-course-form');
  const formData = new FormData(form);

  fetch('/add course', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const courseSubDiv = document.createElement('div');
    courseSubDiv.classList.add('course-subdiv');
    courseSubDiv.innerHTML = `
      <div class="course-subdiv-details">
        <h3 class="course-title">${data.course_name}</h3>
        <p class="course-details">Code: ${data.course_code} | Credit Hours: ${data.credit_hours} | Discipline: ${data.discipline} | Semester: ${data.semester}</p>
        <a href="${data.lectures}" class="course-link">View Lectures</a>
      </div>
    `;
    courseDiv.appendChild(courseSubDiv);
    
    // Redirect user to dashboard after successfully adding the course
    window.location.href = "/dashboard";
  })
  .catch(error => console.error(error));
});

courseDiv.addEventListener('click', (event) => {
  const courseLink = event.target.closest('.course-subdiv .course-link');
  if (courseLink) {
    const courseUrl = courseLink.href;
    window.location.href = courseUrl;
  }
});
