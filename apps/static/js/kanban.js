 // Function to open the task details modal
 function openTaskDetailsModal(taskId) {
    // Perform an AJAX request to fetch task details

    document.getElementById('taskDetailsModal'+taskId).classList.remove('hidden');
    
  }

  // Function to close the task details modal
  function closeTaskDetailsModal(taskId) {
    document.getElementById('taskDetailsModal'+taskId).classList.add('hidden');
  }



function openAddTaskModal(columnId) {
    document.getElementById('AddtasksModal' + columnId).classList.remove('hidden');
}

function closeAddTaskModal(columnId) {
    document.getElementById('AddtasksModal' + columnId).classList.add('hidden');
}




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

        // Ensure all tasks in the new column are ordered correctly
        const tasks = Array.from(evt.to.querySelectorAll('[data-taskid]'));

        // Update order for each task in the new column
        tasks.forEach((task, index) => {
          if (task.dataset.taskid === taskId) {
            document.getElementById('task-id').value = taskId;
            document.getElementById('new-column-id').value = newColumnId;
            document.getElementById('new-order').value = index;
          }
        });

        // Submit the form
        document.getElementById('update-task-form').submit();
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

  // Initialize SortableJS on columns
  const containers = document.querySelectorAll('.column-content');
  containers.forEach(container => {
    new Sortable(container, {
      group: 'kanban',
      animation: 150,
      ghostClass: 'bg-blue-100',
      dragClass: 'dragging',
      onEnd: function (evt) {
        console.log('Dragged:', evt.item);
      },
    });
  });