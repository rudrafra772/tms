// Function to open the task details modal
function openTaskDetailsModal(taskId) {
  // Show the modal
  var modal = document.getElementById('taskDetailsModal' + taskId);
  modal.classList.remove('hidden');

  // Initialize TinyMCE for the specific textarea
  initializeTinyMCE(`#id_description_${taskId}`);
}

// Function to initialize TinyMCE
function initializeTinyMCE(selector) {
  tinymce.init({
    selector: selector,
    plugins: 'advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount hr emoticons codesample directionality imagetools textpattern toc nonbreaking template autosave', // No plugins needed for read-only
    toolbar: false, // No toolbar
    menubar: false, // No menu bar
    readonly: true, // Set the editor to read-only mode
    branding: false,
    statusbar: false, 
    height: 500,
    resize: false, // Disable resizing
});

}

// Function to close the task details modal
function closeTaskDetailsModal(taskId) {
  document.getElementById('taskDetailsModal' + taskId).classList.add('hidden');
}

// Function to open the add task modal
function openAddTaskModal(columnId) {
  document.getElementById('AddtasksModal' + columnId).classList.remove('hidden');
}

// Function to close the add task modal
function closeAddTaskModal(columnId) {
  document.getElementById('AddtasksModal' + columnId).classList.add('hidden');
}

// Close modals on background click or escape key press
window.addEventListener('click', function (event) {
  const modals = document.querySelectorAll('.modal');
  modals.forEach(modal => {
      if (event.target === modal) {
          modal.classList.add('hidden');
      }
  });
});

window.addEventListener('keydown', function (event) {
  if (event.key === 'Escape') {
      const modals = document.querySelectorAll('.modal');
      modals.forEach(modal => modal.classList.add('hidden'));
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const containers = document.querySelectorAll('.bg-gray-100');

  containers.forEach(container => {
    new Sortable(container, {
      group: 'kanban',
      animation: 150,
      ghostClass: 'bg-blue-100', // Class applied to the dragged item
      dragClass: 'dragging', // Class for the dragging state
      onEnd: function (evt) {
        const taskId = evt.item.dataset.taskid; // Get task ID
        const newColumnId = evt.to.closest('[data-columsid]').dataset.columsid; // Get new column ID

        // Update the specific dragged task's position
        const tasks = Array.from(evt.to.querySelectorAll('[data-taskid]'));

        tasks.forEach((task, index) => {
          if (task.dataset.taskid === taskId) {
            // Set form values
            document.getElementById('task-id').value = taskId;
            document.getElementById('new-column-id').value = newColumnId;
            document.getElementById('new-order').value = index;
          }
        });

        // Save the current scroll position
        const scrollPosition = window.scrollY;

        // Use AJAX to submit the form without refreshing the page
        const form = document.getElementById('update-task-form');
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();

        xhr.open('POST', form.action, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Indicate AJAX request

        xhr.onload = function () {
          if (xhr.status >= 200 && xhr.status < 300) {
            const response = JSON.parse(xhr.responseText);
            if (response.success) {
              console.log('Task updated successfully.');
            } else {
              console.log('Error: ' + (response.error || 'An error occurred.'));
            }
          } else {
            console.log('Failed to update task. Server returned status ' + xhr.status);
          }
          // Restore scroll position after the form is submitted
          window.scrollTo(0, scrollPosition);
        };

        xhr.onerror = function () {
          alert('An error occurred during the AJAX request.');
          // Restore scroll position after the form is submitted
          window.scrollTo(0, scrollPosition);
        };

        xhr.send(formData);
      },
    });
  });
});


// Function to match the height of all columns
function matchColumnHeights() {
  let maxHeight = 0;
  const columns = document.querySelectorAll('.column-content');
  
  // Reset heights to auto to recalculate the heights
  columns.forEach(column => column.style.height = 'auto');
  
  // Calculate the maximum height
  columns.forEach(column => {
      const height = column.offsetHeight;
      if (height > maxHeight) {
          maxHeight = height;
      }
  });
  
  // Set all columns to the maximum height
  columns.forEach(column => column.style.height = `${maxHeight}px`);
}

// Match column heights on page load
matchColumnHeights();

// Match column heights when a task is dragged and dropped
document.querySelectorAll('.draggable').forEach(draggable => {
  draggable.addEventListener('dragend', matchColumnHeights);
});

// Recalculate column heights on window resize
window.addEventListener('resize', matchColumnHeights);



