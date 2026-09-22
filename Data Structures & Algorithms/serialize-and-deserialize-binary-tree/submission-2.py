class Codec:
    # share the delimiter between serializer/deserializer
    delimiter = ","

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def pre_order(node):
            if not node:
                # IMPORTANT: yield a Null marker before returning!
                yield "None"
                return
            yield str(node.val)
            yield from pre_order(node.left)
            yield from pre_order(node.right)

        res = self.delimiter.join(list(pre_order(root)))
        return res


    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        # split into a sequence, so we don't need to check the boundary 
        # when we are done with the sequence
        values = iter(data.split(self.delimiter))

        def construct():
            # grab the next value in "sequence", no need to check for boundary
            # if there is no value to pull from `next(values)`, 
            # we don't call `construct` again. We are done.
            val = next(values)
            if val == "None":
                return None

            node = TreeNode(int(val))
            node.left = construct()
            node.right = construct()

            return node

        res = construct()
        return res