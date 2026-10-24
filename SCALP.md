# Range-Scalp Bot

*Updated Sat Oct 24 12:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32000 | 27894 | 4106 (40) | 1 | $-9187.66 | -4.6% |
| **+10¢** | 23941 | 19195 | 4746 (58) | 1 | $-8192.82 | -5.4% |
| **+15¢** | 20041 | 14938 | 5103 (81) | 1 | $-7330.02 | -5.8% |
| **+20¢** | 17751 | 12409 | 5342 (103) | 2 | $-6516.61 | -5.8% |
| **+10¢ (15¢ stop)** | 39304 | 39245 | 59 (32) | 0 | $-15021.15 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 12:16 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-24 12:16 | +20 | ETH | UP | 0.67 | open |  |
| 10-24 12:16 | +15 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 10-24 12:16 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-24 12:16 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 10-24 12:15 | +10 stop | XRP | DOWN | 0.63 | 0.28 | -3.82 |
| 10-24 12:15 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-24 12:15 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-24 12:15 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-24 12:15 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-24 12:11 | +10 stop | BTC | DOWN | 0.54 | 0.28 | -2.93 |
| 10-24 12:07 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-24 12:06 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 12:04 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +20 | XRP | DOWN | 0.71 | 0.93 | 1.96 |
| 10-24 12:04 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-24 12:04 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +10 stop | BTC | UP | 0.58 | 0.40 | -2.15 |
| 10-24 12:04 | +10 | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-24 12:04 | +5 | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-24 12:04 | +10 stop | ETH | UP | 0.54 | 0.38 | -1.95 |
| 10-24 12:04 | +20 | ETH | UP | 0.54 | no | -5.58 |
| 10-24 12:04 | +15 | ETH | UP | 0.53 | 0.70 | 1.37 |
| 10-24 12:04 | +10 | ETH | UP | 0.53 | 0.70 | 1.37 |
| 10-24 12:04 | +5 | ETH | UP | 0.53 | 0.70 | 1.37 |
| 10-24 12:04 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:04 | +20 | SOL | DOWN | 0.69 | 0.91 | 1.97 |
| 10-24 12:04 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 10-24 12:04 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:04 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:02 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-24 12:01 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-24 12:01 | +20 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-24 12:01 | +15 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-24 12:01 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-24 12:01 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
