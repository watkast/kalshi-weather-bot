# Range-Scalp Bot

*Updated Tue Oct 27 10:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36403 | 31787 | 4616 (43) | 6 | $-10072.23 | -4.4% |
| **+10¢** | 27200 | 21861 | 5339 (65) | 6 | $-8895.09 | -5.2% |
| **+15¢** | 22756 | 17024 | 5732 (89) | 6 | $-7847.72 | -5.5% |
| **+20¢** | 20165 | 14160 | 6005 (113) | 6 | $-6876.07 | -5.4% |
| **+10¢ (15¢ stop)** | 44635 | 44572 | 63 (33) | 0 | $-17048.62 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 10:05 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-27 10:05 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-27 10:05 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-27 10:03 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 10:03 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.94 |
| 10-27 10:03 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-27 10:03 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 10:03 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 10-27 10:02 | +10 stop | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-27 10:02 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-27 10:02 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-27 10:02 | +10 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-27 10:02 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 10-27 10:02 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-27 10:02 | +20 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-27 10:02 | +15 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-27 10:02 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-27 10:02 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-27 10:02 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.86 |
| 10-27 10:02 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-27 10:02 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 10:01 | +10 stop | ZEC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-27 10:01 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-27 10:00 | +10 stop | DOGE | UP | 0.62 | 0.47 | -1.85 |
| 10-27 10:00 | +20 | DOGE | UP | 0.62 | open |  |
| 10-27 10:00 | +15 | DOGE | UP | 0.62 | open |  |
| 10-27 10:00 | +10 | DOGE | UP | 0.62 | open |  |
| 10-27 10:00 | +5 | DOGE | UP | 0.62 | open |  |
| 10-27 10:00 | +10 stop | ZEC | UP | 0.66 | 0.42 | -2.74 |
| 10-27 10:00 | +20 | ZEC | UP | 0.66 | open |  |
| 10-27 10:00 | +15 | ZEC | UP | 0.66 | open |  |
| 10-27 10:00 | +10 | ZEC | UP | 0.66 | open |  |
| 10-27 10:00 | +5 | ZEC | UP | 0.67 | open |  |
| 10-27 10:00 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 10-27 10:00 | +20 | NEAR | UP | 0.66 | open |  |
| 10-27 10:00 | +15 | NEAR | UP | 0.66 | open |  |
| 10-27 10:00 | +10 | NEAR | UP | 0.66 | open |  |
| 10-27 10:00 | +5 | NEAR | UP | 0.66 | open |  |
| 10-27 10:00 | +10 stop | HYPE | UP | 0.56 | 0.36 | -2.35 |
| 10-27 10:00 | +20 | HYPE | UP | 0.56 | open |  |
