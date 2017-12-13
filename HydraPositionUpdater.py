from Position import Position

class HydraPositionUpdater(object):

    @staticmethod
    def UpdatePosition(position, message_tokens):
        # interprets hydra execution message
        try:
            quantity = int(message_tokens[10])
            if message_tokens[17] != 'B': quantity *= -1
            execution_price = float(message_tokens[11])
            position.add_fill(quantity, execution_price)
        except:
            pass

# p = Position('MU',1156,43.8)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:090:S:N:20171107 094500:ALGOGROUP:1209604:1:100:43.835::NITE:E::MU:S:M:-1:1056:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:087:S:N:20171107 095026:ALGOGROUP:1209604:2:94:44.07::NITE:E::MU:S:M:-1:962:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:086:S:N:20171107 095026:ALGOGROUP:1209604:3:6:44.07::NITE:E::MU:S:M:-1:956:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:089:S:N:20171107 100030:ALGOGROUP:1209604:4:100:44.215::NITE:E::MU:S:M:-1:856:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:087:S:N:20171107 101130:ALGOGROUP:1209604:5:55:43.78::NITE:E::MU:S:M:-1:801:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:087:S:N:20171107 101130:ALGOGROUP:1209604:6:45:43.78::NITE:E::MU:S:M:-1:756:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:088:S:N:20171107 102456:ALGOGROUP:1209604:7:100:43.74::NITE:E::MU:S:M:-1:656:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:088:S:N:20171107 103736:ALGOGROUP:1209604:8:100:43.77::NITE:E::MU:S:M:-1:556:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:088:S:N:20171107 105313:ALGOGROUP:1209604:9:100:43.72::NITE:E::MU:S:M:-1:456:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:089:S:N:20171107 111004:ALGOGROUP:1209604:10:100:44.05::NITE:E::MU:S:M:-1:356:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:089:S:N:20171107 112931:ALGOGROUP:1209604:11:100:43.86::NITE:E::MU:S:M:-1:256:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:089:S:N:20171107 115315:ALGOGROUP:1209604:12:100:43.82::NITE:E::MU:S:M:-1:156:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:088:S:N:20171107 125952:ALGOGROUP:1209604:13:13:43.51::NITE:E::MU:S:M:-1:143:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:087:S:N:20171107 125952:ALGOGROUP:1209604:14:11:43.5::NITE:E::MU:S:M:-1:132:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:087:S:N:20171107 125952:ALGOGROUP:1209604:15:100:43.5::NITE:E::MU:S:M:-1:32:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
# msg = '#:05343:S:085:S:N:20171107 125952:ALGOGROUP:1209604:16:32:43.5::NITE:E::MU:S:M:-1:0:'
# HydraPositionUpdater.UpdatePosition(p,msg)
# print p.qty, p.dollar_value(), p.open_pnl(43.8)
