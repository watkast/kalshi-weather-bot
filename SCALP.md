# Range-Scalp Bot

*Updated Sun Nov 22 07:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68397 | 59681 | 8716 (138) | 1 | $-18432.44 | -4.3% |
| **+10¢** | 51081 | 40898 | 10183 (181) | 1 | $-17119.31 | -5.3% |
| **+15¢** | 42813 | 31836 | 10977 (231) | 2 | $-15382.42 | -5.7% |
| **+20¢** | 38113 | 26577 | 11536 (289) | 2 | $-13717.48 | -5.7% |
| **+10¢ (15¢ stop)** | 83301 | 83122 | 179 (111) | 1 | $-30615.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 07:02 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-22 07:02 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-22 07:02 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-22 07:02 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-22 07:02 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-22 07:00 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 07:00 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-22 07:00 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-22 07:00 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 07:00 | +5 | BTC | DOWN | 0.71 | 0.80 | 0.63 |
| 11-22 06:57 | +10 stop | BTC | UP | 0.53 | 0.27 | -2.92 |
| 11-22 06:57 | +5 | BTC | UP | 0.54 | 0.61 | 0.35 |
| 11-22 06:57 | +10 stop | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 11-22 06:57 | +20 | DOGE | DOWN | 0.49 | 0.95 | 4.34 |
| 11-22 06:57 | +15 | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 11-22 06:57 | +10 | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 11-22 06:57 | +5 | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 11-22 06:57 | +5 | BTC | DOWN | 0.58 | 0.67 | 0.56 |
| 11-22 06:55 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 06:55 | +10 stop | BTC | DOWN | 0.66 | 0.36 | -3.33 |
| 11-22 06:55 | +20 | BTC | DOWN | 0.66 | 0.94 | 2.58 |
| 11-22 06:55 | +15 | BTC | DOWN | 0.66 | 0.94 | 2.58 |
| 11-22 06:55 | +10 | BTC | DOWN | 0.66 | 0.94 | 2.58 |
| 11-22 06:55 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-22 06:52 | +10 stop | SOL | DOWN | 0.64 | 0.48 | -1.95 |
| 11-22 06:51 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-22 06:51 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
| 11-22 06:51 | +5 | SOL | UP | 0.59 | 0.74 | 1.19 |
| 11-22 06:51 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 11-22 06:51 | +10 stop | XRP | DOWN | 0.71 | 0.85 | 1.16 |
| 11-22 06:51 | +10 stop | NEAR | UP | 0.54 | 0.33 | -2.42 |
| 11-22 06:51 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-22 06:51 | +10 stop | ZEC | UP | 0.67 | 0.47 | -2.34 |
| 11-22 06:50 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 06:50 | +10 stop | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-22 06:49 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.94 |
| 11-22 06:49 | +10 stop | XRP | UP | 0.65 | 0.46 | -2.24 |
| 11-22 06:49 | +10 stop | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-22 06:49 | +10 stop | ETH | UP | 0.61 | 0.45 | -1.95 |
| 11-22 06:49 | +10 stop | BTC | UP | 0.57 | 0.36 | -2.45 |
