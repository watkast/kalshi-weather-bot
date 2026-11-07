# Range-Scalp Bot

*Updated Sat Nov 07 11:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50904 | 44377 | 6527 (76) | 3 | $-14263.78 | -4.5% |
| **+10¢** | 38002 | 30394 | 7608 (102) | 2 | $-13238.34 | -5.5% |
| **+15¢** | 31812 | 23615 | 8197 (131) | 4 | $-12154.31 | -6.1% |
| **+20¢** | 28285 | 19694 | 8591 (173) | 6 | $-10734.26 | -6.1% |
| **+10¢ (15¢ stop)** | 61997 | 61898 | 99 (58) | 1 | $-22907.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 11:04 | +5 | ZEC | DOWN | 0.67 | open |  |
| 11-07 11:03 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 11-07 11:03 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-07 11:03 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-07 11:03 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-07 11:03 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-07 11:03 | +5 | DOGE | UP | 0.64 | open |  |
| 11-07 11:03 | +10 stop | BTC | UP | 0.67 | 0.49 | -2.14 |
| 11-07 11:03 | +20 | BTC | UP | 0.67 | open |  |
| 11-07 11:03 | +15 | BTC | UP | 0.67 | open |  |
| 11-07 11:03 | +10 | BTC | UP | 0.67 | open |  |
| 11-07 11:03 | +5 | BTC | UP | 0.67 | open |  |
| 11-07 11:02 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-07 11:02 | +15 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 11-07 11:02 | +10 | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-07 11:02 | +5 | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-07 11:02 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.75 |
| 11-07 11:02 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-07 11:02 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-07 11:02 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.75 |
| 11-07 11:02 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.75 |
| 11-07 11:02 | +10 stop | DOGE | UP | 0.52 | 0.66 | 1.06 |
| 11-07 11:02 | +20 | DOGE | UP | 0.52 | open |  |
| 11-07 11:02 | +15 | DOGE | UP | 0.52 | open |  |
| 11-07 11:02 | +10 | DOGE | UP | 0.52 | 0.66 | 1.06 |
| 11-07 11:02 | +5 | DOGE | UP | 0.52 | 0.57 | 0.14 |
| 11-07 11:02 | +10 stop | ETH | UP | 0.66 | 0.81 | 1.23 |
| 11-07 11:02 | +10 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 11-07 11:02 | +5 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-07 11:02 | +10 stop | XRP | UP | 0.52 | 0.68 | 1.26 |
| 11-07 11:02 | +20 | XRP | UP | 0.52 | open |  |
| 11-07 11:02 | +15 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 11-07 11:02 | +10 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 11-07 11:02 | +5 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 11-07 11:01 | +10 stop | BNB | UP | 0.68 | 0.82 | 1.16 |
| 11-07 11:01 | +20 | BNB | UP | 0.68 | open |  |
| 11-07 11:01 | +15 | BNB | UP | 0.68 | 0.83 | 1.27 |
| 11-07 11:01 | +10 | BNB | UP | 0.68 | 0.82 | 1.16 |
| 11-07 11:01 | +5 | BNB | UP | 0.68 | 0.77 | 0.64 |
| 11-07 11:01 | +10 stop | ETH | UP | 0.57 | 0.67 | 0.66 |
