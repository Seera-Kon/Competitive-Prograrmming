class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacency_list = defaultdict(list) 

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        label_count = [0] * n  # Initialize a list to count labels in each subtree.

        def depth_first_search(node, parent):
            subtree_labels = ''  # Use a more descriptive name for the variable.

            for child in adjacency_list[node]:
                if child != parent:
                    subtree_labels += depth_first_search(child, node)

            subtree_labels += labels[node]
            label_count[node] = subtree_labels.count(labels[node])

            return subtree_labels

        depth_first_search(0, -1)  # Start the DFS from the root node.
        return label_count
