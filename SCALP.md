# Range-Scalp Bot

*Updated Tue Nov 24 07:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70621 | 61642 | 8979 (148) | 4 | $-18879.36 | -4.2% |
| **+10¢** | 52676 | 42193 | 10483 (193) | 5 | $-17472.34 | -5.3% |
| **+15¢** | 44134 | 32843 | 11291 (250) | 3 | $-15527.14 | -5.6% |
| **+20¢** | 39304 | 27418 | 11886 (316) | 3 | $-13875.18 | -5.6% |
| **+10¢ (15¢ stop)** | 85995 | 85797 | 198 (118) | 0 | $-31617.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 07:41 | +10 stop | BNB | DOWN | 0.56 | 0.32 | -2.74 |
| 11-24 07:41 | +20 | BNB | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 07:41 | +15 | BNB | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 07:41 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-24 07:41 | +5 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-24 07:41 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-24 07:41 | +20 | ETH | UP | 0.65 | 0.92 | 2.53 |
| 11-24 07:41 | +15 | ETH | UP | 0.65 | 0.81 | 1.33 |
| 11-24 07:41 | +10 | ETH | UP | 0.65 | 0.81 | 1.33 |
| 11-24 07:41 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-24 07:41 | +10 stop | BTC | DOWN | 0.65 | 0.42 | -2.64 |
| 11-24 07:41 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-24 07:41 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-24 07:41 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-24 07:41 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-24 07:39 | +5 | NEAR | DOWN | 0.54 | 0.61 | 0.35 |
| 11-24 07:39 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-24 07:39 | +20 | XRP | DOWN | 0.63 | 0.89 | 2.36 |
| 11-24 07:39 | +15 | XRP | DOWN | 0.64 | 0.89 | 2.26 |
| 11-24 07:39 | +10 stop | HYPE | UP | 0.58 | 0.19 | -4.19 |
| 11-24 07:39 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-24 07:39 | +10 stop | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 11-24 07:39 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.14 |
| 11-24 07:39 | +5 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-24 07:38 | +10 stop | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 11-24 07:37 | +5 | BNB | UP | 0.55 | 0.70 | 1.15 |
| 11-24 07:37 | +10 stop | HYPE | UP | 0.57 | 0.35 | -2.54 |
| 11-24 07:37 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 07:37 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.86 |
| 11-24 07:37 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-24 07:36 | +10 stop | XRP | DOWN | 0.59 | 0.78 | 1.60 |
| 11-24 07:36 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-24 07:36 | +15 | XRP | DOWN | 0.55 | 0.78 | 1.99 |
| 11-24 07:36 | +5 | BNB | UP | 0.68 | 0.77 | 0.61 |
| 11-24 07:36 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-24 07:35 | +5 | HYPE | UP | 0.60 | open |  |
| 11-24 07:35 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.62 |
| 11-24 07:35 | +10 stop | XRP | UP | 0.56 | 0.38 | -2.15 |
| 11-24 07:35 | +10 | XRP | UP | 0.56 | open |  |
| 11-24 07:35 | +5 | XRP | UP | 0.56 | open |  |
