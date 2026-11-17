# Range-Scalp Bot

*Updated Tue Nov 17 03:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62502 | 54528 | 7974 (117) | 5 | $-16926.75 | -4.3% |
| **+10¢** | 46686 | 37355 | 9331 (159) | 5 | $-15797.07 | -5.4% |
| **+15¢** | 39131 | 29066 | 10065 (201) | 5 | $-14348.95 | -5.8% |
| **+20¢** | 34877 | 24321 | 10556 (256) | 5 | $-12528.76 | -5.7% |
| **+10¢ (15¢ stop)** | 76076 | 75920 | 156 (92) | 1 | $-28009.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 03:43 | +10 stop | BNB | UP | 0.67 | open |  |
| 11-17 03:42 | +10 stop | ZEC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-17 03:42 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.78 |
| 11-17 03:42 | +10 stop | ZEC | DOWN | 0.35 | 0.54 | 1.56 |
| 11-17 03:41 | +10 stop | XRP | DOWN | 0.56 | 0.38 | -2.15 |
| 11-17 03:41 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-17 03:41 | +15 | XRP | DOWN | 0.57 | open |  |
| 11-17 03:41 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-17 03:41 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-17 03:41 | +10 stop | NEAR | UP | 0.71 | 0.91 | 1.78 |
| 11-17 03:41 | +20 | NEAR | UP | 0.71 | 0.93 | 1.99 |
| 11-17 03:41 | +15 | NEAR | UP | 0.71 | 0.91 | 1.78 |
| 11-17 03:41 | +10 | NEAR | UP | 0.71 | 0.91 | 1.78 |
| 11-17 03:41 | +5 | NEAR | UP | 0.71 | 0.79 | 0.56 |
| 11-17 03:41 | +10 stop | BNB | DOWN | 0.62 | 0.42 | -2.37 |
| 11-17 03:41 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-17 03:41 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-17 03:41 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-17 03:41 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.95 |
| 11-17 03:41 | +20 | ETH | UP | 0.71 | 0.91 | 1.79 |
| 11-17 03:41 | +15 | ETH | UP | 0.70 | 0.91 | 1.89 |
| 11-17 03:41 | +10 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 11-17 03:41 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 11-17 03:40 | +10 stop | SOL | UP | 0.62 | 0.80 | 1.51 |
| 11-17 03:40 | +15 | SOL | UP | 0.61 | 0.80 | 1.61 |
| 11-17 03:40 | +10 | SOL | UP | 0.61 | 0.80 | 1.61 |
| 11-17 03:40 | +5 | SOL | UP | 0.61 | 0.80 | 1.61 |
| 11-17 03:40 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-17 03:40 | +10 stop | ZEC | UP | 0.60 | 0.38 | -2.54 |
| 11-17 03:40 | +20 | ZEC | UP | 0.60 | open |  |
| 11-17 03:40 | +15 | ZEC | UP | 0.60 | open |  |
| 11-17 03:40 | +10 | ZEC | UP | 0.60 | open |  |
| 11-17 03:40 | +5 | ZEC | UP | 0.60 | open |  |
| 11-17 03:39 | +10 stop | DOGE | UP | 0.69 | 0.53 | -1.93 |
| 11-17 03:39 | +10 | DOGE | UP | 0.69 | open |  |
| 11-17 03:39 | +5 | DOGE | UP | 0.71 | open |  |
| 11-17 03:38 | +10 stop | BTC | UP | 0.66 | 0.46 | -2.34 |
| 11-17 03:38 | +5 | BTC | UP | 0.66 | open |  |
| 11-17 03:34 | +10 stop | DOGE | UP | 0.59 | 0.70 | 0.79 |
| 11-17 03:33 | +10 stop | ETH | UP | 0.66 | 0.80 | 1.12 |
