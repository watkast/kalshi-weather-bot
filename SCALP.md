# Range-Scalp Bot

*Updated Tue Oct 06 22:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5591 | 4848 | 743 (9) | 5 | $-1692.95 | -4.8% |
| **+10¢** | 4269 | 3394 | 875 (15) | 7 | $-1611.25 | -6.0% |
| **+15¢** | 3578 | 2651 | 927 (19) | 7 | $-1397.93 | -6.2% |
| **+20¢** | 3198 | 2235 | 963 (26) | 7 | $-1113.23 | -5.5% |
| **+10¢ (15¢ stop)** | 6816 | 6801 | 15 (9) | 3 | $-2443.89 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 22:54 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 10-06 22:53 | +10 stop | BTC | UP | 0.48 | open |  |
| 10-06 22:53 | +10 | BTC | UP | 0.48 | open |  |
| 10-06 22:53 | +5 | BTC | UP | 0.48 | 0.57 | 0.54 |
| 10-06 22:53 | +10 stop | BNB | DOWN | 0.54 | 0.72 | 1.47 |
| 10-06 22:53 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-06 22:53 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-06 22:52 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-06 22:51 | +5 | XRP | UP | 0.50 | 0.64 | 1.05 |
| 10-06 22:51 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-06 22:51 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-06 22:51 | +5 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-06 22:49 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-06 22:49 | +10 stop | DOGE | UP | 0.51 | 0.33 | -2.18 |
| 10-06 22:49 | +20 | DOGE | UP | 0.52 | open |  |
| 10-06 22:49 | +15 | DOGE | UP | 0.52 | open |  |
| 10-06 22:49 | +10 | DOGE | UP | 0.52 | open |  |
| 10-06 22:49 | +5 | DOGE | UP | 0.52 | open |  |
| 10-06 22:48 | +5 | BNB | UP | 0.66 | open |  |
| 10-06 22:48 | +10 stop | ETH | UP | 0.66 | 0.45 | -2.44 |
| 10-06 22:48 | +20 | ETH | UP | 0.66 | open |  |
| 10-06 22:48 | +15 | ETH | UP | 0.66 | open |  |
| 10-06 22:48 | +10 | ETH | UP | 0.66 | open |  |
| 10-06 22:48 | +5 | ETH | UP | 0.66 | open |  |
| 10-06 22:48 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-06 22:48 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-06 22:48 | +20 | SOL | DOWN | 0.57 | 0.85 | 2.49 |
| 10-06 22:48 | +15 | SOL | DOWN | 0.57 | 0.74 | 1.34 |
| 10-06 22:48 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.83 |
| 10-06 22:48 | +5 | SOL | DOWN | 0.57 | 0.65 | 0.42 |
| 10-06 22:46 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-06 22:46 | +20 | BTC | UP | 0.70 | open |  |
| 10-06 22:46 | +15 | BTC | UP | 0.70 | open |  |
| 10-06 22:46 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-06 22:46 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-06 22:46 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
| 10-06 22:46 | +20 | BNB | UP | 0.58 | open |  |
| 10-06 22:46 | +15 | BNB | UP | 0.58 | open |  |
| 10-06 22:46 | +10 | BNB | UP | 0.58 | open |  |
| 10-06 22:46 | +5 | BNB | UP | 0.58 | 0.65 | 0.36 |
