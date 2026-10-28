# Range-Scalp Bot

*Updated Wed Oct 28 20:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38461 | 33563 | 4898 (48) | 1 | $-10797.71 | -4.5% |
| **+10¢** | 28683 | 23026 | 5657 (70) | 1 | $-9578.49 | -5.3% |
| **+15¢** | 23996 | 17922 | 6074 (95) | 1 | $-8510.67 | -5.6% |
| **+20¢** | 21286 | 14926 | 6360 (120) | 1 | $-7443.30 | -5.6% |
| **+10¢ (15¢ stop)** | 47050 | 46983 | 67 (35) | 1 | $-17878.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 20:05 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-28 20:05 | +20 | BTC | UP | 0.59 | open |  |
| 10-28 20:05 | +15 | BTC | UP | 0.59 | open |  |
| 10-28 20:05 | +10 | BTC | UP | 0.59 | open |  |
| 10-28 20:05 | +5 | BTC | UP | 0.60 | open |  |
| 10-28 19:54 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-28 19:53 | +10 stop | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 10-28 19:53 | +20 | DOGE | UP | 0.68 | 0.93 | 2.32 |
| 10-28 19:53 | +15 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 10-28 19:53 | +10 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 10-28 19:53 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-28 19:52 | +10 stop | ZEC | UP | 0.54 | 0.73 | 1.58 |
| 10-28 19:52 | +10 stop | NEAR | UP | 0.53 | 0.69 | 1.27 |
| 10-28 19:51 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-28 19:51 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-28 19:51 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 10-28 19:51 | +10 stop | NEAR | UP | 0.48 | 0.60 | 0.85 |
| 10-28 19:50 | +5 | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 10-28 19:50 | +10 stop | NEAR | DOWN | 0.58 | 0.40 | -2.15 |
| 10-28 19:50 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-28 19:50 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-28 19:50 | +10 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-28 19:50 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-28 19:50 | +5 | ZEC | DOWN | 0.61 | yes | -6.27 |
| 10-28 19:50 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-28 19:50 | +10 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-28 19:50 | +5 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-28 19:50 | +10 stop | XRP | UP | 0.61 | 0.80 | 1.61 |
| 10-28 19:50 | +20 | XRP | UP | 0.61 | 0.81 | 1.72 |
| 10-28 19:50 | +15 | XRP | UP | 0.61 | 0.80 | 1.64 |
| 10-28 19:50 | +10 | XRP | UP | 0.61 | 0.80 | 1.61 |
| 10-28 19:50 | +5 | XRP | UP | 0.62 | 0.80 | 1.51 |
| 10-28 19:50 | +5 | BNB | UP | 0.57 | 0.62 | 0.15 |
| 10-28 19:50 | +10 stop | SOL | UP | 0.52 | 0.70 | 1.47 |
| 10-28 19:50 | +15 | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 10-28 19:50 | +5 | HYPE | UP | 0.58 | 0.64 | 0.21 |
| 10-28 19:49 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 10-28 19:49 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-28 19:49 | +20 | ETH | UP | 0.60 | 0.85 | 2.24 |
| 10-28 19:49 | +15 | ETH | UP | 0.60 | 0.76 | 1.30 |
