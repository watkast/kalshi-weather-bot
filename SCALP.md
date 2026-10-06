# Range-Scalp Bot

*Updated Tue Oct 06 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4867 | 4210 | 657 (7) | 1 | $-1538.97 | -5.0% |
| **+10¢** | 3740 | 2974 | 766 (11) | 1 | $-1423.99 | -6.0% |
| **+15¢** | 3142 | 2330 | 812 (14) | 1 | $-1234.05 | -6.3% |
| **+20¢** | 2814 | 1967 | 847 (19) | 1 | $-1017.83 | -5.8% |
| **+10¢ (15¢ stop)** | 5956 | 5943 | 13 (8) | 0 | $-2123.47 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 09:35 | +10 stop | HYPE | DOWN | 0.57 | 0.36 | -2.49 |
| 10-06 09:35 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-06 09:35 | +10 | HYPE | DOWN | 0.64 | open |  |
| 10-06 09:35 | +10 stop | SOL | UP | 0.57 | 0.70 | 0.97 |
| 10-06 09:35 | +15 | SOL | UP | 0.57 | 0.73 | 1.28 |
| 10-06 09:35 | +10 | SOL | UP | 0.57 | 0.70 | 0.97 |
| 10-06 09:35 | +5 | SOL | UP | 0.57 | 0.70 | 0.97 |
| 10-06 09:34 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.36 |
| 10-06 09:31 | +10 stop | HYPE | DOWN | 0.52 | 0.65 | 0.92 |
| 10-06 09:31 | +20 | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +15 | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +10 | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 10-06 09:31 | +5 | HYPE | DOWN | 0.52 | 0.58 | 0.24 |
| 10-06 09:31 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-06 09:31 | +20 | NEAR | UP | 0.69 | 0.94 | 2.28 |
| 10-06 09:31 | +15 | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 10-06 09:31 | +10 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-06 09:31 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 10-06 09:31 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 09:31 | +20 | SOL | UP | 0.67 | 0.87 | 1.76 |
| 10-06 09:31 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-06 09:31 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 09:31 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-06 09:30 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-06 09:30 | +20 | BTC | UP | 0.70 | 0.90 | 1.78 |
| 10-06 09:30 | +15 | BTC | UP | 0.70 | 0.88 | 1.57 |
| 10-06 09:30 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-06 09:30 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-06 09:27 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-06 09:27 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-06 09:26 | +10 stop | XRP | DOWN | 0.62 | 0.30 | -3.52 |
| 10-06 09:26 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +15 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +10 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +5 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +10 stop | DOGE | DOWN | 0.62 | 0.41 | -2.44 |
| 10-06 09:26 | +20 | DOGE | DOWN | 0.62 | 0.99 | 3.53 |
| 10-06 09:26 | +15 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-06 09:26 | +10 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-06 09:26 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
