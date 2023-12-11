#!/usr/bin/env python3


""" AirBnB Console """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
    __count = 0

    def emptyline(self):
        """Pass if no command is given"""
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input"""
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__count = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            comd_argv = line.split()
            comd_argv[0], comd_argv[1] = comd_argv[1], comd_argv[0]
            line = " ".join(comd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        'exit the program'
        return True

    def do_EOF(self, arg):
        'exit the program on EOF command'
        print()
        return True

    def do_create(self, arg):
        "Create an instance should the Model be valid"
        if not arg:
            print("** class name missing **")
            return None
        try:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Print a dictionary of a instance in base of it's ID"
        comd_argv = arg.split()
        if not comd_argv:
            print("** class name missing **")
            return None
        try:
            eval(comd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_my_objs = storage.all()

        if len(comd_argv) < 2:
                print("** instance id missing **")
                return None

        comd_argv[1] = comd_argv[1].replace("\"", "")
        key = comd_argv[0] + '.' + comd_argv[1]

        if all_my_objs.get(key, False):
            print(all_my_objs[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        "Print all instances saved in file.json"
        comd_argv = arg.split()

        if comd_argv:
            try:
                eval(comd_argv[0])
            except:
                print("** class doesn't exist **")
                return None

        all_my_objs = storage.all()
        print_list = []
        len_objs = len(all_my_objs)
        for key, value in all_my_objs.items():
            if not comd_argv:
                if HBNBCommand.__count == 0:
                    print_list.append("\"" + str(value) + "\"")
                else:
                    print_list.append(str(value))
            else:
                check = key.split('.')
                if comd_argv[0] == check[0]:
                    if HBNBCommand.__count == 0:
                        print_list.append("\"" + str(value) + "\"")
                    else:
                        print_list.append(str(value))
        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

    def do_destroy(self, arg):
        "Deletes an instance based on it's ID, save the changes,
        Usage: destroy <class name> <id>"

        comd_argv = arg.split()
        if not comd_argv:
            print("** class name missing **")
            return None
        try:
            eval(comd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_my_objs = storage.all()

        if len(comd_argv) < 2:
                print("** instance id missing **")
                return None

        comd_argv[1] = comd_argv[1].replace("\"", "")
        key = comd_argv[0] + '.' + comd_argv[1]

        if all_my_objs.get(key, False):
            all_my_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        "Usage: update <class name> <id> <attribute name> <attribute value>"
        comd_argv = []
        part2_argv = []
        is_dict = 0
        if "\"" in arg:
            if "," in arg:
                if "{" in arg:
                    is_dict = 1
                    part1_argv = arg.split(",")[0].split()
                    for b in part1_argv:
                        comd_argv.append(b.replace("\"", ""))
                    part2_argv = arg.replace("}", "").split("{")[1].split(", ")
                    for c in part2_argv:
                        for n in c.split(": "):
                            comd_argv.append(n.replace("\"", "")
                                            .replace('\'', ""))
                else:
                    arg_key = arg.replace(",", "")
                    part1_argv = arg_key.split()
                    for d in part1_argv[:2]:
                        comd_argv.append(d.replace("\"", ""))
                    part2_argv = arg.split(", ")[1:]
                    for e in part2_argv:
                        comd_argv.append(e.replace("\"", ""))
            else:
                part1_argv = arg.split("\"")[0]
                for x in part1_argv.split():
                    comd_argv.append(x)
                part2_argv = arg.split("\"")[1:]
                for t in part2_argv:
                    if t != " " and t != "":
                        comd_argv.append(t.replace("\"", ""))

        else:
            part1_argv = arg.split()
            for a in range(len(part1_argv)):
                if a == 4:
                    break
                comd_argv.append(part1_argv[a])

        if (len(comd_argv) == 0):
            print("** class name missing **")
            return None

        try:
            eval(comd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        if len(comd_argv) < 2:
            print("** instance id missing **")
            return None

        all_my_objs = storage.all()

        key = comd_argv[0] + '.' + comd_argv[1]
        if all_my_objs.get(key, False):
            if (len(comd_argv) >= 3):
                if (len(comd_argv) % 2) == 0:
                    for a in range(2, len(comd_argv), 2):
                        attribute = comd_argv[a]
                        type_attri = getattr(all_my_objs[key], comd_argv[a], "")
                        try:
                            cast_val = type(type_attri)(comd_argv[a + 1])
                        except:
                            cast_val = type_attri
                        setattr(all_my_objs[key], comd_argv[a], cast_val)
                        all_my_objs[key].save()
                        if is_dict == 0:
                            break
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            print("** no instance found **")

    def do_count(self, arg):
        "Usage:to count <class name> or <class name>.count()"
        comd_argv = arg.split()

        if comd_argv:
            try:
                eval(comd_argv[0])
            except:
                print("** class doesn't exist **")
                return None

        all_my_objs = storage.all()
        count = 0

        for key, value in all_my_objs.items():
            if not comd_argv:
                count += 1
            else:
                check = key.split('.')
                if comd_argv[0] == check[0]:
                    count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
