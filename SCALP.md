# Range-Scalp Bot

*Updated Sat Nov 14 08:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59217 | 51667 | 7550 (107) | 1 | $-16005.30 | -4.3% |
| **+10¢** | 44235 | 35401 | 8834 (140) | 4 | $-15023.49 | -5.4% |
| **+15¢** | 37066 | 27540 | 9526 (176) | 4 | $-13668.17 | -5.9% |
| **+20¢** | 33015 | 23014 | 10001 (228) | 6 | $-12073.25 | -5.8% |
| **+10¢ (15¢ stop)** | 72065 | 71923 | 142 (82) | 0 | $-26509.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 08:25 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-14 08:24 | +10 stop | BTC | DOWN | 0.52 | 0.86 | 3.13 |
| 11-14 08:24 | +15 | BTC | DOWN | 0.52 | 0.86 | 3.13 |
| 11-14 08:24 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 11-14 08:23 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 08:23 | +10 stop | NEAR | UP | 0.52 | 0.32 | -2.34 |
| 11-14 08:23 | +10 | NEAR | UP | 0.52 | open |  |
| 11-14 08:23 | +5 | NEAR | UP | 0.52 | 0.61 | 0.55 |
| 11-14 08:23 | +10 stop | BNB | UP | 0.60 | 0.41 | -2.24 |
| 11-14 08:22 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 08:22 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 08:22 | +10 stop | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-14 08:22 | +20 | SOL | UP | 0.68 | open |  |
| 11-14 08:22 | +15 | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-14 08:22 | +10 | SOL | UP | 0.68 | 0.85 | 1.44 |
| 11-14 08:22 | +5 | SOL | UP | 0.68 | 0.75 | 0.39 |
| 11-14 08:22 | +5 | ETH | UP | 0.62 | 0.69 | 0.38 |
| 11-14 08:22 | +10 stop | ZEC | DOWN | 0.71 | 0.49 | -2.53 |
| 11-14 08:22 | +15 | XRP | UP | 0.69 | open |  |
| 11-14 08:22 | +10 | XRP | UP | 0.69 | 0.81 | 0.94 |
| 11-14 08:22 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 11-14 08:22 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-14 08:22 | +20 | XRP | UP | 0.70 | open |  |
| 11-14 08:21 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-14 08:21 | +5 | NEAR | UP | 0.61 | 0.68 | 0.37 |
| 11-14 08:21 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-14 08:21 | +10 stop | BTC | DOWN | 0.51 | 0.64 | 0.95 |
| 11-14 08:21 | +5 | BTC | DOWN | 0.51 | 0.60 | 0.55 |
| 11-14 08:20 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.45 |
| 11-14 08:20 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-14 08:20 | +20 | NEAR | UP | 0.57 | open |  |
| 11-14 08:20 | +15 | NEAR | UP | 0.57 | open |  |
| 11-14 08:20 | +10 | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-14 08:20 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 11-14 08:19 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-14 08:19 | +10 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-14 08:19 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-14 08:19 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.34 |
