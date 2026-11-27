# Range-Scalp Bot

*Updated Fri Nov 27 07:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73552 | 64190 | 9362 (165) | 1 | $-19602.15 | -4.2% |
| **+10¢** | 54808 | 43874 | 10934 (210) | 1 | $-18240.45 | -5.3% |
| **+15¢** | 45897 | 34120 | 11777 (268) | 1 | $-16340.45 | -5.7% |
| **+20¢** | 40845 | 28443 | 12402 (334) | 1 | $-14755.01 | -5.8% |
| **+10¢ (15¢ stop)** | 89581 | 89369 | 212 (129) | 1 | $-33151.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 07:54 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 11-27 07:52 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.24 |
| 11-27 07:51 | +10 stop | HYPE | UP | 0.58 | 0.41 | -2.03 |
| 11-27 07:49 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.94 |
| 11-27 07:49 | +10 stop | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-27 07:49 | +20 | ZEC | UP | 0.71 | 0.93 | 1.95 |
| 11-27 07:49 | +15 | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-27 07:49 | +10 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-27 07:49 | +5 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-27 07:47 | +10 stop | HYPE | UP | 0.68 | 0.47 | -2.44 |
| 11-27 07:47 | +20 | HYPE | UP | 0.68 | open |  |
| 11-27 07:47 | +15 | HYPE | UP | 0.68 | open |  |
| 11-27 07:47 | +10 | HYPE | UP | 0.68 | open |  |
| 11-27 07:47 | +5 | HYPE | UP | 0.68 | open |  |
| 11-27 07:46 | +5 | BTC | UP | 0.65 | 0.70 | 0.23 |
| 11-27 07:45 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-27 07:45 | +20 | BTC | UP | 0.60 | 0.80 | 1.71 |
| 11-27 07:45 | +15 | BTC | UP | 0.60 | 0.79 | 1.61 |
| 11-27 07:45 | +10 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-27 07:45 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 11-27 07:42 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.89 |
| 11-27 07:40 | +10 stop | XRP | UP | 0.62 | 0.88 | 2.30 |
| 11-27 07:39 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.84 |
| 11-27 07:39 | +5 | SOL | UP | 0.62 | 0.73 | 0.79 |
| 11-27 07:38 | +10 stop | XRP | UP | 0.51 | 0.61 | 0.65 |
| 11-27 07:38 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 11-27 07:38 | +10 stop | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +20 | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +15 | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +10 | SOL | UP | 0.69 | 0.93 | 2.21 |
| 11-27 07:38 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 11-27 07:37 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.75 |
| 11-27 07:37 | +15 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-27 07:37 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-27 07:36 | +5 | BNB | UP | 0.39 | 0.68 | 2.57 |
| 11-27 07:36 | +10 stop | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 11-27 07:35 | +5 | NEAR | UP | 0.60 | no | -6.17 |
| 11-27 07:34 | +10 stop | ETH | UP | 0.69 | 0.52 | -2.07 |
| 11-27 07:34 | +10 | ETH | UP | 0.69 | no | -7.09 |
| 11-27 07:33 | +20 | DOGE | UP | 0.71 | no | -7.25 |
