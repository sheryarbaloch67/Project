const courseDiv = document.querySelector('#course-list');

courseDiv.addEventListener('click', (event) => {
  const courseLink = event.target.closest('.course');
  if (courseLink) {
    const courseId = courseLink.getAttribute('data-course-id');
    window.location.href = `/lectures/${courseId}`;
  }
});
