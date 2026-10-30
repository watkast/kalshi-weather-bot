# Range-Scalp Bot

*Updated Fri Oct 30 12:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40772 | 35583 | 5189 (51) | 2 | $-11421.54 | -4.4% |
| **+10¢** | 30372 | 24371 | 6001 (74) | 2 | $-10187.95 | -5.3% |
| **+15¢** | 25388 | 18927 | 6461 (101) | 2 | $-9230.55 | -5.8% |
| **+20¢** | 22534 | 15763 | 6771 (131) | 2 | $-8144.07 | -5.8% |
| **+10¢ (15¢ stop)** | 49711 | 49641 | 70 (37) | 0 | $-18826.77 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 12:28 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 12:28 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 12:28 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 12:28 | +10 stop | HYPE | UP | 0.71 | 0.21 | -5.26 |
| 10-30 12:28 | +10 stop | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 10-30 12:27 | +10 stop | SOL | UP | 0.51 | 0.61 | 0.65 |
| 10-30 12:27 | +20 | SOL | UP | 0.51 | no | -5.28 |
| 10-30 12:27 | +15 | SOL | UP | 0.51 | no | -5.28 |
| 10-30 12:27 | +10 | SOL | UP | 0.51 | 0.61 | 0.65 |
| 10-30 12:27 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 10-30 12:27 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-30 12:27 | +20 | DOGE | DOWN | 0.61 | 0.93 | 2.96 |
| 10-30 12:27 | +15 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-30 12:27 | +10 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-30 12:27 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 10-30 12:26 | +10 | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-30 12:26 | +10 stop | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-30 12:26 | +10 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-30 12:26 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 10-30 12:26 | +10 stop | ZEC | DOWN | 0.60 | 0.19 | -4.38 |
| 10-30 12:26 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-30 12:26 | +10 stop | XRP | DOWN | 0.60 | 0.43 | -2.05 |
| 10-30 12:26 | +5 | ZEC | DOWN | 0.69 | yes | -7.05 |
| 10-30 12:25 | +10 stop | NEAR | DOWN | 0.63 | 0.42 | -2.45 |
| 10-30 12:25 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-30 12:25 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-30 12:25 | +10 stop | HYPE | UP | 0.63 | 0.88 | 2.21 |
| 10-30 12:25 | +10 stop | ZEC | UP | 0.54 | 0.39 | -1.85 |
| 10-30 12:25 | +5 | ZEC | UP | 0.54 | 0.59 | 0.15 |
| 10-30 12:25 | +10 stop | XRP | UP | 0.63 | 0.42 | -2.45 |
| 10-30 12:24 | +5 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-30 12:24 | +5 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-30 12:24 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-30 12:24 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-30 12:24 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 10-30 12:24 | +5 | BTC | DOWN | 0.47 | 0.62 | 1.15 |
| 10-30 12:23 | +10 stop | HYPE | DOWN | 0.70 | 0.45 | -2.83 |
| 10-30 12:23 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-30 12:23 | +10 stop | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 10-30 12:23 | +10 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
