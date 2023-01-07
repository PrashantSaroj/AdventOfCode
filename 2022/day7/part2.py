class Node:
    def __init__(self, parent, is_file, size, name):
        self.size = size
        self.name = name
        self.parent = parent
        self.is_file = is_file

        self.children = []

    def calculate_size(self):
        """
        all children must have their size already calculated.
        """
        for child in self.children:
            self.size += child.size

    def has_child(self, file_name):
        for child in self.children:
            if child.name == file_name:
                return child
        return None


class FileSystem:
    def __init__(self):
        self.root = Node(None, False, 0, 'root')
        self.curr = self.root

    def process_command(self, cmd):
        if cmd[0].startswith('cd'):
            self.process_cd(cmd)
        elif cmd[0].startswith('ls'):
            self.process_ls(cmd)
        else:
            print("Unknown cmd: {}", cmd)

    def process_cd(self, cmd):
        target_dir = cmd[0].split()[1]
        if target_dir == '..':
            self.curr = self.curr.parent
        else:
            target_node = self.curr.has_child(target_dir)
            if target_node is not None:
                self.curr = target_node
            else:
                fresh_node = Node(self.curr, False, 0, target_dir)
                self.curr.children.append(fresh_node)
                self.curr = fresh_node

    def process_ls(self, cmd):
        for output in cmd[1:]:
            if output.startswith('dir'):
                self.process_ls_dir(output)
            else:
                self.process_ls_file(output)

    def process_ls_dir(self, cmd):
        target_dir = cmd.split()[1]
        target_node = self.curr.has_child(target_dir)
        # create child if required
        if target_node is None:
            fresh_node = Node(self.curr, False, 0, target_dir)
            self.curr.children.append(fresh_node)

    def process_ls_file(self, cmd):
        size, name = cmd.split()
        fresh_node = Node(self.curr, True, int(size), name)
        self.curr.children.append(fresh_node)


def update_dir_sizes(node):
    global TARGET_NODE, CURR_DIFF
    if node.is_file:
        return

    for child in node.children:
        update_dir_sizes(child)

    curr_size = 0
    for child in node.children:
        curr_size += child.size
    node.size = curr_size

    if node.size >= TARGET_SZ and node.size - TARGET_SZ < CURR_DIFF:
        TARGET_NODE = node
        CURR_DIFF = node.size - TARGET_SZ


def parse_command(cmd):
    """
    rstrip new line and convert to a list of strings.
    """
    return cmd.rstrip().split('\n')


TARGET_SZ = 2080344
TARGET_NODE = None
CURR_DIFF = 70000000


def main():
    commands = map(parse_command, open('in.txt', 'r').read().split('$ '))
    fs = FileSystem()
    for cmd in commands:
        fs.process_command(cmd)

    update_dir_sizes(fs.root.children[0])
    print(TARGET_NODE.size)


main()
