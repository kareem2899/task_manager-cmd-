from argparse  import ArgumentParser
from .task_controller import task_controller

def main():
    controller=task_controller('tasks.txt')

    parser=ArgumentParser(description='Task manager')
    subparser=parser.add_subparsers()
    add_task=subparser.add_parser('add',help='add the given task')
    add_task.add_argument('title',help='title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description about the task',type=str,default=None)
    add_task.add_argument('-s','--start_date',help='the starting date of the task',type=str,default=None)
    add_task.add_argument('-e','--end_date',help='the ending of the task',type=str,default=None)
    add_task.add_argument('--done',help='the task is done or not',type=bool,default=False)
    add_task.set_defaults(func=controller.add_task)

    list_tasks=subparser.add_parser('list',help='list unfinished tasks')
    list_tasks.add_argument('-a','--all',help='list all the tasks',action='store_true')#store_false ,store_const
    list_tasks.set_defaults(func=controller.display)

    check_tasks=subparser.add_parser('check',help='check the given task')
    check_tasks.add_argument('-t','--task',help='check teh task by its number',type=int)
    check_tasks.set_defaults(func=controller.check_task)

    remove_task=subparser.add_parser('remove',help='remove the given task')
    remove_task.add_argument('-t','--task',help='remove the task given its number',type=int)
    remove_task.set_defaults(func=controller.remove)

    reset=subparser.add_parser('reset',help='remove all tasks')
    reset.set_defaults(func=controller.reset)
    args=parser.parse_args()#make it a command line project
    args.func(args)

if __name__=='__main__':#to avoid excution of codes whilch included in the file when it calling by another file
    main()