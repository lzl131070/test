class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        temp = result

        while (True):
            if (l1 != None):
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if (l2 != None):
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            re = v1 + v2 + temp.val
            temp.val = re % 10

            if (l1 == None and l2 == None):
                if (re // 10 != 0):
                    temp.next = ListNode(re // 10)
                break
            temp.next = ListNode(re // 10)
            nextt = temp.next
            temp = nextt

        return result

