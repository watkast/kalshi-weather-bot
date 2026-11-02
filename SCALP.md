# Range-Scalp Bot

*Updated Mon Nov 02 21:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45121 | 39286 | 5835 (67) | 1 | $-13066.79 | -4.6% |
| **+10¢** | 33679 | 26918 | 6761 (88) | 2 | $-11941.81 | -5.6% |
| **+15¢** | 28167 | 20892 | 7275 (115) | 3 | $-11000.91 | -6.2% |
| **+20¢** | 25014 | 17397 | 7617 (150) | 4 | $-9755.75 | -6.2% |
| **+10¢ (15¢ stop)** | 55060 | 54973 | 87 (51) | 1 | $-20841.30 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 21:02 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.17 |
| 11-02 21:02 | +20 | HYPE | UP | 0.64 | open |  |
| 11-02 21:02 | +15 | HYPE | UP | 0.64 | open |  |
| 11-02 21:02 | +10 | HYPE | UP | 0.64 | 0.79 | 1.17 |
| 11-02 21:02 | +5 | HYPE | UP | 0.64 | 0.79 | 1.17 |
| 11-02 21:01 | +10 stop | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 11-02 21:01 | +20 | ZEC | UP | 0.53 | 0.80 | 2.40 |
| 11-02 21:01 | +15 | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 11-02 21:01 | +10 | ZEC | UP | 0.53 | 0.68 | 1.16 |
| 11-02 21:01 | +5 | ZEC | UP | 0.53 | 0.59 | 0.25 |
| 11-02 21:01 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-02 21:01 | +5 | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-02 21:01 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-02 21:01 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-02 21:01 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-02 21:01 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-02 21:01 | +5 | DOGE | DOWN | 0.64 | open |  |
| 11-02 21:01 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-02 21:01 | +20 | NEAR | UP | 0.61 | 0.82 | 1.82 |
| 11-02 21:01 | +15 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-02 21:01 | +10 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-02 21:01 | +5 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-02 21:00 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-02 21:00 | +20 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 11-02 21:00 | +15 | ETH | UP | 0.62 | 0.81 | 1.62 |
| 11-02 21:00 | +10 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 11-02 21:00 | +5 | ETH | UP | 0.62 | 0.71 | 0.58 |
| 11-02 21:00 | +10 stop | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 21:00 | +20 | BNB | UP | 0.62 | open |  |
| 11-02 21:00 | +15 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-02 21:00 | +10 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 21:00 | +5 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 21:00 | +10 stop | SOL | UP | 0.67 | open |  |
| 11-02 21:00 | +20 | SOL | UP | 0.67 | open |  |
| 11-02 21:00 | +15 | SOL | UP | 0.67 | open |  |
| 11-02 21:00 | +10 | SOL | UP | 0.67 | open |  |
| 11-02 21:00 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 11-02 20:59 | +10 stop | ETH | UP | 0.16 | 0.58 | 3.92 |
| 11-02 20:59 | +20 | ETH | UP | 0.18 | 0.58 | 3.71 |
| 11-02 20:59 | +15 | ETH | UP | 0.18 | 0.58 | 3.71 |
