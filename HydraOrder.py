from Order import *


class HydraOrder(Order):

    def __init__(self):
        super(HydraOrder, self).__init__()
        self.statusChangeNotifier = HydraOrder.StatusChangeNotifier(self)

    def set_nite_vwap(self, start_time, end_time, stop_price):
        self.algo_fields = "4,{0},{1},,,{2},N,N,100,,,N,N,0".format(start_time, end_time, stop_price)

    def craft_message(self):
        return "#:00000:N:000:{0}:{1}:{2}:N:{3}:{4}:{5}:{6}:{7}:{8}:{9}::{10}::{11}:{18}:{13}:{12}:{14}:{15}:{16}:{17}::::*".format(
            self.account, self.parent_id, self.order_id, self.symbol, self.side,
            self.quantity, self.order_price, self.contra, self.channel_of_execution,
            self.tif, self.type, self.display, self.cancel_replace_id,
            self.reserve_size, self.ticket_id, self.algo_fields, self.security_type,
            self.security_id, self.stop_limit_price)

    def craft_cancel_message(self):
        return "#:00000:N:000:{0}::{2}:C:{3}:{4}:{5}:{6}::{8}:{9}::{10}::{11}:*".format(
            self.account, self.parent_id, self.order_id, self.symbol, self.side,
            self.quantity, self.order_price, self.contra, self.channel_of_execution,
            self.tif, self.type, self.display)

    def change_status(self, stat, token_list = []):
        self.status = stat
        self.statusChangeNotifier.notifyObservers((self, token_list))

    def update_order(self, tokens):
        if tokens[2] != 'S':
            raise Exception('invalid message type {0} sent to order.update_order'.format(tokens[2]))
        if tokens[4] == 'S':
            # ignore if status is pending
            if tokens[14] == msg_status_type.pending:
                self.change_status(order_status_type.acknowledged)

            elif tokens[14] == msg_status_type.executed:
                # can be partial or full
                self.executed_quantity += int(tokens[10])
                t = (int(tokens[10]), float(tokens[11]))
                self.execution_list.append(t)
                self.leaves_qty = int(tokens[20])
                if self.leaves_qty == 0:
                    self.change_status(order_status_type.executed, tokens)
                else:
                    self.change_status(order_status_type.partial_open, tokens)
            elif tokens[14] == msg_status_type.open:
                # can be unfilled order or partial
                self.leaves_qty = int(tokens[20])
                if self.leaves_qty != self.quantity:
                    self.change_status(order_status_type.partial_open)
                else:
                    self.change_status(order_status_type.open)
            elif tokens[14] == msg_status_type.rejected:
                # you want to note the error
                self.change_status(order_status_type.rejected)
                self.error = tokens[15]
            elif tokens[14] == msg_status_type.canceled:
                # this can be a partial order canceled so there's filled portion and canceled
                if self.leaves_qty == self.quantity:
                    self.change_status(order_status_type.canceled)
                else:
                    self.change_status(order_status_type.partial_canceled)
        elif tokens[4] == 'F':
            # this is an acknowledgment order, so can be ignored
            pass
        else:
            raise Exception('message type S {0} not implemented'.format(tokens[4]))

    class StatusChangeNotifier(Observable):

        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notifyObservers(self, arg=None):
            self.setChanged()
            Observable.notifyObservers(self, arg)
