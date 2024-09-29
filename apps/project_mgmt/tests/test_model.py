from django.test import TestCase
from apps.project_mgmt.models import Board, Column, Task
from apps.auth.models import UserModel  # Import your custom user model
from apps.project_mgmt.choices import ColorChoices
from apps.project_mgmt.models import Project

class ProjectMgmtModelTest(TestCase):

    def setUp(self):
        # Set up the user, project, board, column, and task for testing
        self.user = UserModel.objects.create_user(username='testuser', email="testuaer@gmai.com", password='testpassword')
        self.project = Project.objects.create(name='Test Project')
        self.board = Board.objects.create(project=self.project, name='Test Board', description='A test board')
        self.column = Column.objects.create(board=self.board, name='Test Column', order=1, color=ColorChoices.blue)
        self.task = Task.objects.create(column=self.column, title='Test Task', description='Task description', order=1, user=self.user)

    def test_board_str(self):
        self.assertEqual(str(self.board), 'Test Board')

    def test_column_str(self):
        self.assertEqual(str(self.column), 'Test Column')

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')

